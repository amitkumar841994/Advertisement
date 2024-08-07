# marketing/facebook_service.py
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from django.conf import settings

FacebookAdsApi.init(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET, settings.FACEBOOK_ACCESS_TOKEN)

class FacebookService:
    def __init__(self, ad_account_id):
        self.ad_account = AdAccount(f'act_{886992382482858}')

    def get_campaigns(self):
        campaigns = self.ad_account.get_campaigns(fields=[Campaign.Field.id, Campaign.Field.name])
        return campaigns

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
