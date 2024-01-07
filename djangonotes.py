# you dont want totouch the manage.py file
# the manage.py helps us run the code in our local host/ command line
# the settings file is the bedrock of ur whole project 
# anything done wrng in the settings file affects ur whole project
# its the file that has everything we need in our project
# all the configurations any apps we r installing anything on our databases
# urls.py we are going to specify all the urls we want in our project
# in the urls.py we will configure the urls
# to deactivate the virtual env in the command line we had created we just type in deactivate
# to get back to thevirtual env in visual studio we get to the terminal and type workon (name of the virtual env)
# work on (name of project) also works in the command terminal

# url routing  AND DJANGO APPS
# django app are a subset ofthe major project. hence the project can have many apps
# now to create the django app we shud be in the virtual env and also on the root directory ie the directory containing manage.py file . 
# all this is in the command terminal
# to create the app we use the manage.py : python manage.py startapp (name of the app)
# after running this in the command line we get differnt files in VS code 
# innit.py - is for the migrations, for the models
# admin.py - here django has this built in admin interface that allows you to control your site, view the databases
# apps.py
# models.py - is the file where we create all our databases
# dealing with databases in django is quite different because we dont need to write a single line of sql code
# tests.py - not frequently used
# views.py - is where all mainthings happen

# now to start on URL Configuration
# it is the mapping of the url in our site eg https://www.djangoproject.com/
# in my app we do not have a url file so we need to create it
# we need to import sometnhing from django called path: from django.urls import path
# this will allow us add multiple urls in a list

# 
# to run our project we go to command line and typethe command python manage.py runserver
# then we copy the url itreturns to our browser to see what we are building
# it doesnt show us anything because we have been working on myapp
# we need import sth in the main project (project 1) called includein the url file


# django template language
# we want django to be able to see our external html file 
# you do that in our root directory we will create a new folder 
# we need to tel django where to look for the templates file
# we will go to the setting.py and look for the template folder a place with DIRS
# then enter BASE_DIR, 'name of our template folder'

# sending dynamic data to your template file
# dynamic data means not the same for every user
# we will declare a variable lets say name then use a dictionary type of relationship to access it
# eg {'name': name})
# then to access it we will use the double curly braces in the index.html {{name}}
# now lets say we also had another dynamic data such as age we wanted to pass it wud make our code very bulky if repeated the above process
# to avoi this we cud use context which is popularly used in django
#context is a dictionary that we can put all our fields

# building a word counter in django
#following was done in the html file
# <h1> Input your text below </h1>
#<form method="" action=""><!--action is where we want all this data to send to. so lets send this url in the url file-->
  #<textarea name="text" rows="25" cols="100"></textarea><br>
  #<input type="submit"/>
#</form>



# GET VS POST IN DJANGO
# there r 2 types of methods ie the GET method and the POST method
# get method is mostly used wen we r not passing any personal information
#post method doesnt show the info in the url which is good esp for sensitive info
# if you leave the method blank it uses a get methof by default
# anytime we use the POST method django expects us to use a CSRF token
# CSRF- cross site request fraudery
# so we need to put the csrf token: {% csrf_token %}

# STATIC FILES
#any external file we use in our template such as an external css file 
# we need a static folder called static where all of our static files will be 
# to enablle django to find the static files; import os, then at the bottom of under the static enter the path


# site to download free templates: bootstrapmade template 
# download the website template and save it in the root directory for our local host
# then move the index.html of the website to the templates folder
# then move the assests to the static file since it contains the css files
# djngo still doesnt recognize these files hence we need to load them. also all links, images and scripts shud have {%static''%}

# MODELS
# models are used in configuring our database
# so most of the time in django you do not need to write a single sql code to get ur database running
# that is why we have sth called model,view,template
# model is what we use forour database, the view is what the user sees, templateis for the indedx.html
# models is easy to configure since wejust use the classes in python to create our database

####
# the dbsqlite fileinth e root directory stores all our databases
# as a default django uses sql lite

# after creating databases on model.py we also need to opencommand terminal
# and on the root dir we need to : python manage.py makemigrations
# then : python manage.py migrate
# this needs to be done anytime we make changes to this model.py file
# this migrated data has now gone to the django dbsqlite
# to manipulate this data that is wheere django admin panel comes in

# wen you go to /admin at the site url it asks for you to login but we do not have any credentials
# so we come into our command terminal and type python manage.py createsuperuser

# the database model which we created called feature needs to be registered in the admin.py

# USER AUTHENTICATION

##USER REGISTRATION
# we need a new url which shud be named register


# user login  and logout and django in django

# logout button is alsothe login or sign up page hece dynamic

# dynamic urls in django
# diff values being passd in the url. eg a url for profile pages for different users

# linking your project to another Dtabase



