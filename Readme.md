# Starting a simple Django site

## Setting up the virtual env
with python we can setup a virtual env so its easy to migrate to other systems/hosts this is standard practice.

* Commands may change on windows i use a linux system

```bash
python -m venv .venv
```

As you can see i prepend my venv directory with a . this hides it from filesystems by default.

Load the virtual enviroment.

```bash
source .venv/bon/activate
```
Now we have virtual enviroment we need to install Django

```bash
pip install Django
```
To have an easy install on other hosts we will pipe requirments to a file

```bash
pip freeze > requirments.txt
```

Now make a .gitignore file and add the virtual enviroment so we dont upload this everytime.

```cmd 
touch .gitignore
cat >> .gitignore << EOF .venv EOF
```

Now we have a simeple python enviroment with django installed so let's setup a Django site.

## Setup Django 

So i setup Django to work with REST and a frontend but this is the best way no matter how you use Django.

```bash
django-admin startproject config .
```
* Note i have named the core project config this is because this is how i use the core we will make Apps later to have a more module site. Also notice the appending . this will install manage.py in the root Dir.

As you can see after running this cmd you have a new directory and file this is our core project is you want to see it running live in the browser you can run it with.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Now visit http://127.0.0.1:8000/ in your browser and you will see your project live. to stop the server use Ctrl + C in the terminal.

## Making our first app.
I'm going to make a site for dog training so it will be called K9School

```bash 
python manage.py startapp k9School
```
As you can see you now have a new Dir with your sites name.

make a new file in this Dir called urls.py these urls will linkup to the views in this dir and the urls.py in the config Dir will link to this urls.py

```bash
touch urls.py
```
Now we have a way to link to config urls to the k9School urls lets make a simple view to test.

Open k9School/views.py

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("If you see this text the view is working")
```

Now open K9School/urls.py to add the view.

```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

as you can see we are linking our index view to our url path in urls.py now we need to link this to our core config urls.py

Open config/urls.py

```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('k9school/', include('K9School.urls')),
    path('admin/', admin.site.urls),
]
```
As you can see we have added the k9school urls.py to our main app now lets migrate and run the server to see our view.

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Now when you load http://127.0.0.1:8000/ in your browser you will notice you get an error this is because we dont have a root view yet, but as you can see in the error if you navigate to http://127.0.0.1:8000/k9school you will see the view we created.

Now we have a Django project we can work on i would suggest making an superuser for the admin interface. if you look at the other available path in our error http://127.0.0.1:8000/admin you will see we have an full CMS built by django. 