from ..dependent import solve_many
from .extractor import Extractor


class APIExtractor(Extractor):
    
    def __init__(self, session, language=None):
        self.session = session
        self.language = language
        
    def extract(self, rev_id, features):
        # Prime the cache with pre-configured values
        cache = {'rev_id': rev_id,
                 'session': self.session}
        
        # If language is available, load utilities into the cache
        if self.language != None:
            cache.update(self.language.cache())
        
        return solve_many(features, cache=cache)
