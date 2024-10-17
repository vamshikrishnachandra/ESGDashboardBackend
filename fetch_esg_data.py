import requests
from django.core.management.base import BaseCommand
from esg.models import ESGData

class Command(BaseCommand):
    help = 'Fetch real-time ESG data'

    def handle(self, *args, **kwargs):
        response = requests.get('YOUR_ESG_API_URL')
        data = response.json()
        for item in data:
            ESGData.objects.update_or_create(
                company_name=item['company_name'],
                defaults={
                    'environmental_score': item['environmental_score'],
                    'social_score': item['social_score'],
                    'governance_score': item['governance_score'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched ESG data'))
