from urllib import response
import urllib.parse
import requests
import json
from datetime import date
from datetime import datetime
import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

DOMAIN = "vegvesen"
DATA_VEGVESEN = "data_vegvesen"

CONF_KJENNEMERKE = "kjennemerke"


DEFAULT_DATE_FORMAT = "%d/%m/%Y"

CONST_URL_KJENNEMERKE = (
    "https://kjoretoyoppslag.atlas.vegvesen.no/ws/no/vegvesen/kjoretoy/kjoretoyoppslag/v1/oppslag/raw/[kjennemerke]"
)
CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_KJENNEMERKE): cv.string,
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)
def setup(hass, config):
    """Set up the vegvesen component."""
    kjennemerke = config[DOMAIN][CONF_KJENNEMERKE]


    vegvesen = Vegvesen(
        kjennemerke
    )
    hass.data[DATA_VEGVESEN] = vegvesen

    return True

class Vegvesen:
    def __init__(self, kjennemerke):
        self.kjennemerke = self._url_encode(kjennemerke)

    @staticmethod
    def _url_encode(string):
        string_dcode_encode = urllib.parse.quote(urllib.parse.unquote(string))
        if string_dcode_encode != string:
            string = string_dcode_encode
        return string

    def _get_kjoretoyopplysninger_from_web_api(self):
        #header = {}
        url = CONST_URL_KJENNEMERKE
        url = url.replace("[kjennemerke]", self.kjennemerke)
        
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            data = response.text
            return data
        else:
            _LOGGER.error(response.status_code)
    
    def _get_from_web_api(self):
        kjoretoyopplysninger = self._get_kjoretoyopplysninger_from_web_api()

        _LOGGER.debug(f"Kjoretoyopplysninger: {kjoretoyopplysninger}")
        return kjoretoyopplysninger

        
