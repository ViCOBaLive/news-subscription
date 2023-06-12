from django.urls import path,include
from .views import *

urlpatterns = [
    path("ussd/", index,name="ussd_index" ),
    path("", index,name="ussd_index" ),
    path("incoming-sms/", incomingSMS,name="ussd_index" ),


]
