import logging
from requests import get
from minemeld.ft.basepoller import BasePollerFT

LOG = logging.getLogger(__name__)

class Miner(BasePollerFT):
    def configure(self):
        pass

    def _process_item(self, item):
        # called on each item returned by _build_iterator
        # it should return a list of (indicator, value) pairs
        return [[item, {'type': 'IP', 'confidence': 100}]]

    def _build_iterator(self, now):
        # called at every polling interval
        # here you should retrieve and return the list of items
        # builds the request and retrieves the page
        try:
            res = get('https://api.github.com/meta')
            r = res.json()
            ips = []
            ips += r.get('hooks',[]) +  r.get('web',[]) +  r.get('api',[]) +  r.get('git',[]) +  r.get('pages',[]) + r.get('importers',[])
        except Exception as err:
            LOG.debug(str(err))
            raise

        return list(set(ips))
