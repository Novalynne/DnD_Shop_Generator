from models import Product
from models import Zone, ZoneEffectType


class PriceCalculator:

    MAGICAL_SURCHARGE_MO = 1000

    @staticmethod
    def calculate(product: Product, zone: Zone | None = None) -> int:
        """
        Calcola il prezzo finale di un prodotto in MR.

        Regole:
        - prodotto normale:
            base_price × rarità
        - prodotto magico:
            (base_price + 1000 MO) × rarità
        - prodotti della categoria 'Oggetti magici':
            non ricevono il +1000 MO
        - gli effetti della zona vengono sommati tra loro
        """

        # 1. Prezzo di partenza
        price_mr = product.base_price_mr

        # 2. Sovrapprezzo per oggetto magico
        if product.is_magical and product.category.name != "Oggetti magici":
            price_mr += PriceCalculator.MAGICAL_SURCHARGE_MO * 100

        # 3. Moltiplicatore della rarità
        price_mr *= product.rarity.multiplier

        # 4. Effetti della zona
        if zone is not None:
            total_zone_modifier = PriceCalculator._calculate_zone_modifier(
                product,
                zone
            )

            price_mr *= (1 + total_zone_modifier)

        # 5. Il prezzo finale è espresso in MR intere
        return max(1, round(price_mr))

    @staticmethod
    def _calculate_zone_modifier(
        product: Product,
        zone: Zone
    ) -> float:

        total_modifier = 0.0

        for effect in zone.effects:

            if PriceCalculator._effect_applies(product, effect):
                total_modifier += effect.modifier

        return total_modifier

    @staticmethod
    def _effect_applies(product: Product, effect) -> bool:

        # Effetto globale → vale per tutti
        if effect.effect_type == ZoneEffectType.GLOBAL_PRICE_MODIFIER:
            return True

        # Effetto per categoria
        if effect.effect_type == ZoneEffectType.CATEGORY_PRICE_MODIFIER:
            if effect.target is None:
                return False

            return product.category in effect.target

        # Effetto per oggetti magici
        if effect.effect_type == ZoneEffectType.MAGICAL_LEVEL_MODIFIER:
            return product.is_magical

        return False