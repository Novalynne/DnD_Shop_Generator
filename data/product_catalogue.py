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
    id="spada_lunga",
    name="Spada lunga",
    category=spada_lunga,
    base_price_mr=1500,
    description="Una classica spada da guerra a una mano.",
)

spada_corta = Product(
    id="spada_corta",
    name="Spada corta",
    category=spada_corta,
    base_price_mr=1000,
    description="Una spada leggera e maneggevole.",
)

daga = Product(
    id="daga",
    name="Daga",
    category=daga,
    base_price_mr=200,
    description="Una piccola lama facilmente occultabile.",
)

spadone = Product(
    id="spadone",
    name="Spadone",
    category=spadone,
    base_price_mr=5000,
    description="Una grande spada a due mani.",
)

stocco = Product(
    id="stocco",
    name="Stocco",
    category=stocco,
    base_price_mr=2500,
    description="Una lama sottile progettata per i colpi di punta.",
)

scimitarra = Product(
    id="scimitarra",
    name="Scimitarra",
    category=scimitarra,
    base_price_mr=2500,
    description="Una lama ricurva e leggera.",
)

ascia = Product(
    id="ascia",
    name="Ascia",
    category=ascia,
    base_price_mr=1000,
    description="Un'ascia da combattimento.",
)

ascetta = Product(
    id="ascetta",
    name="Ascetta",
    category=ascetta,
    base_price_mr=500,
    description="Una piccola ascia adatta anche al lancio.",
)

ascia_bipenne = Product(
    id="ascia_bipenne",
    name="Ascia bipenne",
    category=ascia_bipenne,
    base_price_mr=3000,
    description="Una pesante ascia da guerra a due mani.",
)

mazza = Product(
    id="mazza",
    name="Mazza",
    category=mazza,
    base_price_mr=500,
    description="Una semplice arma contundente.",
)

martello_da_guerra = Product(
    id="martello_da_guerra",
    name="Martello da guerra",
    category=martello_da_guerra,
    base_price_mr=1500,
    description="Un pesante martello da combattimento.",
)

martello_pesante = Product(
    id="martello_pesante",
    name="Martello pesante",
    category=martello_pesante,
    base_price_mr=1000,
    description="Un enorme martello progettato per essere impugnato a due mani.",
)

lancia = Product(
    id="lancia",
    name="Lancia",
    category=lancia,
    base_price_mr=1000,
    description="Un'arma semplice e versatile.",
)

giavellotto = Product(
    id="giavellotto",
    name="Giavellotto",
    category=giavellotto,
    base_price_mr=50,
    description="Una lancia leggera progettata per essere lanciata.",
)

alabarda = Product(
    id="alabarda",
    name="Alabarda",
    category=alabarda,
    base_price_mr=2000,
    description="Una lunga arma ad asta dotata di lama.",
)

picca = Product(
    id="picca",
    name="Picca",
    category=picca,
    base_price_mr=500,
    description="Una lunga arma ad asta con punta metallica.",
)

falce = Product(
    id="falce",
    name="Falce",
    category=falce,
    base_price_mr=100,
    description="Un attrezzo agricolo utilizzabile come arma.",
)

randello = Product(
    id="randello",
    name="Randello",
    category=randello,
    base_price_mr=10,
    description="Un semplice randello di legno.",
)

bastone = Product(
    id="bastone",
    name="Bastone",
    category=bastone,
    base_price_mr=20,
    description="Un semplice bastone da combattimento.",
)

fionda = Product(
    id="fionda",
    name="Fionda",
    category=fionda,
    base_price_mr=100,
    description="Una semplice fionda.",
)

arco_leggero = Product(
    id="arco_leggero",
    name="Arco leggero",
    category=arco_leggero,
    base_price_mr=2500,
    description="Un arco semplice e versatile.",
)

