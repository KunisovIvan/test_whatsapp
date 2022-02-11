from django.core.management.base import BaseCommand

from whatsapp_app.models import Chats
from whatsapp_app.whatsapp import WhatsAppIntegration


class Command(BaseCommand):
    help = 'Получает статус чата'

    def handle(self, *args, **options):
        whatsapp_integration = WhatsAppIntegration()
        chat = Chats.objects.all().latest('pk')
        whatsapp_integration.work_with_chat(id=chat.external_id, method='status', token=chat.token, full=1,
                                            requests_method='get')
