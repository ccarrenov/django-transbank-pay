
def allowed_hosts():
    return ['*',]


def data_bases(base_dir):
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': base_dir / 'db.sqlite3',
        }
    }