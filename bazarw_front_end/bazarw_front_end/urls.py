"""bazarw_front_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bazarw_front_end.views.home import home
from bazarw_front_end.views.cart import cart
from bazarw_front_end.views.transbankpay import commitpay, webpay_plus_create
from django.conf.urls.static import static
from django.conf import settings
from django.urls import URLPattern
urlpatterns = [
    path('', home),
    path('home/', home),
    path('cart/', cart),
    path('commit-pay/', commitpay),
    path('webpay-plus-create/', webpay_plus_create),  
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

for ulr in urlpatterns:

    print('ulr: {0}'.format(ulr.pattern))
