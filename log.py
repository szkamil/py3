import logging
import lo 

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='/Users/kamil/Documents/Python/Rest2/log.txt', level=logging.INFO, format=LOG_FORMAT)



logger = logging.getLogger()

logger.info('afsdsd')