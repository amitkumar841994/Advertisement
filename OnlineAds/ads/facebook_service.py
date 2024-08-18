# # marketing/facebook_service.py
# from facebook_business.api import FacebookAdsApi
# from facebook_business.adobjects.adaccount import AdAccount
# from facebook_business.adobjects.campaign import Campaign
# from django.conf import settings

# FacebookAdsApi.init(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET, settings.FACEBOOK_ACCESS_TOKEN)

# class FacebookService:
#     def __init__(self, ad_account_id):
#         self.ad_account = AdAccount(f'act_{886992382482858}')

#     def get_campaigns(self):
#         campaigns = self.ad_account.get_campaigns(fields=[Campaign.Field.id, Campaign.Field.name])
#         return campaigns

#     def create_campaign(self, name, objective, status, special_ad_categories=['NONE']):
#         campaign = Campaign(parent_id=self.ad_account.get_id_assured())
#         campaign[Campaign.Field.name] = name
#         campaign[Campaign.Field.objective] = objective
#         campaign[Campaign.Field.status] = status
#         campaign.remote_create(params={
#             'status': status,
#             'special_ad_categories': special_ad_categories
#         })
#         return campaign

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from django.conf import settings

FacebookAdsApi.init(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET, settings.FACEBOOK_ACCESS_TOKEN)

class FacebookService:
    def __init__(self, ad_account_id):
        self.ad_account = AdAccount(f'act_{886992382482858}')

    def create_campaign(self, name, objective, status, special_ad_categories=['NONE']):
        campaign = Campaign(parent_id=self.ad_account.get_id_assured())
        campaign[Campaign.Field.name] = name
        campaign[Campaign.Field.objective] = objective
        campaign[Campaign.Field.status] = status
        campaign.remote_create(params={
            'status': status,
            'special_ad_categories': special_ad_categories
        })
        return campaign

    def create_ad_set(self, campaign_id, name, daily_budget, start_time, end_time, targeting):
        ad_set = AdSet(parent_id=self.ad_account.get_id_assured())
        ad_set.update({
            AdSet.Field.name: name,
            AdSet.Field.campaign_id: campaign_id,
            AdSet.Field.daily_budget: daily_budget,
            AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
            AdSet.Field.optimization_goal: AdSet.OptimizationGoal.link_clicks,
            AdSet.Field.bid_amount: 100,
            AdSet.Field.targeting: targeting,
            AdSet.Field.start_time: start_time,
            AdSet.Field.end_time: end_time,
            AdSet.Field.status: AdSet.Status.active,
        })
        ad_set.remote_create()
        return ad_set

    def create_ad_creative(self, page_id, title, body, link,enroll_status):
        creative = AdCreative(parent_id=self.ad_account.get_id_assured())
        creative[AdCreative.Field.name] = title
        creative[AdCreative.Field.name]=enroll_status
        creative[AdCreative.Field.object_story_spec] = {
            'page_id': page_id,
            
            'link_data': {
                'call_to_action': {
                    'type': 'INTERESTED',
                    'value': {
                        'link': link
                    }
                },
                'link': link,
                'message': body,
                'name': title,
            },
            
        },
 
        creative.remote_create()
        return creative

    def create_ad(self, ad_set_id, creative_id, name):
        ad = Ad(parent_id=self.ad_account.get_id_assured())
        ad.update({
            Ad.Field.name: name,
            Ad.Field.adset_id: ad_set_id,
            Ad.Field.creative: {
                'creative_id': creative_id,
            },
            Ad.Field.status: Ad.Status.active,
        })
        ad.remote_create()
        print(">>>>>>>>>>>>>",ad)
        return ad
