import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/memes')
def getMeme():
    urlmeme = "https://dog.ceo/api/breeds/image/random"
    dados = requests.get(urlmeme)
    res = dados.json()
    resultado = res["message"]
    print(resultado)
    return render_template( "meme.html", r = resultado )


if __name__ == '__main__':
    app.run()