arco_pesante = Product(
    id="arco_pesante",
    name="Arco pesante",
    category=arco_pesante,
    base_price_mr=5000,
    description="Un arco robusto dalla grande gittata.",
)

balestra_leggera = Product(
    id="balestra_leggera",
    name="Balestra leggera",
    category=balestra_leggera,
    base_price_mr=2500,
    description="Una balestra compatta.",
)

balestra_pesante = Product(
    id="balestra_pesante",
    name="Balestra pesante",
    category=balestra_pesante,
    base_price_mr=5000,
    description="Una potente balestra da guerra.",
)


# ============================================================================
# ARMATURE
# ============================================================================

armatura_cuoio = Product(
    id="armatura_cuoio",
    name="Armatura di cuoio",
    category=armatura_leggera,
    base_price_mr=1000,
    description="Una semplice armatura composta da cuoio lavorato.",
)

armatura_cuoio_borchie = Product(
    id="armatura_cuoio_borchie",
    name="Armatura di cuoio borchiato",
    category=armatura_leggera,
    base_price_mr=4500,
    description="Un'armatura di cuoio rinforzata con borchie metalliche.",
)

corazza = Product(
    id="corazza",
    name="Corazza",
    category=armatura_media,
    base_price_mr=4000,
    description="Una protezione robusta per il torso.",
)

cotta_di_maglia = Product(
    id="cotta_di_maglia",
    name="Cotta di maglia",
    category=armatura_media,
    base_price_mr=7500,
    description="Un'armatura composta da numerosi anelli metallici.",
)

corazza_di_piastre = Product(
    id="corazza_di_piastre",
    name="Corazza di piastre",
    category=armatura_media,
    base_price_mr=5000,
    description="Una corazza rinforzata con piastre metalliche.",
)

armatura_a_piastre = Product(
    id="armatura_a_piastre",
    name="Armatura a piastre",
    category=armatura_pesante,
    base_price_mr=15000,
    description="Una pesante armatura composta da numerose piastre metalliche.",
)

scudo = Product(
    id="scudo",
    name="Scudo",
    category=scudo,
    base_price_mr=1000,
    description="Uno scudo da combattimento.",
)

# ============================================================================
# OGGETTI MAGICI
# ============================================================================

pozione_guarigione = Product(
    id="pozione_guarigione",
    name="Pozione di guarigione",
    category=pozione, 
    base_price_mr=5000,
    description="Una pozione che ripristina la salute.",
)

pozione_guarigione_maggiore= Product(
    id="pozione_guarigione_maggiore",
    name="Pozione di guarigione maggiore",
    category=pozione,
    base_price_mr=10000,
    description="Una pozione che ripristina una grande quantità di salute.",
)

pozione_forza = Product(
    id="pozione_forza",
    name="Pozione della forza",
    category=pozione,
    base_price_mr=10000,
    description="Una pozione che aumenta temporaneamente la forza.",
)

pozione_invisibilita = Product(
    id="pozione_invisibilita",
    name="Pozione di invisibilità",
    category=pozione,
    base_price_mr=20000,
    description="Una pozione che rende chi la beve invisibile per un breve periodo.",
)

pozione_velocita = Product(
    id="pozione_velocita",
    name="Pozione della velocità",
    category=pozione,
    base_price_mr=15000,
    description="Una pozione che aumenta temporaneamente la velocità.",
)

bacchetta_magica = Product(
    id="bacchetta_magica",
    name="Bacchetta magica",
    category=bacchetta,
    base_price_mr=25000,
    description="Una bacchetta che permette di lanciare incantesimi.",
)

amuleto_protezione = Product(
    id="amuleto_protezione",
    name="Amuleto della protezione",
    category=amuleto,
    base_price_mr=30000,
    description="Un amuleto che offre protezione magica.",
)

pergamena_incantesimo = Product(
    id="pergamena_incantesimo",
    name="Pergamena di incantesimo",
    category=pergamena,
    base_price_mr=20000,
    description="Una pergamena che contiene un incantesimo pronto all'uso.",
)

