# INSTALL VIRTUALENV
```terminal
pip install virtualenv
```

# CREATE VIRTUAL ENV development
```terminal
virtualenv develpoment
```

# LOAD VIRTUALENV development
```terminal
source develpoment/bin/activate
```

# INSTALL DJANGO, RESTFRAMEWORK, MYSQLCLIENT IN VIRTUAL ENV JSONSCHEMA
```terminal
pip install Django djangorestframework transbank-sdk
```

# CREATE PROJECT bazarws
```terminal
django-admin startproject bazarw_front_end
```

# LOAD VIRTUALENV development IN VSCODE
```terminal
source ../develpoment/bin/activate
```

# CONFIG setting.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bazarw_front_end',
]
```

#  GENERATE requirements.txt
```terminal
pip freeze > requirements.txt
```

# INSTALL FROM requirements.txt FILE
```terminal
pip install -r requirements.txt
```

# MIGRATION SQLITE
python manage.py makemigrations
python manage.py migrate


# PROD CONFIG

Add environment DEPLOY_MODE

```terminal
export DEPLOY_MODE=PROD
```

# DEPLOY IN MODE PROD

Execute command for generate staticfiles

```terminal
python bazarw_front_end/manage.py collectstatic --noinput
```

Execute command for deploy local server

```terminal
python bazarw_front_end/manage.py runserver
```
