import requests, json
from requests.auth import HTTPBasicAuth

username = ""
password = ""

def StampaMenuOperazioni():
    print("1. Inserisci cittadino")
    print("2. Leggi dati cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Inserisci credenziali")
    print("6. Exit")
    comando = input("Inserisci comando: ")
    return comando

def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    data_nascita = input("Inserisci la data di nascita: ")
    cf = input("Inserisci il codice fiscale: ")
    datiCittadino = [nome, cognome, data_nascita, cf]
    return datiCittadino

def print_list(dData):
    print(dData)

def AcquisisciCredenziali():
    global username, password
    username = input("Inserisci username: ")
    password = input("Inserisci password: ")


print("Cosa vuoi fare?")
comando = StampaMenuOperazioni()
print("comando inserito" + comando)
if comando == "1":
    api_url = "https://127.0.0.1:8080/create"
    jsonDataRequest = GetDatiCittadino()
    
    response = requests.post(api_url, json = jsonDataRequest, verify=False, auth=HTTPBasicAuth(username, password))
    print(response.status_code)
    print(response.headers["Content-Type"])

    if (type(response.json()) is list):
        print_list(response.json())

if comando == "2":
    api_url = "https://127.0.0.1:8080/read"

    response = requests.get(api_url, verify=False, auth=HTTPBasicAuth(username, password))
    print(response.status_code)
    print(response.headers["Content-Type"])
    if (type(response.json()) is list):
        print_list(response.json())

if comando == "3":
    api_url = "https://127.0.0.1:8080/update"
    jsonDataRequest = GetDatiCittadino()
    
    response = requests.post(api_url, json = jsonDataRequest, verify=False, auth=HTTPBasicAuth(username, password))
    print(response.status_code)
    print(response.headers["Content-Type"])
    
    if (type(response.json()) is list):
        print_list(response.json())

if comando == "4":
    api_url = "https://127.0.0.1:8080/delete"
    jsonDataRequest = GetDatiCittadino()

    response = requests.post(api_url, json = jsonDataRequest, verify=False, auth=HTTPBasicAuth(username, password))
    print(response.status_code)
    print(response.headers["Content-Type"])
    
    if (type(response.json()) is list):
        print_list(response.json())



if comando == "5":
    AcquisisciCredenziali()


