from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from product import Category, Rarity 


class ZoneEffectType(Enum):
    """
    Tipi di effetti economici che una zona può applicare.

    Il calcolo effettivo dei prezzi verrà gestito in seguito
    dal price_calculator.py.

    Esempi:
        ZoneEffectType.GLOBAL_PRICE_MODIFIER      -> Modifica il prezzo di tutti i prodotti di una zona.
        ZoneEffectType.CATEGORY_PRICE_MODIFIER    -> Modifica il prezzo dei prodotti di una categoria specifica in una zona.
        ZoneEffectType.MAGICAL_LEVEL_MODIFIER     -> Modifica il prezzo dei prodotti magici in base al livello di sviluppo della zona. 
                                                     Zona ad alto sviluppo magico -> +20% su prodotti magici di rarità Epica e Leggendaria.
    """

    GLOBAL_PRICE_MODIFIER = "global_price_modifier"
    CATEGORY_PRICE_MODIFIER = "category_price_modifier"
    MAGICAL_LEVEL_MODIFIER = "magical_level_modifier"


@dataclass
class ZoneEffect:
    """
    Rappresenta un singolo effetto applicato da una zona.

    modifier:
        Percentuale espressa come numero decimale.

        Esempi:
            +20% -> 0.20
            -50% -> -0.50
            +30% -> 0.30

    target:
        Indica a cosa si applica l'effetto.

        Esempi:
            "all"       -> tutti i prodotti
            "pesce"     -> categoria Pesce
            "carne"     -> categoria Carne
            "frutta"    -> categoria Frutta
            "verdure"   -> categoria Verdure
    """

    effect_type: ZoneEffectType
    modifier: float = 0.0
    target: Optional[Category] = None || Optional[Rarity] = None || str = "all"
    description: str = ""


@dataclass
class Zone:
    """
    Rappresenta una zona geografica del mondo di gioco.

    Una zona può avere più effetti contemporaneamente.
    """

    name: str
    description: str = ""
    effects: list[ZoneEffect] = field(default_factory=list)

    def add_effect(self, effect: ZoneEffect) -> None:
        """Aggiunge un effetto economico alla zona."""
        self.effects.append(effect)


# ---------------------------------------------------------------------------
# ZONE PRINCIPALI
# ---------------------------------------------------------------------------

zona_estremamente_ricca = Zone(
    name="Zona estremamente ricca",
    description="Zona con un elevato livello di ricchezza.",
)

zona_ricca = Zone(
    name="Zona ricca",
    description="Zona con un alto livello di ricchezza.",
)

zona_povera = Zone(
    name="Zona povera",
    description="Zona con un basso livello di ricchezza.",
)

zona_estremamente_povera = Zone(
    name="Zona estremamente povera",
    description="Zona con un livello di ricchezza molto basso.",
)

zona_turistica = Zone(
    name="Zona turistica",
    description="Zona frequentata da viaggiatori e turisti.",
)

zona_deserta = Zone(
    name="Zona deserta",
    description="Zona con poca disponibilità e poco commercio.",
)

zona_alto_commercio = Zone(
    name="Zona ad alto commercio",
    description="Zona caratterizzata da un elevato volume di commercio.",
)

zona_pesca = Zone(
    name="Zona di pesca",
    description="Zona in cui il pesce di maggiore rarità ha un valore più elevato.",
)

zona_montagna = Zone(
    name="Zona di montagna",
    description="Zona in cui la carne di maggiore qualità ha un valore più elevato.",
)

zona_pianura = Zone(
    name="Zona di pianura",
    description="Zona in cui frutta e verdura di maggiore qualità hanno un valore più elevato.",
)

zona_alta_istruzione = Zone(
    name="Zona ad alta istruzione",
    description="Zona in cui sono più facilmente reperibili oggetti magici di maggiore rarità.",
)

zona_bassa_istruzione = Zone(
    name="Zona a bassa istruzione",
    description="Zona in cui gli oggetti magici di maggiore rarità sono meno comuni.",
)

zona_inflazione = Zone(
    name="Zona con inflazione",
    description="Zona in cui l'inflazione aumenta il prezzo di tutti i prodotti.",
)

