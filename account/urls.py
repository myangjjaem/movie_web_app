from django.urls import path
import account.views

urlpatterns = [
    path('join/', account.views.join, name='join'),
    path('dojoin/', account.views.dojoin, name='dojoin'),
]