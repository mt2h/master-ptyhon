
# Proyecto Django

## Commands

```bash
#create project django
django-admin startproject ProyectoDjango
cd ProyectoDjango/
python3 manage.py runserver 0.0.0.0:8080

#create main app
python3 manage.py startapp mainapp

#create apps
python manage.py startapp page
python manage.py sqlmigrate pages 0001 #generate code sql to deploy on database
python manage.py migrate

#admin
python manage.py createsuperuser #admin | admin

pip install django-ckeditor==6.1.0
python -m pip install Pillow

python manage.py makemigrations #add new file migration 0002
python manage.py sqlmigrate pages 0002 #view as to migration
python manage.py migrate #apply migration
```

La carpeta template, media, static dentro de una app y el urls.py, processor.py se crean a mano