from flask import Flask, json, request
import base64

utenti = [["mario", "passwd123", "rw"],
          ["lorenzo", "passwd456", "read"]]

cittadini=[["Lorenzo", "Pippo", "12/06/2004", "PPPLNZ80A01H501N"],
        ["Filippo", "Rossi", "16/07/2002", "FFPLNZ80A01T502N"],
        ["Luca", "Verdi", "22/12/1999", "PPLNZ70A01G501N"]]

api = Flask("__name__")


@api.route('/create', methods = ['POST'])
def process_json():
    print("Ricevuta chiamata")

    #lettura dati basic authentication per VERIFICA
    auth = request.headers.get('Authorization')
    auth = auth[6:]
    security_data = base64.b64decode(auth)
    print(security_data)

    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        print(jsonReq)
        cittadini.append(jsonReq)
        jsonResp = {"Esito":"ok","Msg":"Dato inserito"}	
        return json.dumps(jsonResp)
    else:
        return 'Content-Type not supported!'



@api.route('/read', methods = ['POST'])
def process_json1():
    print("Ricevuta chiamata")

    #lettura dati basic authentication per VERIFICA
    auth = request.headers.get('Authorization')
    auth = auth[6:]
    security_data = base64.b64decode(auth)
    print(security_data)
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        print(jsonReq)
        print(cittadini)
        jsonResp = {"Esito":"ok","Msg":"Dato inserito"}
        return json.dumps(jsonResp)
    else:
        return 'Content-Type not supported!'

if __name__ =='__main__':
    api.run(host = "127.0.0.1", port = 8080, ssl_context='adhoc')