# ============================================================================
# PERCENTUALI BASE DELLE ZONE
# ============================================================================
#
# Questi valori sono volutamente definiti in un'unica sezione.
# In futuro potranno essere caricati/modificati tramite la GUI e salvati
# nel database senza dover modificare la logica del programma.
#
# Tutti i modifier sono decimali:
#   0.20  = +20%
#  -0.50  = -50%
#   0.35  = +35%
# ============================================================================

ZONE_MODIFIERS = {
    "zona_estremamente_ricca": 0.70,
    "zona_ricca": 0.50,
    "zona_povera": -0.30,
    "zona_estremamente_povera": -0.80,

    "zona_turistica": 0.35,
    "zona_deserta": -0.40,
    "zona_alto_commercio": -0.10,

    "zona_pesca": 0.20,
    "zona_montagna": 0.20,
    "zona_pianura": 0.20,

    "zona_alta_istruzione": 0.20,
    "zona_bassa_istruzione": -0.20,

    "zona_inflazione": 0.25,
}

# ============================================================================
# EFFETTI DELLE ZONE
# ============================================================================

# Ricchezza
zona_estremamente_ricca.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_estremamente_ricca"],
        target="all",
        description="Rincaro del 50% su tutti i prodotti.",
    )
)

zona_ricca.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_ricca"],
        target="all",
        description="Rincaro del 30% su tutti i prodotti.",
    )
)

zona_povera.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_povera"],
        target="all",
        description="Sconto del 30% su tutti i prodotti.",
    )
)

zona_estremamente_povera.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_estremamente_povera"],
        target="all",
        description="Sconto del 50% su tutti i prodotti.",
    )
)


# Turismo
zona_turistica.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_turistica"],
        target="all",
        description="Rincaro del 20% su tutti i prodotti.",
    )
)


# Zona deserta
zona_deserta.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_deserta"],
        target="all",
        description="Sconto del 20% dovuto alla scarsa domanda e alla difficoltà di commercio.",
    )
)


# Alto commercio
zona_alto_commercio.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_alto_commercio"],
        target="all",
        description="Riduzione del 10% grazie all'elevata disponibilità di merci.",
    )
)


# Pesca
zona_pesca.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.RARITY_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_pesca"],
        target="Pesce",
        description="Il pesce di maggiore rarità riceve un rincaro del 20%.",
    )
)


# Montagna
zona_montagna.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.QUALITY_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_montagna"],
        target="Carne",
        description="La carne di maggiore qualità riceve un rincaro del 20%.",
    )
)


# Pianura
zona_pianura.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.QUALITY_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_pianura"],
        target="Frutta",
        description="La frutta di maggiore qualità riceve un rincaro del 20%.",
    )
)

zona_pianura.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.QUALITY_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_pianura"],
        target="Verdure",
        description="Le verdure di maggiore qualità ricevono un rincaro del 20%.",
    )
)


# Istruzione
zona_alta_istruzione.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.MAGICAL_RARITY_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_alta_istruzione"],
        target="magical",
        description="Gli oggetti magici di maggiore rarità ricevono un rincaro del 20%.",
    )
)

zona_bassa_istruzione.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.MAGICAL_RARITY_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_bassa_istruzione"],
        target="magical",
        description="Gli oggetti magici di maggiore rarità ricevono uno sconto del 20%.",
    )
)


# Inflazione
zona_inflazione.add_effect(
    ZoneEffect(
        effect_type=ZoneEffectType.GLOBAL_PRICE_MODIFIER,
        modifier=ZONE_MODIFIERS["zona_inflazione"],
        target="all",
        description="Rincaro del 25% su tutti i prodotti indipendentemente dalla categoria.",
    )
)


# ---------------------------------------------------------------------------
# ELENCO DELLE ZONE
# ---------------------------------------------------------------------------

ZONES = [
    zona_estremamente_ricca,
    zona_ricca,
    zona_povera,
    zona_estremamente_povera,
    zona_turistica,
    zona_deserta,
    zona_alto_commercio,
    zona_pesca,
    zona_montagna,
    zona_pianura,
    zona_alta_istruzione,
    zona_bassa_istruzione,
    zona_inflazione,
]
