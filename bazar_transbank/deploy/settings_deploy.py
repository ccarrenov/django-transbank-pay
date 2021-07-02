import bazar_transbank.deploy.default.settings_default as dev
import bazar_transbank.deploy.prod.settings_prod as prod

PROD = 'PROD'

def debug(mode):
    if mode == PROD:
        return False       
    else:
        return True

def allowed_hosts(mode):
    if mode == PROD:
        return prod.allowed_hosts()        
    else:
        return dev.allowed_hosts()


def data_bases(mode, base_dir):
    if mode == PROD:
        return prod.data_bases(base_dir)       
    else:
        return dev.data_bases(base_dir)

def middleware(mode):

    if mode == PROD:
        return prod.middleware()  
    else:
        return dev.middleware()       