from flask import jsonify
from flask import request
from flask import Flask, render_template , redirect , url_for , g


import requests

from bs4 import BeautifulSoup

import json


app = Flask(__name__)
def followers(name):

    ku=requests.get("http://www.instagram.com/"+str(name))
    if ku.status_code != 200 :
        return {"errmsg" : "not found"}
    else :    
        soup = BeautifulSoup(ku.text, 'html.parser')
        data=soup.find_all('meta',attrs={'property':'og:description'})
        mon=data[0].get('content').split()
        return {'errmsg' :'success' , 'followers':mon[0],'posts':mon[4],'following':mon[2]}



@app.route('/')
def ret():
    return jsonify({"errmsg" : "not found"})

@app.route('/<user_id>')
def main(user_id) :
    return jsonify(followers(user_id)) 


if __name__ == '__main__' :
    app.run()