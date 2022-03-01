from dotenv import load_dotenv
load_dotenv()

import os
WATSON_API_KEY = os.getenv('WATSON_API_KEY')
WATSON_ENDPOINT = os.getenv('WATSON_ENDPOINT')
CONTENT_TYPE = 'audio/wav'
FILE_PATH = '../files/'
MODEL = 'ja-JP_NarrowbandModel'