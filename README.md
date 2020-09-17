# Minimal_Flask_Endpoint_API_for_Data_Science
https://github.com/lineality/Minimal_Flask_Endpoint_API_for_Data_Science

## Here is a guide for quickly setting up Minimal Flask Heroku Endpoint API for Deploying Data Science &amp; Machine Learning Functions, including files and tools for deploying and testing, including an HTML home page interface so you can test your functions directly from the page (and make that available to users if you want).

## Steps
- 1. (Optional) Make a github repo (optional sync heroku to that)
- 2. Set up a file system and Pipenv environment for your project
- 3. (Optional) Good idea to test out your basic endpoints locally
- 4. Create a new app on heroku.com, follow instruction there (also here) to deploy (very much like github, but it's heroku-git. 
- 5. (Optional) Test that it's working (tools here, and some built in). 
- Done!

# Guide 

## Minimal Flask API for Data Science (Doc version of guide)
https://docs.google.com/document/d/1BdTu-WxGwxuAQ_xVwjbnAXvGgQMQkYxGn_UGGV_4pPw/edit?usp=sharing

##1. Files you Need
- proc file
- pipenv file
- app.py
	
## 2. Running Flask locally to check
- https://docs.google.com/document/d/1eMlHzh0mske6XF10rchp8qDbgAu9ii8Y1ygk_YMuRno/edit?usp=sharing

- create pipenv environment (code in rReadMe)
If you have a pipfile, you can try $ pipenv install
which will re-create a pipenv/piplock from the pipfile

- If you don't have a pipefile or it's out of date, or if for whatever reason you want to make a new fresh install, run the line below. You will probably add to this but it should work to start:
```pipenv install certifi chardet click flask gunicorn idna itsdangerous jinja2 numpy pandas python-dateutil python-dotenv pytz requests urllib3 werkzeug flask-cors```

- run/create pipenv shell ($ pipenv shell)

Once you have a pipenv and shell set up and running:
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
- You can use postman locally and online, but here is a very quick colab that works for online (not locally).
-https://colab.research.google.com/drive/1IluMraiJnpiMWwBhLo73czWTrvvqcAm_?usp=sharing




### Heroku vs. AWS Notes:
- app.route (heroku)
- vs.
- application.route (AWS)




