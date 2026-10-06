from product import (
    Product,
    comune,
    rara,
    epica,
    leggendaria,

    # Categorie / sottocategorie
    arco_leggero,
    arco_pesante,
    balestra_leggera,
    balestra_pesante,
    daga,
    spada_corta,
    spada_lunga,
    spadone,
    stocco,
    scimitarra,
    ascia,
    ascetta,
    ascia_bipenne,
    mazza,
    martello_da_guerra,
    martello_pesante,
    lancia,
    giavellotto,
    alabarda,
    picca,
    falce,
    randello,
    bastone,
    fionda,

    armatura_leggera,
    armatura_media,
    armatura_pesante,
    scudo,

    bacchetta,
    verga,
    pergamena,
    pozione,

    mantello,
    cappello,
    abito,
    scarpe,

    anello,
    amuleto,
    collana,
    orecchini,
    occhiali,
    tiara,

    borsa,
    corda,
    torcia,
    attrezzi,
    kit,
    munizioni,
    strumento_musicale,
    oggetto_da_viaggio,

    carne,
    pesce,
    verdure,
    frutta,
    legumi,
    farine,

    alcolici,
    non_alcolici,
    super_alcolici,
)


# ============================================================================
# ARMI
# ============================================================================

spada_lunga = Product(
    name="Spada lunga",
    category=spada_lunga,
    base_price_mr=1500,
    description="Una classica spada da guerra a una mano.",
    is_magical=False,
    rarity=comune,
)

spada_corta = Product(
    name="Spada corta",
    category=spada_corta,
    base_price_mr=1000,
    description="Una spada leggera e maneggevole.",
    is_magical=False,
    rarity=comune,
)

daga = Product(
    name="Daga",
    category=daga,
    base_price_mr=200,
    description="Una piccola lama facilmente occultabile.",
    is_magical=False,
    rarity=comune,
)

spadone = Product(
    name="Spadone",
    category=spadone,
    base_price_mr=5000,
    description="Una grande spada a due mani.",
    is_magical=False,
    rarity=comune,
)

stocco = Product(
    name="Stocco",
    category=stocco,
    base_price_mr=2500,
    description="Una lama sottile progettata per i colpi di punta.",
    is_magical=False,
    rarity=comune,
)

scimitarra = Product(
    name="Scimitarra",
    category=scimitarra,
    base_price_mr=2500,
    description="Una lama ricurva e leggera.",
    is_magical=False,
    rarity=comune,
)

ascia = Product(
    name="Ascia",
    category=ascia,
    base_price_mr=1000,
    description="Un'ascia da combattimento.",
    is_magical=False,
    rarity=comune,
)

ascetta = Product(
    name="Ascetta",
    category=ascetta,
    base_price_mr=500,
    description="Una piccola ascia adatta anche al lancio.",
    is_magical=False,
    rarity=comune,
)

ascia_bipenne = Product(
    name="Ascia bipenne",
    category=ascia_bipenne,
    base_price_mr=3000,
    description="Una pesante ascia da guerra a due mani.",
    is_magical=False,
    rarity=comune,
)

mazza = Product(
    name="Mazza",
    category=mazza,
    base_price_mr=500,
    description="Una semplice arma contundente.",
    is_magical=False,
    rarity=comune,
)

martello_da_guerra = Product(
    name="Martello da guerra",
    category=martello_da_guerra,
    base_price_mr=1500,
    description="Un pesante martello da combattimento.",
    is_magical=False,
    rarity=comune,
)

martello_pesante = Product(
    name="Martello pesante",
    category=martello_pesante,
    base_price_mr=1000,
    description="Un enorme martello progettato per essere impugnato a due mani.",
    is_magical=False,
    rarity=comune,
)

lancia = Product(
    name="Lancia",
    category=lancia,
    base_price_mr=1000,
    description="Un'arma semplice e versatile.",
    is_magical=False,
    rarity=comune,
)

giavellotto = Product(
    name="Giavellotto",
    category=giavellotto,
    base_price_mr=50,
    description="Una lancia leggera progettata per essere lanciata.",
    is_magical=False,
    rarity=comune,
)

alabarda = Product(
    name="Alabarda",
    category=alabarda,
    base_price_mr=2000,
    description="Una lunga arma ad asta dotata di lama.",
    is_magical=False,
    rarity=comune,
)

picca = Product(
    name="Picca",
    category=picca,
    base_price_mr=500,
    description="Una lunga arma ad asta con punta metallica.",
    is_magical=False,
    rarity=comune,
)

