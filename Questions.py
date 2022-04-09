from pprint import pprint
import nltk
import json
nltk.download('stopwords')
from Questgen import main
from youtube_transcript_api import YouTubeTranscriptApi
from operator import itemgetter

def boolean_questions(payload):
    qe= main.BoolQGen()
    output = qe.predict_boolq(payload)
    pprint (output)
    return output

def mcq_questions(payload):
    qg = main.QGen()
    output = qg.predict_mcq(payload)
    pprint (output)
    return output

# need the payload only
def faq_questions(payload):
    qg = main.QGen()
    output = qg.predict_shortq(payload)
    pprint (output)
    return output

# need payload and number of questions
def paraphrasing_questions(payload, num_questions):
    qg = main.QGen()
    text2=faq_questions(payload)
    text=json.dumps(text2)
    text3=json.loads(text)
    text4=text3['questions'][0]['Question']
    payload2 = {
    "input_text" : text4,
    "max_questions": num_questions }
    pprint(payload2)
    output = qg.paraphrase(payload2)
    pprint (output)
    return output

def getTranscript(video_id):
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['en'])
    transcript2 = transcript.fetch()
    x=''
    res = list(map(itemgetter('text'), transcript2))
    for i in res:
        x+=' '+i;
    print(x)
    return x;

# getTranscript('vAoB4VbhRzM')
