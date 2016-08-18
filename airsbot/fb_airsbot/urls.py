from django.conf.urls import include, url
from .views import AirsBotView
import os, binascii

#print binascii.hexlify(os.urandom(10))

urlpatterns = [url(r'^22517939a260011c5e13f9a9180211269172c8981024106968/?$', AirsBotView.as_view())]
