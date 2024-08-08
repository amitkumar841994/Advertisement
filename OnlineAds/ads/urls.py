# marketing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('campaigns/', views.list_campaigns, name='list_campaigns'),
    # path('campaigns/create/', views.create_campaign, name='create_campaign')
    path('create/ads/', views.create_facebook_ad, name='create_campaign')
]