falce = Product(
    name="Falce",
    category=falce,
    base_price_mr=100,
    description="Un attrezzo agricolo utilizzabile come arma.",
    is_magical=False,
    rarity=comune,
)

randello = Product(
    name="Randello",
    category=randello,
    base_price_mr=10,
    description="Un semplice randello di legno.",
    is_magical=False,
    rarity=comune,
)

bastone = Product(
    name="Bastone",
    category=bastone,
    base_price_mr=20,
    description="Un semplice bastone da combattimento.",
    is_magical=False,
    rarity=comune,
)

fionda = Product(
    name="Fionda",
    category=fionda,
    base_price_mr=100,
    description="Una semplice fionda.",
    is_magical=False,
    rarity=comune,
)

arco_leggero = Product(
    name="Arco leggero",
    category=arco_leggero,
    base_price_mr=2500,
    description="Un arco semplice e versatile.",
    is_magical=False,
    rarity=comune,
)

arco_pesante = Product(
    name="Arco pesante",
    category=arco_pesante,
    base_price_mr=5000,
    description="Un arco robusto dalla grande gittata.",
    is_magical=False,
    rarity=comune,
)

balestra_leggera = Product(
    name="Balestra leggera",
    category=balestra_leggera,
    base_price_mr=2500,
    description="Una balestra compatta.",
    is_magical=False,
    rarity=comune,
)

balestra_pesante = Product(
    name="Balestra pesante",
    category=balestra_pesante,
    base_price_mr=5000,
    description="Una potente balestra da guerra.",
    is_magical=False,
    rarity=comune,
)


# ============================================================================
# ARMATURE
# ============================================================================

armatura_cuoio = Product(
    name="Armatura di cuoio",
    category=armatura_leggera,
    base_price_mr=1000,
    description="Una semplice armatura composta da cuoio lavorato.",
    is_magical=False,
    rarity=comune,
)

armatura_cuoio_borchie = Product(
    name="Armatura di cuoio borchiato",
    category=armatura_leggera,
    base_price_mr=4500,
    description="Un'armatura di cuoio rinforzata con borchie metalliche.",
    is_magical=False,
    rarity=comune,
)

corazza = Product(
    name="Corazza",
    category=armatura_media,
    base_price_mr=4000,
    description="Una protezione robusta per il torso.",
    is_magical=False,
    rarity=comune,
)

cotta_di_maglia = Product(
    name="Cotta di maglia",
    category=armatura_media,
    base_price_mr=7500,
    description="Un'armatura composta da numerosi anelli metallici.",
    is_magical=False,
    rarity=comune,
)

corazza_di_piastre = Product(
    name="Corazza di piastre",
    category=armatura_media,
    base_price_mr=5000,
    description="Una corazza rinforzata con piastre metalliche.",
    is_magical=False,
    rarity=comune,
)

armatura_a_piastre = Product(
    name="Armatura a piastre",
    category=armatura_pesante,
    base_price_mr=15000,
    description="Una pesante armatura composta da numerose piastre metalliche.",
    is_magical=False,
    rarity=comune,
)

scudo = Product(
    name="Scudo",
    category=scudo,
    base_price_mr=1000,
    description="Uno scudo da combattimento.",
    is_magical=False,
    rarity=comune,
)

# ============================================================================
# OGGETTI MAGICI
# ============================================================================

pozione_guarigione = Product(
    name="Pozione di guarigione",
    category=pozione, 
    base_price_mr=5000,
    description="Una pozione che ripristina la salute.",
    is_magical=True,
    rarity=comune,
)

pozione_guarigione_maggiore= Product(
    name="Pozione di guarigione maggiore",
    category=pozione,
    base_price_mr=10000,
    description="Una pozione che ripristina una grande quantità di salute.",
    is_magical=True,
    rarity=rara,
)

pozione_forza = Product(
    name="Pozione della forza",
    category=pozione,
    base_price_mr=10000,
    description="Una pozione che aumenta temporaneamente la forza.",
    is_magical=True,
    rarity=rara,
)

pozione_invisibilita = Product(
    name="Pozione di invisibilità",
    category=pozione,
    base_price_mr=20000,
    description="Una pozione che rende chi la beve invisibile per un breve periodo.",
    is_magical=True,
    rarity=rara,
)

pozione_velocita = Product(
    name="Pozione della velocità",
    category=pozione,
    base_price_mr=15000,
    description="Una pozione che aumenta temporaneamente la velocità.",
    is_magical=True,
    rarity=rara,
)

