from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Rarity:
    """
    Rappresenta la rarità di un prodotto.

    Esempi:
        Rarity("Comune", 1)
        Rarity("Rara", 2)
        Rarity("Epica", 3)
        Rarity("Leggendaria", 4)
    """

    name: str
    multiplier: int

@dataclass
class Category:
    """
    Rappresenta una categoria o sottocategoria di prodotto.

    Esempi:
        Category("Armi")
        Category("Spada lunga", parent="Armi")
    """

    name: str
    parent: Optional["Category"] = None
    subcategories: list["Category"] = field(default_factory=list)

    def add_subcategory(self, category: "Category") -> None:
        """Aggiunge una sottocategoria a questa categoria."""
        category.parent = self
        self.subcategories.append(category)


@dataclass
class Product:
    """
    Rappresenta un prodotto acquistabile nel gioco.

    La rarità e la proprietà magica sono volutamente separate
    dalla categoria: in questo modo, ad esempio, una Spada lunga
    può essere Comune, Rara, Magica, ecc.
    """

    name: str
    category: Category
    base_price_mr: int
    description: str = ""
    is_magical: bool = False
    rarity: Rarity


# ---------------------------------------------------------------------------
# CATEGORIE
# ---------------------------------------------------------------------------

gioielli = Category("Gioielli")
armi = Category("Armi")
armature = Category("Armature")
oggetti_magici = Category("Oggetti magici")
vestiti = Category("Vestiti")
equipaggiamento = Category("Equipaggiamento")
cibo = Category("Cibo")
bevande = Category("Bevande")


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - GIOIELLI
# ---------------------------------------------------------------------------

gioielli.add_subcategory(Category("Anello"))
gioielli.add_subcategory(Category("Amuleto"))
gioielli.add_subcategory(Category("Collana"))
gioielli.add_subcategory(Category("Orecchini"))
gioielli.add_subcategory(Category("Occhiali"))
gioielli.add_subcategory(Category("Tiare"))


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - ARMI
# ---------------------------------------------------------------------------

armi.add_subcategory(Category("Arco leggero"))
armi.add_subcategory(Category("Arco pesante"))
armi.add_subcategory(Category("Balestra leggera"))
armi.add_subcategory(Category("Balestra pesante"))
armi.add_subcategory(Category("Daga"))
armi.add_subcategory(Category("Spada corta"))
armi.add_subcategory(Category("Spada lunga"))
armi.add_subcategory(Category("Spadone"))
armi.add_subcategory(Category("Stocco"))
armi.add_subcategory(Category("Scimitarra"))
armi.add_subcategory(Category("Ascia"))
armi.add_subcategory(Category("Ascetta"))
armi.add_subcategory(Category("Ascia bipenne"))
armi.add_subcategory(Category("Mazza"))
armi.add_subcategory(Category("Martello da guerra"))
armi.add_subcategory(Category("Martello pesante"))
armi.add_subcategory(Category("Lancia"))
armi.add_subcategory(Category("Giavellotto"))
armi.add_subcategory(Category("Alabarda"))
armi.add_subcategory(Category("Picca"))
armi.add_subcategory(Category("Falce"))
armi.add_subcategory(Category("Randello"))
armi.add_subcategory(Category("Bastone"))
armi.add_subcategory(Category("Fionda"))


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - ARMATURE
# ---------------------------------------------------------------------------

armature.add_subcategory(Category("Armatura leggera"))
armature.add_subcategory(Category("Armatura media"))
armature.add_subcategory(Category("Armatura pesante"))
armature.add_subcategory(Category("Scudo"))


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - OGGETTI MAGICI
# ---------------------------------------------------------------------------

oggetti_magici.add_subcategory(Category("Bacchetta"))
oggetti_magici.add_subcategory(Category("Verga"))
oggetti_magici.add_subcategory(Category("Pergamena"))
oggetti_magici.add_subcategory(Category("Pozione"))


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - VESTITI
# ---------------------------------------------------------------------------

vestiti.add_subcategory(Category("Mantello"))
vestiti.add_subcategory(Category("Cappello"))
vestiti.add_subcategory(Category("Abito"))
vestiti.add_subcategory(Category("Scarpe"))


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - CIBO
# ---------------------------------------------------------------------------

cibo.add_subcategory(Category("Carne"))
cibo.add_subcategory(Category("Pesce"))
cibo.add_subcategory(Category("Verdure"))
cibo.add_subcategory(Category("Frutta"))
cibo.add_subcategory(Category("Legumi"))
cibo.add_subcategory(Category("Farine"))


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - BEVANDE
# ---------------------------------------------------------------------------

bevande.add_subcategory(Category("Alcolici"))
bevande.add_subcategory(Category("Non alcolici"))
bevande.add_subcategory(Category("Super alcolici"))

# ---------------------------------------------------------------------------
# RARITÀ
# ---------------------------------------------------------------------------

comune = Rarity("Comune", 1)
rara = Rarity("Rara", 2)
epica = Rarity("Epica", 3)
leggendaria = Rarity("Leggendaria", 4)


# ---------------------------------------------------------------------------
# LISTE DI CATEGORIE E RARITÀ
# ---------------------------------------------------------------------------

CATEGORIES = [
    gioielli,
    armi,
    armature,
    oggetti_magici,
    vestiti,
    equipaggiamento,
    cibo,
    bevande,
]

RARITIES = [
    comune,
    rara,
    epica,
    leggendaria,
]
