from data import PRODUCTS
from models.product import Product, Category, Rarity
from models.shop import Shop, ShopType
import random

class ShopGenerator:

    # ---------------------------------------------------------------------------
    # METODI CASUALI PER LA GENERAZIONE DI PRODOTTI
    # ---------------------------------------------------------------------------

    @staticmethod
    def generate_random_name() -> str:
        """
        Genera un nome casuale per il negozio.

        Returns:
            str: Un nome casuale per il negozio.
        """

    @staticmethod
    def generate_random_description() -> str:
        """
        Genera una descrizione casuale per il negozio.

        Returns:
            str: Una descrizione casuale per il negozio.
        """

    @staticmethod
    def generate_random_rarity() -> Rarity:
        """
        Genera una rarità casuale per un prodotto.

        Returns:
            Rarity: Una rarità casuale.
        """
        return random.choice(list(Rarity))

    @staticmethod
    def generate_random_category(allowed_categories: list[Category]) -> Category:
        """
        Genera una categoria casuale da una lista di categorie consentite.

        Args:
            allowed_categories (list[Category]): La lista di categorie consentite.

        Returns:
            Category: Una categoria casuale.
        """
        return random.choice(allowed_categories)

    @staticmethod
    def generate_random_magical_property() -> bool:
        """
        Genera una proprietà magica casuale per un prodotto.

        Returns:
            bool: True se il prodotto è magico, False altrimenti.
        """
        return random.choice([True, False])

    @staticmethod
    def generate_random_products(num_products: int = 10) -> list[Product]:
        """
        Genera una lista di prodotti casuali da una lista di prodotti disponibili.

        Args:
            products (list[Product]): La lista di prodotti disponibili.
            num_products (int, optional): Il numero di prodotti da generare. Default è 10.

        Returns:
            list[Product]: Una lista di prodotti casuali.
        """

    # ---------------------------------------------------------------------------
    # METODI CASUALI PER LA GENERAZIONE DI NEGOZI
    # ---------------------------------------------------------------------------

    @staticmethod
    def generate_shop_name() -> str:
        """
        Genera un nome casuale per il negozio.

        Returns:
            str: Un nome casuale per il negozio.
        """

    @staticmethod
    def generate_shop_description() -> str:
        """
        Genera una descrizione casuale per il negozio.

        Returns:
            str: Una descrizione casuale per il negozio.
        """

    @staticmethod
    def generate_shop(type: ShopType, allowed_categories: list[Category], zone=None, num_products: int = 10) -> Shop:
        """
        Genera un negozio con prodotti casuali.

        Args:
            allowed_categories (list[Category]): Le categorie di prodotti consentite nel negozio.
            zone (Zone, optional): La zona geografica del negozio. Default è None.
            num_products (int, optional): Il numero di prodotti da generare. Default è 10.

        Returns:
            Shop: Un oggetto Shop con prodotti generati casualmente.
        """
        
        # Crea il negozio con i prodotti filtrati
        shop = Shop(
            type=type,
            name=Shop.generate_shop_name(),
            description=Shop.generate_shop_description(),
            allowed_categories=allowed_categories,
            products=Shop.generate_random_products(num_products),
            zone=zone
        )

        return shop