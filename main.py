from info import _database, base
from model.ema.guidline import EMSscraper
from utils.utils import Utils

utils = Utils(info=base)

EMSscraper = EMSscraper(utils=utils)
EMSscraper.run()
