# ACS_Walkthrough

[Master Python Intro](https://github.com/Oliver-CoderAcademy/ACS_Masterclass)

[Link to video](https://www.acs.org.au/myacs/memberarea/ict-leaders-series/play.html?videoPath=/content/dam/acs/ICT_Leaders_Vodcast/ACS%20Masterclass-%20Introduction%20to%20Python.mp4)

[Setup Django](https://github.com/Oliver-CoderAcademy/ACS_Masterclass/blob/main/django_walkthrough.md)

[Useful links](https://github.com/Oliver-CoderAcademy/ACS_Masterclass/blob/main/useful_resources.md)

[Download nvm](https://github.com/coreybutler/nvm-windows/releases)

```
C:\Users\Python310\AppData\Local\Programs\Python\Python310\Scripts
```
PIP location

```
py -m pip install virtualenv
```
Install virtualenv using pip 
```
virtualenv venv
```
create virtual environment to hold any packages in the project

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
pip install -r requirements.txt
```
Install dependencies

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
git push origin main


```
https://rapidapi.com/blog/python-django-rest-api-tutorial/

https://blog.logrocket.com/django-rest-framework-create-api/

https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

```

Create Rest API in Django