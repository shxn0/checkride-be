from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from .. import config

async def call(upload_file):
    authenticator = IAMAuthenticator(config.WATSON_API_KEY)
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url(config.WATSON_ENDPOINT)

    with open(f'{config.FILE_PATH}{upload_file.filename}','rb') as audio_file:
        response = speech_to_text.recognize(
            audio = audio_file,
            content_type = config.CONTENT_TYPE,
            model = config.MODEL
        ).get_result()

    # print(response['results'], flush=True)
    print("***** Completed *****")
    scripts = list()
    for i in response['results']:
        for j in i['alternatives']:
            scripts.append(j['transcript'])

    print(scripts, flush=True)
    return scripts