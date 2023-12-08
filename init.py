import requests
from flask import Flask, render_template, redirect, url_for, request, session, flash, app, Blueprint, jsonify


def new_quote():
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'ZmT0LPspKjXo3Bh7OxePpA==1TJoxItFfZdtXVQt'})
    data = response.json()
    data1 = data[0]  ##data1 is dictonary

    return data1


#Initialize Flask app
app = Flask(__name__)

@app.route('/')
@app.route('/new')
def home():
    return render_template('index.html', data1=new_quote())



if __name__ == '__main__':
    app.run(debug=True)
