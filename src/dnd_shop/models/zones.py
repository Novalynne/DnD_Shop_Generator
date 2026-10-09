from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from dnd_shop.models.product import Category


# ============================================================================
# TIPI DI EFFETTO
# ============================================================================

class ZoneEffectType(Enum):
    """
    Tipi di effetti economici che una zona può applicare.

    GLOBAL_PRICE_MODIFIER
        Modifica il prezzo di tutti i prodotti della zona.

    CATEGORY_PRICE_MODIFIER
        Modifica il prezzo dei prodotti appartenenti
        a una o più categorie specifiche.

    MAGICAL_LEVEL_MODIFIER
        Modifica il prezzo di tutti i prodotti con
        magic=True, indipendentemente dalla loro categoria.
    """

    GLOBAL_PRICE_MODIFIER = "global_price_modifier"
    CATEGORY_PRICE_MODIFIER = "category_price_modifier"
    MAGICAL_LEVEL_MODIFIER = "magical_level_modifier"


# ============================================================================
# EFFETTO DI UNA ZONA
# ============================================================================

@dataclass
class ZoneEffect:
    """
    Rappresenta un singolo effetto economico applicato da una zona.

    modifier:
        Percentuale espressa come numero decimale.

        Esempi:
            +20% -> 0.20
            -50% -> -0.50
            +30% -> 0.30

    target:
        Lista di categorie a cui applicare l'effetto.

        Viene utilizzato solo con CATEGORY_PRICE_MODIFIER.

        Esempi:
            [Category("Pesce")]
            [Category("Armi"), Category("Armature")]

        Per GLOBAL_PRICE_MODIFIER e MAGICAL_LEVEL_MODIFIER
        deve essere None.

    description:
        Descrizione leggibile dell'effetto.
    """

    effect_type: ZoneEffectType
    modifier: float = 0.0
    target: Optional[list[Category]] = None
    description: str = ""


# ============================================================================
# ZONA
# ============================================================================

@dataclass
class Zone:
    """
    Rappresenta una zona geografica del mondo di gioco.

    Una zona può avere più effetti contemporaneamente.
    """

    name: str
    description: str
    effects: list[ZoneEffect] = field(default_factory=list)

    def add_effect(self, effect: ZoneEffect) -> None:
        """Aggiunge un effetto economico alla zona."""
        self.effects.append(effect)


# ============================================================================
# PERCENTUALI BASE DELLE ZONE
# ============================================================================
#
# Tutti i modifier sono espressi come numeri decimali:
#
#     0.20  = +20%
#    -0.50  = -50%
#     0.35  = +35%
#
# Questi valori potranno in futuro essere modificati tramite GUI
# e salvati nel database senza modificare la logica del programma.
# ============================================================================

ZONE_MODIFIERS = {

    # Ricchezza
    "zona_estremamente_ricca": 0.70,
    "zona_ricca": 0.50,
    "zona_povera": -0.50,
    "zona_estremamente_povera": -0.80,

    # Commercio / turismo
    "zona_turistica": 0.25,
    "zona_deserta": -0.40,
    "zona_alto_commercio": -0.10,

    # Produzione / risorse
    "zona_pesca": 0.20,
    "zona_montagna": 0.20,
    "zona_pianura": 0.20,

    # Sviluppo magico
    "zona_alta_istruzione_magica": 0.20,
    "zona_bassa_istruzione_magica": -0.20,

    # Economia generale
    "zona_inflazione": 0.25,
}


# ============================================================================
# EFFETTI GLOBALI
# ============================================================================

# ---------------------------------------------------------------------------
# Ricchezza
# ---------------------------------------------------------------------------

zona_estremamente_ricca = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_estremamente_ricca"],
    description="Rincaro del 70% su tutti i prodotti.",
)

zona_ricca = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_ricca"],
    description="Rincaro del 50% su tutti i prodotti.",
)

zona_povera = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_povera"],
    description="Sconto del 50% su tutti i prodotti.",
)

zona_estremamente_povera = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_estremamente_povera"],
    description="Sconto dell'80% su tutti i prodotti.",
)


# ---------------------------------------------------------------------------
# Turismo
# ---------------------------------------------------------------------------

zona_turistica = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_turistica"],
    description="Rincaro del 25% su tutti i prodotti.",
)


# ---------------------------------------------------------------------------
# Zona deserta
# ---------------------------------------------------------------------------

zona_deserta = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_deserta"],
    description="Sconto del 40% dovuto alla scarsa domanda e alla difficoltà di commercio.",
)


