import mediacloud, datetime ## mediacloud API
import logging, unittest ## unit testing
from config import KEY ## personal config

#### Initialize logging: https://docs.python.org/3/howto/logging-cookbook.html
# create logger
logger = logging.getLogger('testlogger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

#'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


class mediacloudTest(unittest.TestCase):

	def setUp(self):
		self.mc = mediacloud.api.MediaCloud(KEY)
		
	
	def connectMC(self):
		logger.info('Checking API key is included...')
		assert self.KEY is not None
		logger.info('Checking MediaCloud is connected...')
		assert mc is not None
		logger.info('Connecting to API...')
		logger.error("Error connecting API!")

	def testCount(self):
		mc = mediacloud.api.MediaCloud(KEY)

		logger.info('Querying for test word [HILLARY] in September 2016...')
		res = mc.sentenceCount("Hillary", solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 9, 30) ), 'tags_id_media:1' ])
		count = res['count']

		logger.info('Finding results on Mediacloud...')
		print ("SENTENCES CONTAINING THE WORD 'Hillary' IN SEPTEMBER 2016: ", count)
		assert count > 0
		logger.error("Error counting sentences!")

# if this file is run directly, run the tests
if __name__ == "__main__":
    unittest.main()
