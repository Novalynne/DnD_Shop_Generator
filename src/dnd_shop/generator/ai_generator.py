import os
import re
from unittest import result
from urllib import response
from urllib import response

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import errors

from dnd_shop.models.product import Product


# Carica le variabili definite nel file .env
load_dotenv()


class AIGenerator:
    """Genera nomi e descrizioni fantasy tramite Google Gemini."""

    def __init__(self, model=None):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "Chiave API mancante. "
                "Inserisci GEMINI_API_KEY nel file .env."
            )

        #self.client = genai.Client(api_key=api_key)
        self.client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(
                retry_options=types.HttpRetryOptions(
                    attempts=5,
                    initial_delay=1,
                    max_delay=10,
                    exp_base=2,
                    jitter=1,
                )
            ),
        )

        # Il modello può essere sostituito senza modificare i metodi.
        self.model = model or os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        )

    def _generate_text_dyagnostic(self, prompt):
        """Invia un prompt a Gemini e restituisce il testo generato."""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=1024,
                thinking_config=types.ThinkingConfig(
                    thinking_level="low",
                ),
            ),
        )

        print("\n--- DIAGNOSTICA GEMINI ---")
        print("Modello:", self.model)
        print("Prompt feedback:", response.prompt_feedback)
        print("Numero candidati:", len(response.candidates or []))
        
        for candidate in response.candidates or []:
            print("Finish reason:", candidate.finish_reason)
            print("Contenuto candidato:", candidate.content)
        
        text = response.text
        
        print("Testo estratto:", repr(text))
        print("--- FINE DIAGNOSTICA ---\n")
        
        if not text or not text.strip():
            raise RuntimeError(
                "Gemini non ha restituito testo utilizzabile."
            )
        
        return text.strip()
    
    def _generate_text(self, prompt):
        """Invia un prompt a Gemini e restituisce il testo generato."""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.9,
                max_output_tokens=350,
            ),
        )

        text = response.text

        if not text or not text.strip():
            raise RuntimeError(
                "Gemini non ha restituito alcun testo."
            )

        return text.strip()
    
    @staticmethod
    def _parse_response(text):
        """Estrae nome e descrizione dalla risposta di Gemini."""

        # Rimuove eventuali delimitatori Markdown.
        text = text.strip()
        text = re.sub(r"^```(?:text|markdown)?\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s*```$", "", text)

        # Cerca i due campi, consentendo più righe nella descrizione.
        match = re.search(
            r"Nome:\s*(.*?)\s*Descrizione:\s*(.*)",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if not match:
            raise ValueError(
                "Formato della risposta AI non valido. "
                f"Risposta ricevuta: {text!r}"
            )

        name = match.group(1).strip()
        description = match.group(2).strip()

        # Rimuove gli asterischi eventualmente usati per il Markdown.
        name = name.strip("*` ")
        description = description.strip()

        if not name or not description:
            raise ValueError(
                "Nome o descrizione generati sono vuoti."
            )

        return name, description

    def generate_product(
        self,
        base_product,
        is_magical,
        rarity,
    ):
        """
        Genera nome e descrizione di un oggetto.

        Args:
            base_product: dizionario con i dati dell'oggetto
                          oppure stringa descrittiva.
            is_magical: indica se l'oggetto è magico.
            rarity: rarità dell'oggetto.

        Returns:
            tuple[str, str]: nome e descrizione.
        """

        if isinstance(base_product, Product):
            product_type = base_product.name
            category = base_product.category.name
            base_description = (
                base_product.description
                or "Nessuna descrizione disponibile."
            )
        elif isinstance(base_product, dict):
            product_type = base_product.get(
                "name",
                base_product.get(
                    "nome",
                    base_product.get("type", "Oggetto")
                ),
            )

            category = base_product.get(
                "category",
                base_product.get("categoria", "Generica"),
            )

            base_description = base_product.get(
                "description",
                base_product.get(
                    "descrizione",
                    "Nessuna descrizione disponibile."
                ),
            )
        else:
            product_type = str(base_product)
            category = "Generica"
            base_description = str(base_product)

        magic_status = (
            "magico"
            if is_magical
            else "non magico"
        )

        prompt = f"""
Sei uno scrittore fantasy specializzato in oggetti
per campagne di Dungeons & Dragons.

Genera un nome originale e una descrizione immersiva
in italiano per il seguente oggetto.

Tipo di oggetto: {product_type}
Categoria: {category}
Descrizione di partenza: {base_description}
Natura: {magic_status}
Rarità: {rarity}

REGOLE:
- Scrivi esclusivamente in italiano.
- Il nome deve essere evocativo, breve e originale.
- La descrizione deve essere coerente con il tipo
  di oggetto e con la sua rarità.
- Se l'oggetto non è magico, non attribuirgli poteri.
- Non inventare statistiche, prezzi o bonus meccanici.
- Rispetta la descrizione di partenza.
- Non aggiungere testo introduttivo o commenti.

Usa esattamente questo formato:

Nome: [nome dell'oggetto]
Descrizione: [descrizione dell'oggetto]
"""

        try:
            result = self._generate_text_dyagnostic(prompt)
            print("RISPOSTA GREZZA GEMINI:", repr(result))
            return self._parse_response(result)

        except errors.ServerError as exc:
            if exc.code == 503:
                raise RuntimeError(
                    "Gemini è temporaneamente sovraccarico. "
                    "Riprova tra qualche minuto."
            ) from exc

            raise

    def generate_shop(
        self,
        shop_type,
        allowed_categories,
    ):
        """
        Genera nome e descrizione di un negozio.

        Returns:
            tuple[str, str]: nome e descrizione.
        """

        categories = ", ".join(
            str(category)
            for category in allowed_categories
        )

        prompt = f"""
Sei uno scrittore fantasy specializzato
nella creazione di ambientazioni per Dungeons & Dragons.

Crea un negozio fantasy originale.

Tipo di negozio: {shop_type}
Categorie di prodotti consentite: {categories}

REGOLE:
- Scrivi esclusivamente in italiano.
- Crea un nome memorabile e adatto all'ambientazione.
- Descrivi l'aspetto del negozio, la sua atmosfera
  e ciò che lo rende caratteristico.
- Mantieni la descrizione coerente con le categorie
  di prodotti consentite.
- Non inventare prezzi o inventari specifici.
- Non aggiungere testo introduttivo o commenti.

Usa esattamente questo formato:

Nome: [nome del negozio]
Descrizione: [descrizione del negozio]
"""

        try:
            result = self._generate_text_dyagnostic(prompt)
            print("RISPOSTA GREZZA GEMINI:", repr(result))
            return self._parse_response(result)
        
        except errors.ServerError as exc:
            if exc.code == 503:
                raise RuntimeError(
                        "Gemini è temporaneamente sovraccarico. "
                        "Riprova tra qualche minuto."
                ) from exc
        
            raise