# ============================================================================
# EQUIPAGGIAMENTO
# ============================================================================

borsa = Product(
    id="borsa",
    name="Borsa",
    category=borsa,
    base_price_mr=20,
    description="Una semplice borsa.",
)

corda = Product(
    id="corda",
    name="Corda di canapa (15 m)",
    category=corda,
    base_price_mr=100,
    description="Una robusta corda di canapa.",
)

torcia = Product(
    id="torcia",
    name="Torcia",
    category=torcia,
    base_price_mr=10,
    description="Una torcia comune.",
)

kit_avventuriero = Product(
    id="kit_avventuriero",
    name="Kit dell'avventuriero",
    category=kit, 
    base_price_mr=5000,
    description="Un kit completo per l'avventuriero, contenente vari strumenti utili.",
)

cassetta_attrezzi = Product(
    id="cassetta_attrezzi",
    name="Cassetta degli attrezzi",
    category=attrezzi,
    base_price_mr=2500,
    description="Una cassetta contenente strumenti comuni.",
)

borraccia = Product(
    id="borraccia",
    name="Borraccia",
    category=oggetto_da_viaggio,
    base_price_mr=20,
    description="Un contenitore per l'acqua.",
)

custodia_pergamene = Product(
    id="custodia_pergamene",
    name="Custodia per pergamene",
    category=oggetto_da_viaggio,
    base_price_mr=100,
    description="Un contenitore per proteggere pergamene.",
)

sapone = Product(
    id="sapone",
    name="Sapone",
    category=oggetto_da_viaggio,
    base_price_mr=5,
    description="Un semplice sapone per l'igiene personale.",
)

frecce = Product(
    id="frecce",
    name="Frecce (20)",
    category=munizioni,
    base_price_mr=100,
    description="Una faretra contenente venti frecce.",
)

dardi = Product(
    id="dardi",
    name="Dardi da balestra (20)",
    category=munizioni,
    base_price_mr=100,
    description="Una confezione contenente venti dardi.",
)


# ============================================================================
# VESTITI
# ============================================================================

mantello_viaggio = Product(
    id="mantello_viaggio",
    name="Mantello da viaggio",
    category=mantello,
    base_price_mr=500,
    description="Un mantello resistente adatto ai viaggi.",
)

mantello_elegante = Product(
    id="mantello_elegante",
    name="Mantello elegante",
    category=mantello,
    base_price_mr=2500,
    description="Un mantello raffinato.",
)

cappello = Product(
    id="cappello",
    name="Cappello",
    category=cappello,
    base_price_mr=100,
    description="Un semplice cappello.",
)

abito_comune = Product(
    id="abito_comune",
    name="Abito comune",
    category=abito,
    base_price_mr=500,
    description="Abiti semplici per la vita quotidiana.",
)

abito_elegante = Product(
    id="abito_elegante",
    name="Abito elegante",
    category=abito,
    base_price_mr=1500,
    description="Un abito di buona fattura.",
)

scarpe = Product(
    id="scarpe",
    name="Scarpe da viaggio",
    category=scarpe,
    base_price_mr=300,
    description="Scarpe resistenti per lunghi viaggi.",
)


gonna = Product(
    id="gonna",
    name="Gonna",
    category=abito,
    base_price_mr=300,
    description="Una gonna semplice adatta all'uso quotidiano.",
)

vestito_da_sera = Product(
    id="vestito_da_sera",
    name="Vestito da sera",
    category=abito,
    base_price_mr=2500,
    description="Un elegante vestito destinato a occasioni formali.",
)


# ============================================================================
# GIOIELLI
# ============================================================================

anello_argento = Product(
    id="anello_argento",
    name="Anello d'argento",
    category=anello,
    base_price_mr=5000,
    description="Un semplice anello d'argento.",
)

