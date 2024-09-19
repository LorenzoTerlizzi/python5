from flask import Flask, render_template, request

utenti=[["Lorenzo", "Pippo", "pippo@gmail.com", "PPPLNZ80A01H501N", "0"], ["Stefano", "Gialli", "stefano@gmail.com", "FFFNGG80A02H501N", "0"], ["Luca", "Rossi", "luca@gmail.com", "LLLG90AH03AH501N", "0"]]
api = Flask("__name__")

@api.route('/Registrati', methods = ['POST'])
def sumbit():
    nome=request.form['nome']
    cognome=request.form['cognome']
    email=request.form['email']
    codice_fiscale=request.form['cf']

    for utente in utenti:
        if (utente[0] == nome and 
        utente[1] == cognome and 
        utente[2] == email and 
        utente[3] == codice_fiscale):
            return render_template('reggok.html')
    return render_template('reggko.html')

    

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


if __name__ =='__main__':
    api.run(host = "0.0.0.0", port = 8085)
