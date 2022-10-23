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
I will add this after we speak to see if you want a js frontend on the site.
