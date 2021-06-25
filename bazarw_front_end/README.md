# INSTALL VIRTUALENV

pip install virtualenv

# CREATE VIRTUAL ENV development

virtualenv develpoment

# LOAD VIRTUALENV development

source develpoment/bin/activate

# INSTALL DJANGO, RESTFRAMEWORK, MYSQLCLIENT IN VIRTUAL ENV JSONSCHEMA

pip install Django djangorestframework transbank-sdk

# CREATE PROJECT bazarws

django-admin startproject bazarw_front_end

# LOAD VIRTUALENV development IN VSCODE

source ../develpoment/bin/activate

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

pip freeze > requirements.txt

# INSTALL FROM requirements.txt FILE

pip install -r requirements.txt
