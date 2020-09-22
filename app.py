#version 1: Miminal Endpoint API (Flask, Heroku)

## Instructions For Heroku Login & Deploy
#
# $ heroku login
# $ cd my-project/
# $ git init
# $ heroku git:remote -a NAME_OF_YOUR_APP
# $ git add .
# $ git commit -am "make it better"
# $ git push heroku master

## Instructions To create the pipenv in terminal
# pipenv install certifi chardet click flask gunicorn idna itsdangerous jinja2 numpy pandas python-dateutil python-dotenv pytz requests urllib3 werkzeug flask-cors

# ## sample pipenv
# [[source]]
# name = "pypi"
# url = "https://pypi.org/simple"
# verify_ssl = true
#
# [dev-packages]
#
# [packages]
# certifi = "*"
# chardet = "*"
# click = "*"
# flask = "*"
# gunicorn = "*"
# idna = "*"
# itsdangerous = "*"
# jinja2 = "*"
# numpy = "*"
# pandas = "*"
# python-dateutil = "*"
# python-dotenv = "*"
# pytz = "*"
# requests = "*"
# urllib3 = "*"
# werkzeug = "*"
# flask-cors = "*"
#
# [requires]
# python_version = "3.8"

# Import Packages & Libraries
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# Optional
dummy_data = {
"A": 1,
"B": "2",
"C": 3.0,
}

# Required for Flask/Heroku
app = Flask(__name__)
CORS(app)

# note: for herkoku or aws use private environment variables
# use dotenv
#
# Need to install git secrets

# Your Home Screen
@app.route('/')
def home():
    # Displays a basic app written in HTML so that code can be tested directly.
    return render_template('base.html')

# Main Demo Endpoint, using user-input
#
# Likely you will eventually use this kind of endpoint
# that runs a function, processes, input, and gives output


def multiple_terms():
    json_obj = {'search': [{'feature': request.values['feature1'], 'terms': request.values['terms1']},
                            {'feature': request.values['feature2'], 'terms': request.values['terms2']}],
                'offset': request.values['offset'], 'range': request.values['range']}

@app.route('/endpoint_1_post_HTML', methods=['POST'])
def endpoint_1_post_HTML():

    # this gets the json object from the user
    json_obj = {'input_1': request.values['input_1'], 'input_2': request.values['input_2']}

    # variables that are use-able by python
    input_1_item = json_obj["input_1"]
    input_2_item = json_obj["input_2"]

    ####
    ## Your Actual function/model Code Goes Here
    ####
    # example of just returning the input
    new_string = input_1_item + input_2_item
    demo_output = {"answer is combined inputs": new_string}

    # this turns output into a json object
    json_output = jsonify(demo_output)

    # returns the json format output
    return json_output

# input form: {'input_1': "x", 'input_2': "y"}
@app.route('/post_endpoint_1', methods=['POST'])
def post_endpoint_1():

    # this gets the json object from the user
    json_obj = request.get_json(force=True)

    # These lines brake up the json object into
    # variables that are use-able by python
    input_1_item = json_obj["input_1"]
    input_2_item = json_obj["input_2"]

    ####
    ## Your Actual function/model Code Goes Here
    ####
    # example of just returning the input
    new_string = input_1_item + input_2_item
    demo_output = {"answer": new_string}

    # this turns output into a json object
    json_output = jsonify(demo_output)

    # returns the json format output
    return json_output


# dummy data is often useful at the start of a project before you have real data
# no input needed for this endpoint
@app.route('/data_get_endpoint')
def data_get_endpoint():
    return jsonify(dummy_data)


# premade json files for output can be useful (super-fast)
# no input needed for this endpoint
@app.route('/prefab_endpoint_1', methods=['GET'])
def prefab_endpoint_1():
    return open('json_file.json','r').read()


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
