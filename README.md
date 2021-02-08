# Django Portfolio Blog

### Setup the Workspace
Open your terminal and cd to the location you want to store your project. 
``` code 
mkdir myNewProject
cd myNewProject
```
Create a virtual enviorment for your project to live in. In this case, I'm naming the enviorment env. If you don't have venv insalled, go here.
``` code 
python -m venv env
```
Next, make sure you activate the virtual enviorment prior to installing django.
```
source env/bin/activate
```
Now it's time to install djagno in the virtual enviorment. You should see the env turned on.
```
(env): pip install django --upgrade pip
```
### Start the Project
Now it's time to start our Django Project. You can name your's whatever you like, just replace myproject with your project name. We will also start the app that will house all of our pages.
```
(env): django-admin startproject myproject
(env): cd myproject
(env): django-admin startapp pages
```
### Open and Configure
Go to the settings file and add your app to the bottom of the installed apps.
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages'
]
```
**Static Files & Templates** 

Everyone sets up their projects differntly. Some poeple like to keep the static files and templates the way they are. I like to create folders in the base directory to keep everything in one spot. To do so, simply add the following to the bottom of your settings file.
``` python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```

Since we are refrencing the BASE_DIR, we have to change a few more settings above. First, import os at the top of the project.
``` python
import os
```
Next, configure the database settings. For this project, we will be sticking with sqlite provided by django. 
``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
We also need to tell Django where to look for our templates since we will be keeping them in the root of our project. Just change the 'DIRS' part of the settings.
```python
TEMPLATES = [
    {
        ...

        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        ...
        
]
```
The last thing we need to do in the settings file for now is tell Django what BASE_DIR is. At the top of the file, change the BASE_DIR settings to the following 
```python  
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```


### Create the Static and Template Folders
Create three folders, static, media, and templates, in the base directory of your project. Your project should look similar to the following,
```
- env
- myNewProject
  |-- > media
  |-- > myNewProject
  |-- > pages
  |-- > static
  |-- > templates
  |-- db.sqlite3
  |-- manage.py
```
Finally, run the following commands to migrate the database for your project.
```
python manage.py makemigrations
python manage.py migrate
```
**Extra Tid Bit**
Sometimes, writing the same commands over and over can become time consuming. It's great to establish the muscle memory but once you've done it a few times, it's all about efficentcy. I like to make aliaes for commands we will be using most.
```
alias rs="python manage.py runserver"
alias migrations="python manage.py makemigrations"
alias migrate="python manage.py migrate"
```
Now all you have to do to run the server is type the following
```
rs
```

## Views and Templates
Now that we have our project set up and ready to go, we have to

``` js
function simple(){
    let
}
```
``` python
def NewFunc():
    variable = "stirng"
```
``` html
<h1>New Title</h1>
```