### Create Virtual Environment
```
$python3 -m venv djangoblog-venv
$cp -r djangoblog/* djangoblog-venv/
$cd djangoblog-venv/bin/
$source activate
$(djangoblog-venv) user@computer djangoblog-venv %
$deactivate
```
### Install Requirements
If conflicting remove package in requirements.txt and install using $pip install <package_name_only>
```
$pip install -r requirements.txt #Install in Venv and in Main Project
```
### List Requirements
```
$pip freeze > requirements.txt
```
### Collect Static
```
$python manage.py collectstatic
```
### Check Deployment
```
$python manage.py check --deploy
```
### Install Django Libraries
```
$pip install django
$pip install channels
$pip install django-jazzmin
$pip install django-import-export
$pip install django-tinymce
$pip install django-debug-toolbar
$pip install pillow
$pip install whitenoise
$pip install django-auto-logout
```
### Run in Local Server
Change SSL REDIRECT in djangoblog/settings.py
```
SECURE_SSL_REDIRECT = False
```
```
$cd djangoblog-venv/
$python manage.py runserver <custom_non_conflict_port i.e. 8000>
```
```
http://127.0.0.1:8000/
```