bacchetta_magica = Product(
    name="Bacchetta magica",
    category=bacchetta,
    base_price_mr=25000,
    description="Una bacchetta che permette di lanciare incantesimi.",
    is_magical=True,
    rarity=epica,
)

amuleto_protezione = Product(
    name="Amuleto della protezione",
    category=amuleto,
    base_price_mr=30000,
    description="Un amuleto che offre protezione magica.",
    is_magical=True,
    rarity=epica,
)

# ============================================================================
# EQUIPAGGIAMENTO
# ============================================================================

borsa = Product(
    name="Borsa",
    category=borsa,
    base_price_mr=20,
    description="Una semplice borsa.",
    rarity=comune,
)

corda = Product(
    name="Corda di canapa (15 m)",
    category=corda,
    base_price_mr=100,
    description="Una robusta corda di canapa.",
    rarity=comune,
)

torcia = Product(
    name="Torcia",
    category=torcia,
    base_price_mr=10,
    description="Una torcia comune.",
    rarity=comune,
)

kit_avventuriero = Product(
    name="Kit dell'avventuriero",
    category=kit, 
    base_price_mr=5000,
    description="Un kit completo per l'avventuriero, contenente vari strumenti utili.",
    rarity=comune,
)

cassetta_attrezzi = Product(
    name="Cassetta degli attrezzi",
    category=attrezzi,
    base_price_mr=2500,
    description="Una cassetta contenente strumenti comuni.",
    rarity=comune,
)

borraccia = Product(
    name="Borraccia",
    category=oggetto_da_viaggio,
    base_price_mr=20,
    description="Un contenitore per l'acqua.",
    rarity=comune,
)

custodia_pergamene = Product(
    name="Custodia per pergamene",
    category=oggetto_da_viaggio,
    base_price_mr=100,
    description="Un contenitore per proteggere pergamene.",
    rarity=comune,
)

sapone = Product(
    name="Sapone",
    category=oggetto_da_viaggio,
    base_price_mr=5,
    description="Un semplice sapone per l'igiene personale.",
    rarity=comune,
)

frecce = Product(
    name="Frecce (20)",
    category=munizioni,
    base_price_mr=100,
    description="Una faretra contenente venti frecce.",
    rarity=comune,
)

dardi = Product(
    name="Dardi da balestra (20)",
    category=munizioni,
    base_price_mr=100,
    description="Una confezione contenente venti dardi.",
    rarity=comune,
)


# ============================================================================
# VESTITI
# ============================================================================

mantello_viaggio = Product(
    name="Mantello da viaggio",
    category=mantello,
    base_price_mr=500,
    description="Un mantello resistente adatto ai viaggi.",
    rarity=comune,
)

mantello_elegante = Product(
    name="Mantello elegante",
    category=mantello,
    base_price_mr=2500,
    description="Un mantello raffinato.",
    rarity=comune,
)

cappello = Product(
    name="Cappello",
    category=cappello,
    base_price_mr=100,
    description="Un semplice cappello.",
    rarity=comune,
)

abito_comune = Product(
    name="Abito comune",
    category=abito,
    base_price_mr=500,
    description="Abiti semplici per la vita quotidiana.",
    rarity=comune,
)

abito_elegante = Product(
    name="Abito elegante",
    category=abito,
    base_price_mr=1500,
    description="Un abito di buona fattura.",
    rarity=comune,
)

scarpe = Product(
    name="Scarpe da viaggio",
    category=scarpe,
    base_price_mr=300,
    description="Scarpe resistenti per lunghi viaggi.",
    rarity=comune,
)


# ============================================================================
# GIOIELLI
# ============================================================================

anello_argento = Product(
    name="Anello d'argento",
    category=anello,
    base_price_mr=5000,
    description="Un semplice anello d'argento.",
    rarity=comune,
)

anello_oro = Product(
    name="Anello d'oro",
    category=anello,
    base_price_mr=10000,
    description="Un anello d'oro finemente lavorato.",
    rarity=comune,
)

amuleto_argento = Product(
    name="Amuleto d'argento",
    category=amuleto,
    base_price_mr=5000,
    description="Un piccolo amuleto decorativo.",
    rarity=comune,
)

collana_oro = Product(
    name="Collana d'oro",
    category=collana,
    base_price_mr=25000,
    description="Una raffinata collana d'oro.",
    rarity=comune,
)

orecchini_argento = Product(
    name="Orecchini d'argento",
    category=orecchini,
    base_price_mr=5000,
    description="Un paio di orecchini d'argento.",
    rarity=comune,
)

