from django.core.management.base import BaseCommand

from whatsapp_app.models import Chats
from whatsapp_app.whatsapp import WhatsAppIntegration


class Command(BaseCommand):
    help = 'Отправляет сообщение'

    def handle(self, *args, **options):
        whatsapp_integration = WhatsAppIntegration()
        chat = Chats.objects.all().latest('pk')
        json_for_post = {
            'chatId': f'{chat.date_add}@c.us',
            'body': 'Тестовое сообщение2',
            'quotedMsgId': '',
            'sendSeen': '1',
            'typeMsg': 'text',
        }

        whatsapp_integration.work_with_chat(id=chat.external_id, method='sendMessage', token=chat.token,
                                            requests_method='post', json_for_post=json_for_post)
