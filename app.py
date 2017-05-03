
import os
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        # because I exceeded my limit, lets make it authenticated
        resp = requests.get("https://api.github.com/users/"+ username +"/keys?state=closed&access_token=28204bde5c3dc023967893e7717f92d59c53bc3e")
        print resp.status_code
        response_dict = resp.json()
        if resp.status_code != 200:
            error = "Username not found"
            return render_template('index.html', error=error)

        else:
            return render_template('index.html', username=username,response_dict=response_dict)

@app.route('/<username>', methods=['GET'])
def show_user_profile(username):
    resp = requests.get("https://api.github.com/users/"+ username +"/keys?state=closed&access_token=28204bde5c3dc023967893e7717f92d59c53bc3e")
    print resp.status_code
    response_dict = resp.json()
    if resp.status_code != 200:
        error = "Username not found"
        return render_template('profile.html', error=error)

    else:
        return render_template('profile.html', username=username,response_dict=response_dict)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

