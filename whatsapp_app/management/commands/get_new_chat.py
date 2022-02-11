from django.core.management.base import BaseCommand

from whatsapp_app.models import Chats
from whatsapp_app.whatsapp import WhatsAppIntegration


class Command(BaseCommand):
    help = 'Получает новый чат'

    def handle(self, *args, **options):
        whatsapp_integration = WhatsAppIntegration()
        response = whatsapp_integration.get_new_chat('TEST', 'test')
        data = response.json()
        if not data.get('error_code'):
            Chats.objects.create(
                external_id=data.get('id'),
                instanceId=data.get('instanceId'),
                token=data.get('token'),
                chat_id=data.get('chat_id'),
                md=data.get('md'),
                chat_token=data.get('chat_token'),
                chat_key=data.get('chat_key'),
                apikey=data.get('apikey'),
                date_add=data.get('date_add'),
                date_trial=data.get('date_trial'),
                date_pay=data.get('date_pay'),
                date_subscription=data.get('date_subscription'),
                phone=data.get('phone'),
                name=data.get('name'),
                platform=data.get('platform'),
                status=data.get('status'),
                is_premium=data.get('is_premium'),
            )