anello_oro = Product(
    id="anello_oro",
    name="Anello d'oro",
    category=anello,
    base_price_mr=10000,
    description="Un anello d'oro finemente lavorato.",
)

amuleto_argento = Product(
    id="amuleto_argento",
    name="Amuleto d'argento",
    category=amuleto,
    base_price_mr=5000,
    description="Un piccolo amuleto decorativo.",
)

collana_oro = Product(
    id="collana_oro",
    name="Collana d'oro",
    category=collana,
    base_price_mr=25000,
    description="Una raffinata collana d'oro.",
)

orecchini_argento = Product(
    id="orecchini_argento",
    name="Orecchini d'argento",
    category=orecchini,
    base_price_mr=5000,
    description="Un paio di orecchini d'argento.",
)

tiara_decorativa = Product(
    id="tiara_decorativa",
    name="Tiara decorativa",
    category=tiara,
    base_price_mr=50000,
    description="Una tiara ornamentale.",
)


# ============================================================================
# CIBO
# ============================================================================

carne_fresca = Product(
    id="carne_fresca",
    name="Carne fresca",
    category=carne,
    base_price_mr=30,
    description="Carne fresca proveniente dagli allevamenti locali.",
)

carne_secca = Product(
    id="carne_secca",
    name="Carne secca",
    category=carne,
    base_price_mr=50,
    description="Carne conservata mediante essiccazione.",
)

pesce_fresco = Product(
    id="pesce_fresco",
    name="Pesce fresco",
    category=pesce,
    base_price_mr=30,
    description="Pesce appena pescato.",
)

pesce_affumicato = Product(
    id="pesce_affumicato",
    name="Pesce affumicato",
    category=pesce,
    base_price_mr=50,
    description="Pesce conservato tramite affumicatura.",
)

verdure = Product(
    id="verdure",
    name="Verdure miste",
    category=verdure,
    base_price_mr=20,
    description="Una selezione di verdure fresche.",
)

frutta = Product(
    id="frutta",
    name="Frutta fresca",
    category=frutta,
    base_price_mr=20,
    description="Frutta fresca di stagione.",
)

legumi = Product(
    id="legumi",
    name="Legumi secchi",
    category=legumi,
    base_price_mr=20,
    description="Legumi conservati.",
)

farina = Product(
    id="farina",
    name="Farina",
    category=farine,
    base_price_mr=10,
    description="Farina di grano macinato.",
)


# ============================================================================
# BEVANDE
# ============================================================================

acqua = Product(
    id="acqua",
    name="Acqua",
    category=non_alcolici,
    base_price_mr=5,
    description="Acqua potabile.",
)

latte = Product(
    id="latte",
    name="Latte",
    category=non_alcolici,
    base_price_mr=10,
    description="Latte fresco.",
)

succo_frutta = Product(
    id="succo_frutta",
    name="Succo di frutta",
    category=non_alcolici,
    base_price_mr=20,
    description="Succo di frutta fresca.",
)

birra = Product(
    id="birra",
    name="Birra",
    category=alcolici,
    base_price_mr=40,
    description="Una birra comune prodotta localmente.",
)

vino = Product(
    id="vino",
    name="Vino",
    category=alcolici,
    base_price_mr=100,
    description="Vino da tavola.",
)

vino_pregiato = Product(
    id="vino_pregiato",
    name="Vino pregiato",
    category=alcolici,
    base_price_mr=1000,
    description="Vino di alta qualità.",
)

liquore = Product(
    id="liquore",
    name="Liquore",
    category=super_alcolici,
    base_price_mr=200,
    description="Un liquore distillato.",
)

distillato_pregiato = Product(
    id="distillato_pregiato",
    name="Distillato pregiato",
    category=super_alcolici,
    base_price_mr=1500,
    description="Un distillato di alta qualità.",
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
    gonna,
    vestito_da_sera,
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