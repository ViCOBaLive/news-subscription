from django.urls import path
from .views import USSDView, IncomingSMSView


urlpatterns = [
    path('ussd/', USSDView.index, name='ussd_index'),
    path('incoming-sms/', IncomingSMSView.index, name='incomingView'),

]
