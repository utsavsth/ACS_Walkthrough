# ACS_Walkthrough
```
https://github.com/Oliver-CoderAcademy/ACS_Masterclass
```
```
virtualenv venv
```
create virtual environment to hold packages

```
venv/Scripts/activate
```
activate the virtual environment into the folder

```
pip install django
```
install django in our environment

```
pip install gunicorn
```
Upload the website

```
pip freeze > requirements.txt
```
records the packages that we've installed in requirement.txt file

```
django-admin startproject <project_name>
```
create django project folder containing boilerplate

```
py manage.py startapp <app_name>
```

```
py manage.py migrate
```

```
py manage.py runserver
```

git add .
git commit -m "message"
