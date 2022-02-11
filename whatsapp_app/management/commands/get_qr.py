from django.core.management.base import BaseCommand

from whatsapp_app.models import Chats
from whatsapp_app.whatsapp import WhatsAppIntegration


class Command(BaseCommand):
    help = 'Сохраняет qr виде html'

    def handle(self, *args, **options):
        whatsapp_integration = WhatsAppIntegration()
        chat = Chats.objects.all().latest('pk')
        response = whatsapp_integration.work_with_chat(id=chat.external_id, method='qr_code', token=chat.token,
                                                       requests_method='get')
        with open('index.html', 'wb') as f:
            f.write(response.content)
