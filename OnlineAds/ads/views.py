# marketing/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .facebook_service import FacebookService
import logging

logger = logging.getLogger(__name__)

def list_campaigns(request):
    service = FacebookService('your_ad_account_id')
    try:
        campaigns = service.get_campaigns()
        campaign_data = [{'id': campaign['id'], 'name': campaign['name']} for campaign in campaigns]
        return JsonResponse(campaign_data, safe=False)
    except Exception as e:
        logger.error(f"Error listing campaigns: {e}")
        return JsonResponse({'error': str(e)}, status=500)

def create_campaign(request):
    service = FacebookService('your_ad_account_id')
    try:
        campaign = service.create_campaign(
            name='Test Campaign', 
            objective='OUTCOME_LEADS', 
            status='PAUSED', 
            special_ad_categories=['NONE']
        )
        return JsonResponse({'id': campaign['id'], 'name': campaign['name']})
    except Exception as e:
        logger.error(f"Error creating campaign: {e}")
        return JsonResponse({'error': str(e)}, status=500)