# ---------------------------------------------------------------------------
# Alto commercio
# ---------------------------------------------------------------------------

zona_alto_commercio = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_alto_commercio"],
    description="Riduzione del 10% grazie all'elevata disponibilità di merci.",
)


# ---------------------------------------------------------------------------
# Inflazione
# ---------------------------------------------------------------------------

zona_inflazione = ZoneEffect(
    effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_inflazione"],
    description="Rincaro del 25% su tutti i prodotti.",
)


# ============================================================================
# EFFETTI BASATI SULLA CATEGORIA
# ============================================================================

# ---------------------------------------------------------------------------
# Zona mineraria
# ---------------------------------------------------------------------------

zona_mineraria = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_montagna"],
    target=[
        Category("Armi"),
        Category("Armature"),
    ],
    description="Le armi e le armature realizzate con minerali di maggiore qualità ricevono un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di pesca
# ---------------------------------------------------------------------------

zona_pesca = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pesca"],
    target=[
        Category("Pesce"),
    ],
    description="Il pesce riceve un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona montana - carne
# ---------------------------------------------------------------------------

zona_carne = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_montagna"],
    target=[
        Category("Carne"),
    ],
    description="La carne riceve un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di pianura - frutta
# ---------------------------------------------------------------------------

zona_frutta = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pianura"],
    target=[
        Category("Frutta"),
    ],
    description="La frutta riceve un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di pianura - verdure
# ---------------------------------------------------------------------------

zona_verdura = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pianura"],
    target=[
        Category("Verdure"),
    ],
    description="Le verdure ricevono un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di pianura - farina
# ---------------------------------------------------------------------------

zona_farina = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pianura"],
    target=[
        Category("Farina"),
    ],
    description="La farina riceve un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di pianura - legumi
# ---------------------------------------------------------------------------

zona_legumi = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pianura"],
    target=[
        Category("Legumi"),
    ],
    description="I legumi ricevono un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di produzione di alcolici
# ---------------------------------------------------------------------------

zona_alcolici = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pianura"],
    target=[
        Category("Alcolici"),
        Category("Super Alcolici"),
    ],
    description="Gli alcolici ricevono un rincaro del 20%.",
)


# ---------------------------------------------------------------------------
# Zona di produzione di gioielli e vestiti
# ---------------------------------------------------------------------------

zona_gioielli_vestiti = ZoneEffect(
    effect_type=ZoneEffectType.CATEGORY_PRICE_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_pianura"],
    target=[
        Category("Gioielli"),
        Category("Vestiti"),
    ],
    description="I gioielli e i vestiti ricevono un rincaro del 20%.",
)


# ============================================================================
# EFFETTI BASATI SULLO SVILUPPO MAGICO
# ============================================================================
#
# Questi effetti NON utilizzano target.
#
# Il price_calculator.py controllerà:
#
#     product.magic == True
#
# indipendentemente dalla categoria del prodotto.
#
# Quindi l'effetto si applica sia a:
#
#     Spada +1
#     Armatura magica
#     Pozione
#     Bacchetta
#     Pergamena magica
#     ecc.
#
# purché product.magic sia True.
# ============================================================================

zona_alta_istruzione_magica = ZoneEffect(
    effect_type=ZoneEffectType.MAGICAL_LEVEL_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_alta_istruzione_magica"],
    description="L'elevato sviluppo magico della zona aumenta del 20% il prezzo di tutti gli oggetti magici.",
)


zona_bassa_istruzione_magica = ZoneEffect(
    effect_type=ZoneEffectType.MAGICAL_LEVEL_MODIFIER,
    modifier=ZONE_MODIFIERS["zona_bassa_istruzione_magica"],
    description="Il basso sviluppo magico della zona riduce del 20% il prezzo di tutti gli oggetti magici.",
)


# ============================================================================
# ELENCO DI TUTTI GLI EFFETTI DISPONIBILI
# ============================================================================

ZONES_EFFECTS = [
    # Globali
    zona_estremamente_ricca,
    zona_ricca,
    zona_povera,
    zona_estremamente_povera,
    zona_turistica,
    zona_deserta,
    zona_alto_commercio,
    zona_inflazione,

    # Categorie
    zona_mineraria,
    zona_pesca,
    zona_carne,
    zona_frutta,
    zona_verdura,
    zona_farina,
    zona_legumi,
    zona_alcolici,
    zona_gioielli_vestiti,

    # Sviluppo magico
    zona_alta_istruzione_magica,
    zona_bassa_istruzione_magica,
]