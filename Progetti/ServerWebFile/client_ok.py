import requests, json, sys
import subprocess
from myjson import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
sGoogleApiKey = 'AIzaSyB_jCxqJnXIhE_sPAlkvb4keVz_80D9Abc'



def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./image.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath,"./image.jpg"])
  subprocess.run(["bash", "./creajsonpersf.sh"])


def EseguiOperazione(iOper, sServizio, dDatiToSend):
    try:
        if iOper == 1:
            response = requests.post(sServizio, json=dDatiToSend)
        if iOper == 2:
            response = requests.get(sServizio)
        if iOper == 3:
            response = requests.put(sServizio, json=dDatiToSend)
        if iOper == 4:
            response = requests.delete(sServizio, json=dDatiToSend)

        if response.status_code==200:
            print(response.json())
        else:
            print("Attenzione, errore " + str(response.status_code))
    except:
        print("Problemi di comunicazione con il server, riprova piÃ¹ tardi.")




print("Benvenuti nella mia Generative AI") 
api_url = base_url + sGoogleApiKey

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Richiedi una domanda su un'immagine")
    print("3. Esci")


    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sDomanda = input("Inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts":[{"text": sDomanda}]}]}
        response = requests.post(api_url,json=jsonDataRequest,verify=True)
        if response.status_code==200:
            #print(response.json())
            lListaRisposte = response.json()["candidates"]
            for dRisposta in lListaRisposte:
                sTestoRisposta = dRisposta["content"]["parts"][0]["text"]
                print(sTestoRisposta)

    elif iOper == 2:
        sImage = input("Inserisci file img da analizzare: ")
        sDomanda = input("Inserisci la domanda: ")
        ComponiJsonPerImmagine(sImage)
        jsonDataRequest = JsonDeserialize("request.json")
        jsonDataRequest["contents"][0]["parts"][0]["text"]=sDomanda
        response = requests.post(api_url,json=jsonDataRequest,verify=True)
        if response.status_code==200:
            #print(response.json())
            lRisposte = response.json()['candidates']
            for risposta in lRisposte:
                sTestoRisposta = risposta["content"]["parts"][0]["text"]
                print(sTestoRisposta)
    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1
    else:
        print("Operazione non disponibile, riprova.")





