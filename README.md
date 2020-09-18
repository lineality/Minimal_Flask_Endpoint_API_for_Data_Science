# Minimal_Flask_Endpoint_API_for_Data_Science

### Git hub Repo for this guide:
https://github.com/lineality/Minimal_Flask_Endpoint_API_for_Data_Science
 
### Doc version of this guide: https://docs.google.com/document/d/1BdTu-WxGwxuAQ_xVwjbnAXvGgQMQkYxGn_UGGV_4pPw/edit?usp=sharing

### Deployed Running Example of Demo: 
https://endpoint-template.herokuapp.com/

### Here is a guide for quickly setting up Minimal Flask Heroku Endpoint API for Deploying Data Science &amp; Machine Learning Functions, including files and tools for deploying and testing, including an HTML home page interface so you can test your functions directly from the page (and make that available to users if you want).

## Steps
1. (Optional) Repo: Make a github repo (optional sync heroku to that)
2. Pipevn: Set up a file system and Pipenv environment for your project
3. Code: Drop in the template files from this repo (can git clone from here), you can put in your real function code later. 
4. (Optional) Good idea to test out your basic endpoints locally
5. Heroku: Create a new app on heroku.com, & follow instructions there (also here) to deploy (very much like github, but it's heroku-git. 
6. (Optional) Test that it's working (tools here, and some built in). 
- Done!

# Guide:  Minimal Flask API for Data Science 


## 1. Main Files You Need
- proc file
- pipenv file
- app.py

For this minimal design, the app.py is basically your whole endpoint system, including all the functions, endpoints, flask server code, etc. (The Template directory stores the html used for the home page.)  The app.py file here includes a few types of demo endpoints. One is a 2 input post endpoint. One is a basic 'get' endpoint that posts data or whatever you want (could be help information). There is also a pre-made json-file example, those are fast. And the home page of the api url is an html display including an interactive test for not exactly the same endpoints, but alternate versions that will work from form-filled data from that page. That way the same site can be both an API for machines, and a tool for human users. 
	
## 2. Running Flask locally to check
- https://docs.google.com/document/d/1eMlHzh0mske6XF10rchp8qDbgAu9ii8Y1ygk_YMuRno/edit?usp=sharing

- create pipenv environment (code in rReadMe)
If you have a pipfile, you can try $ pipenv install
which will re-create a pipenv/piplock from the pipfile

- If you don't have a pipefile or it's out of date, or if for whatever reason you want to make a new fresh install, run the line below. You will probably add to this but it should work to start:

```pipenv install certifi chardet click flask gunicorn idna itsdangerous jinja2 numpy pandas python-dateutil python-dotenv pytz requests urllib3 werkzeug flask-cors```

- run/create pipenv shell ($ pipenv shell)

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


