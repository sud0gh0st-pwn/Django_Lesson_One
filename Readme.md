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

This will be where we build out main site backend as for the frontend we can add a JS frontend later but for now i think to keep things simple keep it to django alone.


# I will stop here and call this lesson 1, Ask me on whatsapp if you have any questions and let me know when you want to continue.