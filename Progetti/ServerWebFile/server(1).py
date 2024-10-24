from flask import Flask, render_template, request
import requests, json, sys
import subprocess
from myjson import *
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
sGoogleApiKey = 'AIzaSyB_jCxqJnXIhE_sPAlkvb4keVz_80D9Abc'
api_url = base_url + sGoogleApiKey
api = Flask(__name__)


@api.route('/', methods=['GET'])
def index():
    return render_template('index2.html')





@api.route('/mansendfile', methods=['POST'])
def question():
    domanda = request.form['question']
    print("domanda: " + domanda)
    
    if not domanda:
        return "<HTML><BODY><h3>Domanda non ricevuta<BODY><HTML>"
    else:
        domanda += " tradotto in italiano"
        jsonDataRequest = {"contents": [{"parts": [{"text": domanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify = False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
    
        # if not f:
        #     return "<HTML><BODY><h3>File non ricevuto<BODY><HTML>"
        # else:
        #     f = request.form['file']
        #     ComponiJsonPerImmagine(f)
        #     dJsonRequest = JsonDeserialize("request.json")
        #     dJsonRequest["contents"][0]["parts"][0]["text"] = domanda
        #     response = requests.post(api_url, json=dJsonRequest, verify = False)
        #     if response.status_code == 200:
        #         dResponse = response.json()
        #         sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
        #         print()
                

    return "<HTML><BODY><h3>Domanda ricevuta<br><hr><h5> Domanda: " + domanda + "<br>" + sTestoPrimaRisposta +"</BODY></HTML>"



api.run(host="0.0.0.0",port=8085)


