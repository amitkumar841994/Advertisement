from django.shortcuts import render


from django.http import JsonResponse
from django.shortcuts import render

from .facebook_service import FacebookService

def list_campaigns(request):
    service = FacebookService('your_ad_account_id')
    campaigns = service.get_campaigns()
    campaign_data = [{'id': campaign['id'], 'name': campaign['name']} for campaign in campaigns]
    return JsonResponse(campaign_data, safe=False)

def create_campaign(request):
    service = FacebookService('your_ad_account_id')
    campaign = service.create_campaign(name='Test Campaign', objective='LINK_CLICKS', status='PAUSED')
    return JsonResponse({'id': campaign['id'], 'name': campaign['name']})