tiara_decorativa = Product(
    name="Tiara decorativa",
    category=tiara,
    base_price_mr=50000,
    description="Una tiara ornamentale.",
    rarity=comune,
)


# ============================================================================
# CIBO
# ============================================================================

carne_fresca = Product(
    name="Carne fresca",
    category=carne,
    base_price_mr=30,
    description="Carne fresca proveniente dagli allevamenti locali.",
    rarity=comune,
)

carne_secca = Product(
    name="Carne secca",
    category=carne,
    base_price_mr=50,
    description="Carne conservata mediante essiccazione.",
    rarity=comune,
)

pesce_fresco = Product(
    name="Pesce fresco",
    category=pesce,
    base_price_mr=30,
    description="Pesce appena pescato.",
    rarity=comune,
)

pesce_affumicato = Product(
    name="Pesce affumicato",
    category=pesce,
    base_price_mr=50,
    description="Pesce conservato tramite affumicatura.",
    rarity=comune,
)

verdure = Product(
    name="Verdure miste",
    category=verdure,
    base_price_mr=20,
    description="Una selezione di verdure fresche.",
    rarity=comune,
)

frutta = Product(
    name="Frutta fresca",
    category=frutta,
    base_price_mr=20,
    description="Frutta fresca di stagione.",
    rarity=comune,
)

legumi = Product(
    name="Legumi secchi",
    category=legumi,
    base_price_mr=20,
    description="Legumi conservati.",
    rarity=comune,
)

farina = Product(
    name="Farina",
    category=farine,
    base_price_mr=10,
    description="Farina di grano macinato.",
    rarity=comune,
)


# ============================================================================
# BEVANDE
# ============================================================================

acqua = Product(
    name="Acqua",
    category=non_alcolici,
    base_price_mr=5,
    description="Acqua potabile.",
    rarity=comune,
)

latte = Product(
    name="Latte",
    category=non_alcolici,
    base_price_mr=10,
    description="Latte fresco.",
    rarity=comune,
)

succo_frutta = Product(
    name="Succo di frutta",
    category=non_alcolici,
    base_price_mr=20,
    description="Succo di frutta fresca.",
    rarity=comune,
)

birra = Product(
    name="Birra",
    category=alcolici,
    base_price_mr=40,
    description="Una birra comune prodotta localmente.",
    rarity=comune,
)

vino = Product(
    name="Vino",
    category=alcolici,
    base_price_mr=100,
    description="Vino da tavola.",
    rarity=comune,
)

vino_pregiato = Product(
    name="Vino pregiato",
    category=alcolici,
    base_price_mr=1000,
    description="Vino di alta qualità.",
    rarity=rara,
)

liquore = Product(
    name="Liquore",
    category=super_alcolici,
    base_price_mr=200,
    description="Un liquore distillato.",
    rarity=comune,
)

distillato_pregiato = Product(
    name="Distillato pregiato",
    category=super_alcolici,
    base_price_mr=1500,
    description="Un distillato di alta qualità.",
    rarity=rara,
)


# ============================================================================
# CATALOGO COMPLETO
# ============================================================================

PRODUCTS = [
    # Armi
    spada_lunga,
    spada_corta,
    daga,
    spadone,
    stocco,
    scimitarra,
    ascia,
    ascetta,
    ascia_bipenne,
    mazza,
    martello_da_guerra,
    martello_pesante,
    lancia,
    giavellotto,
    alabarda,
    picca,
    falce,
    randello,
    bastone,
    fionda,
    arco_leggero,
    arco_pesante,
    balestra_leggera,
    balestra_pesante,

    # Armature
    armatura_cuoio,
    armatura_cuoio_borchie,
    corazza,
    cotta_di_maglia,
    corazza_di_piastre,
    armatura_a_piastre,
    scudo,

    # Equipaggiamento
    borsa,
    corda,
    torcia,
    cassetta_attrezzi,
    borraccia,
    custodia_pergamene,
    frecce,
    dardi,

    # Vestiti
    mantello_viaggio,
    mantello_elegante,
    cappello,
    abito_comune,
    abito_elegante,
    scarpe,

    # Gioielli
    anello_argento,
    anello_oro,
    amuleto_argento,
    collana_oro,
    orecchini_argento,
    tiara_decorativa,

    # Cibo
    carne_fresca,
    carne_secca,
    pesce_fresco,
    pesce_affumicato,
    verdure,
    frutta,
    legumi,
    farina,

    # Bevande
    acqua,
    latte,
    succo_frutta,
    birra,
    vino,
    vino_pregiato,
    liquore,
    distillato_pregiato,
]
