# # marketing/views.py
# from django.http import JsonResponse
# from django.shortcuts import render
# from .facebook_service import FacebookService
# import logging

# logger = logging.getLogger(__name__)

# def list_campaigns(request):
#     service = FacebookService('your_ad_account_id')
#     try:
#         campaigns = service.get_campaigns()
#         campaign_data = [{'id': campaign['id'], 'name': campaign['name']} for campaign in campaigns]
#         return JsonResponse(campaign_data, safe=False)
#     except Exception as e:
#         logger.error(f"Error listing campaigns: {e}")
#         return JsonResponse({'error': str(e)}, status=500)

# def create_campaign(request):
#     service = FacebookService('your_ad_account_id')
#     try:
#         campaign = service.create_campaign(
#             name='Test Campaign', 
#             objective='OUTCOME_LEADS', 
#             status='PAUSED', 
#             special_ad_categories=['NONE']
#         )
#         return JsonResponse({'id': campaign['id'], 'name': campaign['name']})
#     except Exception as e:
#         logger.error(f"Error creating campaign: {e}")
#         return JsonResponse({'error': str(e)}, status=500)


from django.http import JsonResponse
from django.shortcuts import render
from .facebook_service import FacebookService
import logging

logger = logging.getLogger(__name__)

def create_facebook_ad(request):
    service = FacebookService('YOUR_AD_ACCOUNT_ID')  # Replace with actual ad account ID
    try:
        campaign = service.create_campaign(
            name='Test Campaign', 
            objective='OUTCOME_LEADS', 
            status='PAUSED', 
            special_ad_categories=['NONE']
        )
        ad_set = service.create_ad_set(
            campaign_id=campaign['id'],
            name='Test Ad Set',
            daily_budget=1000,
            start_time='2024-08-06T00:00:00-0700',
            end_time='2024-08-13T00:00:00-0700',
            targeting={'geo_locations': {'countries': ['INDIA']}}
        )
        ad_creative = service.create_ad_creative(
            page_id='YOUR_PAGE_ID',  # Replace with your Facebook Page ID
            title='Test Ad',
            body='This is a test ad',
            link='https://www.example.com'
        )
        ad = service.create_ad(
            ad_set_id=ad_set['id'],
            creative_id=ad_creative['id'],
            name='Test Ad'
        )
        return JsonResponse({'campaign_id': campaign['id'], 'ad_set_id': ad_set['id'], 'ad_id': ad['id']})
    except Exception as e:
        logger.error(f"Error creating ad: {e}")
        return JsonResponse({'error': str(e)}, status=500)
