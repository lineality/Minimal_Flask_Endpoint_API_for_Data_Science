# Minimal_Flask_Endpoint_API_for_Data_Science

#### Here is a guide for quickly setting up Minimal Flask Heroku Endpoints for Deploying Data Science &amp; Machine Learning Functions, including files and tools for deploying and testing, and an HTML home page interface so you can test your functions directly from the page (and make that available to users if you want).
 
 
### Git hub Repo for this guide:
https://github.com/lineality/Minimal_Flask_Endpoint_API_for_Data_Science
 
### Doc version of this guide:  
https://docs.google.com/document/d/1BdTu-WxGwxuAQ_xVwjbnAXvGgQMQkYxGn_UGGV_4pPw/edit?usp=sharing

### Deployed Running Example of Demo: 
https://endpoint-template.herokuapp.com/

### Endpoint on Deployed Running Example of Demo: POST
https://endpoint-template.herokuapp.com/demo_post

### Endpoint on Deployed Running Example of Demo: GET
https://endpoint-template.herokuapp.com/dummy_data

## Steps
1. (Optional) Repo: Make a github repo (optional sync heroku to that)
2. Pipevn: Set up a file system and Pipenv environment for your project
3. Code: Drop in the template files from this repo (can git clone from here), you can put in your real function code later. 
4. (Optional) Good idea to test out your basic endpoints locally
5. Heroku: Create a new app on heroku.com, & follow instructions there (also here) to deploy (very much like github, but it's heroku-git. 
6. (Optional) Test that your endpoints are working (tools here, and some built in). 
- Done!

# Guide:  Minimal Flask API for Data Science 


## Main Files You Need (for Heroku to run a flask api)
- proc file
- pipenv file
- app.py

For this minimal design, the app.py is basically your whole endpoint system, including all the functions, endpoints, flask server code, etc. (The Template directory stores the html used for the home page.)  The app.py file here includes a few types of demo endpoints. One is a 2 input post endpoint. One is a basic 'get' endpoint that posts data or whatever you want (could be help information). There is also a pre-made json-file example, those are fast. And the home page of the api url is an html display including an interactive test for not exactly the same endpoints, but alternate versions that will work from form-filled data from that page. That way the same site can be both an API for machines, and a tool for human users. 

## Step 1. Make a github repo for your project
You can also sync your heroku app to this directly if you want later, making versioning and syncing that much more streamlined.

## Step 2. Make your pip environment
Heroku is like a container deployment system. Your endpoint is self contained environment in Heroku running on a server (with HTTPS and all the great things that Heroku does for you). 
For Heroku to work you will need to tell heroku what packages it needs to install to run your programs. Having the pipfile and piplock files should be enough. A requirements.txt file may also work.
In theory since the system only needs to run on heroku, you can just upload the pipfile and piplock environment files to heroku without ever building an environment locally to test on your local machine first. But testing locally is recommended. 

Here are two ways to (re)create the pip environment from the files in the template
1. create pipenv environment (code in ReadMe)
If you have a pipfile, you can try $ pipenv install
which will re-create a pipenv/piplock from the pipfile

2. 
```pipenv install certifi chardet click flask gunicorn idna itsdangerous jinja2 numpy pandas python-dateutil python-dotenv pytz requests urllib3 werkzeug flask-cors```

- To start and enter the pipenv shell to test your code: run in terminal $ pipenv shell

Guide on Pipenv and Editor Configuration:
https://docs.google.com/document/d/1dZJI20D7uIknT1pdlTSmlHH1WPYdVhs2PSUyH1qdnUo/edit?usp=sharing


## Step 3. Drop in the code for your Endpoints App
The github template contains a working demo so you don't have to add anything just to get it running. The app.py file contains the flask and endpoint and function code. 
- To make your own endpoint that does something new you'll need to put new code into the demo endpoint. 
- To set up an HTML easy-testing function, you'll need to modify the html template to fit what your new input is.
 	
## Step 4. Running Flask locally to check
- Guide for Different Ways to Run Flask Apps https://docs.google.com/document/d/1eMlHzh0mske6XF10rchp8qDbgAu9ii8Y1ygk_YMuRno/edit?usp=sharing


- If you don't have a pipefile or it's out of date, or if for whatever reason you want to make a new fresh install, run the line below. You will probably add to this but it should work to start:


Once you have a pipenv and shell set up and running (and files to run):
- $ python3 app.py

## 3. Deploying to Heroku
```
# $ heroku login
# $ cd my-project/
# $ git init
# $ heroku git:remote -a NAME_OF_YOUR_APP
# $ git add .
# $ git commit -am "make it better"
# $ git push heroku master
```

## 4. Testing Endpoints
- You can use postman locally and online, but here is a very quick colab that works for online (not locally). https://colab.research.google.com/drive/1IluMraiJnpiMWwBhLo73czWTrvvqcAm_?usp=sharing

## 5. Heroku
Create a new app on heroku.com, & follow instructions there (also here) to deploy (very much like github, but it's heroku-git. 

## 6. Test that your endpoints are working 

- You can use postman (or something similar) locally and online 
https://www.postman.com/

- Here is a very quick colab that works for online (not locally). https://colab.research.google.com/drive/1IluMraiJnpiMWwBhLo73czWTrvvqcAm_?usp=sharing

- For a quick local test of the functions, you can use the built-in HTML interface that lets you hit a version of the endpoint. 
https://github.com/lineality/Minimal_Flask_Endpoint_API_for_Data_Science/tree/master/templates
In the templates file you will find the base.html file that is used. You will need to modify this and the endpoint it uses (if you're making your own new endpoint).


### Heroku vs. AWS Notes:
An AWS deployment is very similar, but there are some small differences. e.g.
- app.route (heroku)
- vs.
- application.route (AWS)


Other links:

Search Functions in Pandas.ipynb
https://colab.research.google.com/drive/1xKgXm0EQJgCkKBqhFiYw8TG2K83LfGAQ#scrollTo=eKIKzxe8P-PD

Plotly Dash Heroku Github Tutorial Notes
https://docs.google.com/document/d/1t-Jxd8bInY10KpIg4eklPNZT6m9o5WiFptB1e6wdEEc/edit


