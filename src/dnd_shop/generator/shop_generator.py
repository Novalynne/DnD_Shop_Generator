from unicodedata import category

from dnd_shop.data.product_catalogue import PRODUCTS
from dnd_shop.models.product import Product, Category, Rarity, RARITIES
from dnd_shop.models.shop import Shop, ShopType
from dnd_shop.generator.ai_generator import AIGenerator
from dnd_shop.utils.price_calculator import PriceCalculator

import random


class ShopGenerator:

    ai = AIGenerator()

    # ---------------------------------------------------------------------------
    # GENERAZIONE PRODOTTI
    # ---------------------------------------------------------------------------

    @staticmethod
    def generate_random_rarity() -> Rarity:
        return random.choice(RARITIES)

    @staticmethod
    def generate_random_magical_property() -> bool:
        return random.choice([True, False])

    @staticmethod
    def get_all_subcategories(category: Category) -> list[Category]:
        categories = [category]

        for subcategory in category.subcategories:
            categories.extend(
                ShopGenerator.get_all_subcategories(subcategory)
            )

        return categories

    @staticmethod
    def generate_random_products(
        allowed_categories: list[Category],
        num_products: int = 10,
        zone=None
    ) -> list[Product]:

        all_allowed_categories = []

        for category in allowed_categories:
            all_allowed_categories.extend(
                ShopGenerator.get_all_subcategories(category)
            )

        available_products = [
            product
            for product in PRODUCTS
            if product.category in all_allowed_categories
        ]

        if not available_products:
            raise ValueError(
                "Non ci sono prodotti disponibili per questo shop."
            )

        generated_products = []

        for _ in range(num_products):

            # 1. Scegliamo il prodotto base
            base_product = random.choice(available_products)

            # 2. Generiamo le proprietà dinamiche
            rarity = ShopGenerator.generate_random_rarity()
            is_magical = ShopGenerator.generate_random_magical_property()
                
            if (_ == num_products-1):
                # 3. Chiediamo all'AI nome e descrizione solo per l'ultimo oggetto
                #    in modo tale da evitare di fare troppe chiamate all'ai dato che
                #    si usa per la generazione un modello gratuito e quindi soggetto a
                #    limitazioni
                name, description = ShopGenerator.ai.generate_product(
                    base_product=base_product,
                    is_magical=is_magical,
                    rarity=rarity.name
                )
            else:
                name = base_product.name
                description = base_product.description or "Nessuna descrizione disponibile."

            # 4. Creiamo il prodotto e li assegniamo il prezzo di base nel catalogo
            product = Product(
                id=base_product.id,
                name=name,
                category=base_product.category,
                base_price_mr=base_product.base_price_mr,
                description=description,
                is_magical=is_magical,
                rarity=rarity
            )

            # 5. Calcola il prezzo del prodotto a seconda della zona
            product_price = PriceCalculator.calculate(product= product, zone= zone)
            product.base_price_mr = product_price

            generated_products.append(product)

        return generated_products

    # ---------------------------------------------------------------------------
    # GENERAZIONE SHOP
    # ---------------------------------------------------------------------------

    @staticmethod
    def generate_shop(
        shop_type: ShopType,
        allowed_categories: list[Category],
        zone=None,
        num_products: int = 10
    ) -> Shop:

        # Nome e descrizione dello shop generati dall'AI
        name, description = ShopGenerator.ai.generate_shop(
            shop_type=shop_type,
            allowed_categories=allowed_categories
        )

        # Generazione dei prodotti
        products = ShopGenerator.generate_random_products(
            allowed_categories=allowed_categories,
            num_products=num_products,
            zone=zone
        )

        return Shop(
            type=shop_type,
            name=name,
            description=description,
            allowed_categories=allowed_categories,
            products=products,
            zone=zone
        )