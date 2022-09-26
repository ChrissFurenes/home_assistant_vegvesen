from datetime import timedelta
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from ..vesvesen import DATA_VEGVESEN

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=60)

def setup_platform(hass, config, add_entities, discovery_info=None):
    kjortetoyopplysninger = hass.data[DATA_VEGVESEN]

    add_entities(
        KjortetoyopplysningerSensor(kjortetoyopplysninger)
    )

class KjortetoyopplysningerSensor(Entity):
    def __init__(self, kjortetoyopplysninger):
        self.kjortetoyopplysninger = kjortetoyopplysninger

    @property
    def name(self):
        return "BIL"

    @property
    def state(self):
        return "2022-08-31"
    
    