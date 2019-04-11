from flask import jsonify
from flask import request
from flask import Flask, render_template , redirect , url_for , g


import requests

from bs4 import BeautifulSoup

import json


app = Flask(__name__)
def followers(name):

    ku=requests.get("http://www.instagram.com/"+str(name))
    soup = BeautifulSoup(ku.text, 'html.parser')

    data=soup.find_all('meta',attrs={'property':'og:description'})

    mon=data[0].get('content').split()
    if mon==None:
        return 'cannot find'
    else:
        return {'followers':mon[0],'posts':mon[2],'following':mon[4]}





@app.route('/<user_id>')
def main(user_id) :
    print(user_id)
    return jsonify(followers(user_id)) 


if __name__ == '__main__' :
    app.run()