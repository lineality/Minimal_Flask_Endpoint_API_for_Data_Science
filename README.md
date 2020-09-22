# Minimal_Flask_Endpoint_API_for_Data_Science

#### Here is a guide for quickly setting up Minimal Flask Heroku Endpoints for Deploying Data Science &amp; Machine Learning Functions, including files and tools for deploying and testing, and an HTML home page interface so you can test your functions directly from the page (and make that available to users if you want).

Doc version of this guide:  https://docs.google.com/document/d/1BdTu-WxGwxuAQ_xVwjbnAXvGgQMQkYxGn_UGGV_4pPw/edit?usp=sharing

### Git hub Repo for this guide:
https://github.com/lineality/Minimal_Flask_Endpoint_API_for_Data_Science
 
### Deployed Running Example of Demo: 
https://endpoint-template.herokuapp.com/

### Endpoint on Deployed Running Example of Demo: POST
https://endpoint-template.herokuapp.com/demo_post

### Endpoint on Deployed Running Example of Demo: GET
https://endpoint-template.herokuapp.com/dummy_data


## Steps
1. (Optional) Repo: Make a github repo (optional sync heroku to that)
2. Pipenv: Set up a file system and Pipenv environment for your project
3. Code: Drop in the template files from this repo (git clone from here), you can put in your real function code later. 
4. (Optional) Good idea to test out your endpoints locally
5. Heroku: Create a new app on heroku.com, & follow instructions there (also here) to deploy (very much like github, but it's heroku-git. 
6. (Optional) Test that your endpoints are working (tools linked here, and some built in). 
- Done!


# Guide:  Minimal Flask API for Data Science 

## Main Files You Need (for Heroku to run a flask api)
- proc file
- pipenv file
- app.py

For this minimal design, the app.py is basically your whole endpoint system, including all the functions, endpoints, flask server code, etc. (Optional Exception: The Template directory stores the html used for the home page.)  The app.py file here includes a few types of demo endpoints. One is a 2 input post endpoint. One is a basic 'get' endpoint that posts data or whatever you want (could be help information). There is also a pre-made json-file endpoint example; those are fast. Usually with an API, the URL is only for machines has no interface for a user who goes to that URL with a browser, but it is possible to make an HTML interface to let a user interact with endpoints through HTML on that URL (e.g. the home page). The demo home page of the api url is an html display to use endpoints. Note: the HTML version does not hit exactly the same endpoints (due to json-input formatting), but as a way to test the endpoint functions these HTML-endpoints are identical in how they handle input and output. In other words, this way of making a page includes a built-in interactive-html-interface endpoint-test for not exactly the same endpoints, but alternate versions that will work from form-filled data from that html page. That way the same site can be both an API for machines, and a tool for human users, albeit using two sets of endpoints.

# Steps to Deploy Your Endpoints

## Step 1. Make a github repo for your project
It is probably a good idea (if not absolutely necessary) to make a github repo for your project. In this case, using a fork of this demo (using clone command below) is probably best and easiest. 
```
git clone https://github.com/lineality/Minimal_Flask_Endpoint_API_for_Data_Science.git
```
Note: after you clone a repo, cd (change directory) into that repo! Easy to forget. 

You can also sync your heroku app to this directly if you want later, making versioning and syncing that much more streamlined. Note: After you make the repo (or use a clone of the demo).

## Step 2. Make your pip environment
Heroku is like a container deployment system. Your endpoint is self contained environment in Heroku running on a server (with HTTPS and all the great things that Heroku does for you). 
For Heroku to work you will need to tell heroku what packages it needs to install to run your programs. Having the pipfile and piplock files should be enough. A requirements.txt file may also work.
In theory since the system only needs to run on heroku, you can just upload the pipfile and piplock environment files to heroku without ever building an environment locally to test on your local machine first. But testing locally is recommended. 

Here are two ways to (re)create the pip environment from the files in the template

Way 1. (re)create pipenv environment (code in ReadMe)
If you have a pipfile, you can try the command below which will re-create a pipenv/piplock from the pipfile:
```
$ pipenv install
```
An advantage of this is that it will use the same package versions which may be necessary so that everything 'plays nice' and runs together. A disadvantage can be that if the project you are copying this way is an old project, the packages may be unnessesarily old versions and using new versions may be safe and a good idea. E.g. for this demo code, it's probably best to use the newest versions of the packages and libraries listed here. 


Way 2: If you do not have a pipefile or it's out of date, or if for whatever reason you want to make a new fresh install, run the line below. You will probably add to this but it should work to start:
```
pipenv install certifi chardet click flask gunicorn idna itsdangerous jinja2 numpy pandas python-dateutil python-dotenv pytz requests urllib3 werkzeug flask-cors
```

- To start and enter the pipenv shell to test your code: run in terminal $ pipenv shell

Guide on Pipenv and Editor Configuration:
https://docs.google.com/document/d/1dZJI20D7uIknT1pdlTSmlHH1WPYdVhs2PSUyH1qdnUo/edit?usp=sharing


## Step 3. Code & Functions
To start with you can deploy the default demo code. The github template contains a working demo so you don't have to add anything just to get it running. The app.py file contains the flask and endpoint and function code. 

Especially with flask and heroku, it is a recommended strategy to start with something that works and test the endpoints with every single small change you make. Debugging a one function on your computer is bad enough. Debugging broken spaghetti code through a deployed endpoint is close to impossible. Test after every change you make and you avoid a lot of trouble. Testing locally on flask can be useful, but make sure you test deployment to heroku. Code that works fine locally on your computer (on a local flask server) may not work on Heroku and the more changes you make between deployed tests makes debugging that much harder.

Add your code: When you have your own functions that you want to deploy, incrementally add those changes small piece by small piece to the working demo to make sure everything works. 

To use the HTML you'll need to make two copies of your endpoint, one for a machine endpoint, and one for the HTML human endpoint:
- Make your own (for machines) endpoint that does something new you'll need to put new code into the demo endpoint. 
- To Set up an HTML easy-testing function, copy and past the machine function, rename it, and change the format of the input following the demo examples. This is completely optional but it is very helpful to have both for testing and for users. 


## Step 4. Running Flask locally to check your code

**Note: You must be in your pipenv-shell!** (Your computer's name in the terminal should appear different if you are in your pipenv shell) If you are not in a shell, go back to step 2. If you are unsure, open a fresh terminal in your directory and start again. 

Once you have a pipenv and shell set up and running (and files to run):
- Run your flask server: Run in command in a terminal:
```
$ python3 app.py
```
(on your machine it may be "$ python app.py"

- For more information on running flask servers: Guide for Different Ways to Run Flask Apps https://docs.google.com/document/d/1eMlHzh0mske6XF10rchp8qDbgAu9ii8Y1ygk_YMuRno/edit?usp=sharing


## Step 7. Heroku: Deploying to Heroku
Create a new app on heroku.com, & follow instructions there (also here) to deploy (very much like github, but it's heroku-git. 

Go to https://dashboard.heroku.com/ and login or make an account. (free tier should be fine)
You may also need to install the heroku command line interface (details depend on your OS). 
Follow instructions to create a new app, which should be similar to this:
```
# $ heroku login
# $ cd my-project/
# $ git init
# $ heroku git:remote -a NAME_OF_YOUR_APP
# $ git add .
# $ git commit -am "make it better"
# $ git push heroku master
```

## Step 8. Testing Endpoints
- You can use postman locally and online, but here is a very quick colab that works for online (not locally). https://colab.research.google.com/drive/1IluMraiJnpiMWwBhLo73czWTrvvqcAm_?usp=sharing

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
If you can use this tutorial to make a working heroku endpoint, then moving that to AWS should be manageable (at least you know the code the steps, the difficulty will be in navigating AWS services, but the same code (with the above term change) should work just fine. Elastic Beanstalk and HTTPS services are probably a good way to go.

### Other links:

Search Functions in Pandas.ipynb
https://colab.research.google.com/drive/1xKgXm0EQJgCkKBqhFiYw8TG2K83LfGAQ#scrollTo=eKIKzxe8P-PD

Plotly Dash Heroku Github Tutorial Notes: For a graphical interface to your DS function
https://docs.google.com/document/d/1t-Jxd8bInY10KpIg4eklPNZT6m9o5WiFptB1e6wdEEc/edit

AWS & HTTPS Guide
https://docs.google.com/document/d/18ivF-ACu-sFEomPXmymua-p1_uWXorqMkm4GCKMT7P4/edit?usp=sharing

