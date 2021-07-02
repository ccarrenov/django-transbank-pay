def allowed_hosts():
    return []


def data_bases(base_dir):
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': base_dir / 'db.sqlite3',
        }
    }

def middleware():

    return [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]    