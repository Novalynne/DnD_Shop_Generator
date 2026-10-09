from dnd_shop.generator.shop_generator import ShopGenerator
from dnd_shop.models.product import armi, armature
from dnd_shop.models.shop import ShopType

# Scegliamo le categorie e il tipo di negozio
categories = [armi, armature]

shop_type = ShopType.SMITH


# Generiamo un negozio con 5 prodotti
shop = ShopGenerator.generate_shop(
    shop_type=shop_type,
    allowed_categories=categories,
    num_products=5,
)

print("\nNEGOZIO GENERATO\n")
print(f"Nome: {shop.name}")
print(f"Tipo: {shop.type.name}")
print(f"Descrizione: {shop.description}")

print("\nPRODOTTI DEL NEGOZIO\n")

for product in shop.products:
    print(f"Nome: {product.name}")
    print(f"Categoria: {product.category.name}")
    print(f"Descrizione: {product.description}")
    print(f"Prezzo: {product.base_price_mr} MR")
    print(f"Magico: {product.is_magical}")
    print(f"Rarità: {product.rarity.name}")
    print("-" * 40)