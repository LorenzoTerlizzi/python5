from flask import Flask, render_template, request
import requests, json, sys
import subprocess
from myjson import *
import urllib3
import base64
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
    elif not request.files['filedomanda']:
        domanda += " tradotto in italiano"
        jsonDataRequest = {"contents": [{"parts": [{"text": domanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest, verify = False)
        if response.status_code == 200:
            dResponse = response.json()
            sTestoPrimaRisposta = dResponse['candidates'][0]['content']['parts'][0]['text']
        return '<HTML><BODY>' + sTestoPrimaRisposta + '</BODY></HTML>'
    else:
        file = request.files['filedomanda']
        jsonDataRequest = {
        "contents":[
            {
            "parts":[
                {"text": domanda},
                {
                "inline_data": {
                    "mime_type":"image/jpeg",
                    "data": base64.b64encode(file.read()).decode("utf-8")
                }
                }
            ]
            }
        ]
        }
        response = requests.post(api_url,json=jsonDataRequest, verify=False)
        dResponse = response.json()
        risposta = dResponse['candidates'][0]['content']['parts'][0]['text']
        return '<HTML><BODY>' + risposta + '</BODY></HTML>'



api.run(host="0.0.0.0",port=8085)


