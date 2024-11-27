from flask import Flask, render_template, request
import os
import shutil
from myjson import *
import requests
import base64
from pathlib import Path
import urllib3

urllib3.disable_warnings()


api = Flask(__name__)

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-exp-0827:generateContent?key="

googleAPIKey = "AIzaSyB_jCxqJnXIhE_sPAlkvb4keVz_80D9Abc"

api_url = base_url + googleAPIKey

cartella_di_partenza = input("Inserisci la directory in cui effettuare la ricerca: ")
parola = input("Inserisci la parola da cercare: ")
cartella_di_destinazione = input("Inserisci la cartella di output: ")

def cerca_e_copia_file(cartella_di_partenza, parola, cartella_di_destinazione):
    print()
    if not os.path.exists(cartella_di_destinazione):
        os.makedirs(cartella_di_destinazione)

    cartella_di_partenza = Path(cartella_di_partenza).absolute()
    
    for root, _, files in os.walk(cartella_di_partenza):
        for file in files:
            if parola in file:
                percorso_file = os.path.join(root, file)
                print(f"Trovato file {file}\n")
                shutil.copy2(percorso_file, cartella_di_destinazione)
                print(f"Copiato: {file} -> {cartella_di_destinazione}\n")
            else:
                extension_supportate: dict = {".pdf": "application/pdf", ".gif": "image/gif", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", "png": "image/png"}
                percorso_file = os.path.join(root, file)
                filename, file_extension = os.path.splitext(percorso_file)
                if file_extension not in extension_supportate:
                    print("Impossibile aprire il file, estenzione non supportata\n")
                    continue
                
                with open(percorso_file, "rb") as file_to_read:
                    file_base_64 = base64.b64encode(file_to_read.read())
                mime_type = extension_supportate[file_extension]
                domanda = "Dentro questo file c'Ã¨ qualcosa che riguarda il tema: " + parola + " rispondi solo 'SÃ¬' o 'No' " 
                jsonDataRequest = {"contents": [{"parts":[{"text": domanda},{"inline_data": {"mime_type": mime_type, "data": file_base_64}}]}]}
                response = requests.post(api_url, json=jsonDataRequest, verify=False)
                if response.status_code == 200:
                    response = response.json()
                    testo = response['candidates'][0]['content']['parts'][0]['text']
                    if testo == 'SÃ¬':
                        print(f"Trovato file {file}\n")
                        shutil.copy2(percorso_file, cartella_di_destinazione)
                        print(f"Copiato: {file} -> {cartella_di_destinazione}\n")
                        
                    else:
                        continue  
                else:
                    print("Errore server\n")
                    continue

cerca_e_copia_file(cartella_di_partenza, parola, cartella_di_destinazione)