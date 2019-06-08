from flask import jsonify
from flask import request
from flask import Flask, render_template , redirect , url_for , g
import re

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
        usercount_inter= soup.find_all('script', attrs={'type': 'application/ld+json'})
        user_count=re.findall(r'\"(.+?)\"',str(usercount_inter))
        mon=data[0].get('content').split()
        if len(user_count)!=0:
            followers = user_count[-3]
            #bio=user_count[10]
        else:
            followers=mon[0]
            #bio='NA'
        
        return {'errmsg' :'success' , 'followers':followers,'posts':mon[4],'following':mon[2]}



@app.route('/')
def ret():
    return jsonify({"errmsg" : "not found"})

@app.route('/<user_id>')
def main(user_id) :
    return jsonify(followers(user_id)) 


if __name__ == '__main__' :
    app.run()