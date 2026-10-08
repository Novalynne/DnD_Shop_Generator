from dnd_shop.generator.ai_generator import AIGenerator
from dnd_shop.data.product_catalogue import spada_lunga

ai = AIGenerator()

# Prova a generare un oggetto
name, description = ai.generate_product(
    base_product=spada_lunga,
    is_magical=True,
    rarity="Rara",
)

print("Nome:", spada_lunga.name)
print("Categoria:", spada_lunga.category.name)
print("Descrizione:", repr(spada_lunga.description))

print("\nOGGETTO GENERATO\n")
print(f"Nome: {name}")
print(f"Descrizione: {description}")


# Prova a generare un negozio
shop_name, shop_description = ai.generate_shop(
    shop_type="Armeria nanica",
    allowed_categories=["Armi", "Scudi", "Armature"],
)

print("\nNEGOZIO")
print(f"Nome: {shop_name}")
print(f"Descrizione: {shop_description}")