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

# ---------------------------------------------------------------------------
# RARITÀ
# ---------------------------------------------------------------------------

comune = Rarity("Comune", 1)
rara = Rarity("Rara", 2)
epica = Rarity("Epica", 3)
leggendaria = Rarity("Leggendaria", 4)

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
    id: str
    name: str
    category: Category
    base_price_mr: int
    description: str = ""
    is_magical: bool = False
    rarity: Rarity = field(default_factory=lambda: Rarity("Comune", 1))


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

anello = Category("Anello")
amuleto = Category("Amuleto")
collana = Category("Collana")
orecchini = Category("Orecchini")
occhiali = Category("Occhiali")
tiara = Category("Tiara")

gioielli.add_subcategory(anello)
gioielli.add_subcategory(amuleto)
gioielli.add_subcategory(collana)
gioielli.add_subcategory(orecchini)
gioielli.add_subcategory(occhiali)
gioielli.add_subcategory(tiara)


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - ARMI
# ---------------------------------------------------------------------------

arco_leggero = Category("Arco leggero")
arco_pesante = Category("Arco pesante")
balestra_leggera = Category("Balestra leggera")
balestra_pesante = Category("Balestra pesante")
daga = Category("Daga")
spada_corta = Category("Spada corta")
spada_lunga = Category("Spada lunga")
spadone = Category("Spadone")
stocco = Category("Stocco")
scimitarra = Category("Scimitarra")
ascia = Category("Ascia")
ascetta = Category("Ascetta")
ascia_bipenne = Category("Ascia bipenne")
mazza = Category("Mazza")
martello_da_guerra = Category("Martello da guerra")
martello_pesante = Category("Martello pesante")
lancia = Category("Lancia")
giavellotto = Category("Giavellotto")
alabarda = Category("Alabarda")
picca = Category("Picca")
falce = Category("Falce")
randello = Category("Randello")
bastone = Category("Bastone")
fionda = Category("Fionda")

armi.add_subcategory(arco_leggero)
armi.add_subcategory(arco_pesante)
armi.add_subcategory(balestra_leggera)
armi.add_subcategory(balestra_pesante)
armi.add_subcategory(daga)
armi.add_subcategory(spada_corta)
armi.add_subcategory(spada_lunga)
armi.add_subcategory(spadone)
armi.add_subcategory(stocco)
armi.add_subcategory(scimitarra)
armi.add_subcategory(ascia)
armi.add_subcategory(ascetta)
armi.add_subcategory(ascia_bipenne)
armi.add_subcategory(mazza)
armi.add_subcategory(martello_da_guerra)
armi.add_subcategory(martello_pesante)
armi.add_subcategory(lancia)
armi.add_subcategory(giavellotto)
armi.add_subcategory(alabarda)
armi.add_subcategory(picca)
armi.add_subcategory(falce)
armi.add_subcategory(randello)
armi.add_subcategory(bastone)
armi.add_subcategory(fionda)


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - ARMATURE
# ---------------------------------------------------------------------------

armatura_leggera = Category("Armatura leggera")
armatura_media = Category("Armatura media")
armatura_pesante = Category("Armatura pesante")
scudo = Category("Scudo")

armature.add_subcategory(armatura_leggera)
armature.add_subcategory(armatura_media)
armature.add_subcategory(armatura_pesante)
armature.add_subcategory(scudo)


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - OGGETTI MAGICI
# ---------------------------------------------------------------------------

bacchetta = Category("Bacchetta")
verga = Category("Verga")
pergamena = Category("Pergamena")
pozione = Category("Pozione")

oggetti_magici.add_subcategory(bacchetta)
oggetti_magici.add_subcategory(verga)
oggetti_magici.add_subcategory(pergamena)
oggetti_magici.add_subcategory(pozione)

# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - EQUIPAGGIAMENTO
# ---------------------------------------------------------------------------


borsa = Category("Borsa")
corda = Category("Corda")
torcia = Category("Torcia")
attrezzi = Category("Attrezzi")
kit = Category("Kit")
munizioni = Category("Munizioni")
strumento_musicale = Category("Strumento musicale")
oggetto_da_viaggio = Category("Oggetto da viaggio")

equipaggiamento.add_subcategory(borsa)
equipaggiamento.add_subcategory(corda)
equipaggiamento.add_subcategory(torcia)
equipaggiamento.add_subcategory(attrezzi)
equipaggiamento.add_subcategory(kit)
equipaggiamento.add_subcategory(munizioni)
equipaggiamento.add_subcategory(strumento_musicale)
equipaggiamento.add_subcategory(oggetto_da_viaggio)


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - VESTITI
# ---------------------------------------------------------------------------

mantello = Category("Mantello")
cappello = Category("Cappello")
abito = Category("Abito")
scarpe = Category("Scarpe")

vestiti.add_subcategory(mantello)
vestiti.add_subcategory(cappello)
vestiti.add_subcategory(abito)
vestiti.add_subcategory(scarpe)


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - CIBO
# ---------------------------------------------------------------------------

carne = Category("Carne")
pesce = Category("Pesce")
verdure = Category("Verdure")
frutta = Category("Frutta")
legumi = Category("Legumi")
farine = Category("Farine")

cibo.add_subcategory(carne)
cibo.add_subcategory(pesce)
cibo.add_subcategory(verdure)
cibo.add_subcategory(frutta)
cibo.add_subcategory(legumi)
cibo.add_subcategory(farine)


# ---------------------------------------------------------------------------
# SOTTOCATEGORIE - BEVANDE
# ---------------------------------------------------------------------------

alcolici = Category("Alcolici")
non_alcolici = Category("Non alcolici")
super_alcolici = Category("Super alcolici")

bevande.add_subcategory(alcolici)
bevande.add_subcategory(non_alcolici)
bevande.add_subcategory(super_alcolici)


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
