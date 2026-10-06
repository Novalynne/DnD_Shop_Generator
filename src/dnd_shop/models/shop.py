from dataclasses import dataclass, field
from typing import Optional
from zones import Zone
from product import Product

@dataclass
class Shop:
    """
    Rappresenta un negozio.

    Un negozio ha un nome, una descrizione, una lista di prodotti e una zona geografica.
    """

    name: str
    description: str = ""
    products: list[Product] = field(default_factory=list)
    zone: Optional[Zone] = None