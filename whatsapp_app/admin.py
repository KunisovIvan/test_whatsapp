from django.contrib import admin

from whatsapp_app.models import Chats


class ChatsAdmin(admin.ModelAdmin):
    """Выводить модель InstagramAccount"""

    list_display = ['external_id', 'token']


admin.site.register(Chats, ChatsAdmin)

