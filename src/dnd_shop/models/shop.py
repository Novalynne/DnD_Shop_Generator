from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from zones import Zone
from product import Product, Category


class ShopType(Enum):
    """
    Rappresenta il tipo di negozio.

    Esempi:
        ShopType("Fabbro")
        ShopType("Alchimista")
        ShopType("Emporio")
        ShopType("Taverna")
        ShopType("Generale")
    """

    SMITH = "Fabbro"
    ALCHEMIST = "Alchimista"
    EMPORIO = "Emporio"
    TAVERN = "Taverna"
    CLOTHING = "Negozio di vestiti"
    ACCESSORIES = "Negozio di accessori"
    MAGIC = "Negozio di oggetti magici"
    GENERAL = "Generale"

@dataclass
class Shop:
    """
    Rappresenta un negozio.

    Un negozio ha un nome, una descrizione, una lista di prodotti e una zona geografica.
    """

    type: ShopType
    name: str
    description: str = ""
    allowed_categories: list[Category]
    products: list[Product] = field(default_factory=list)
    zone: Optional[Zone] = None