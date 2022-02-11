from django.db import models


class Chats(models.Model):
    """Модель, хранящая информацию о чатах."""

    external_id = models.PositiveIntegerField('внешний id', blank=True, null=True)
    instanceId = models.CharField('instanceId', max_length=255, blank=True, null=True)
    token = models.CharField('Токен', max_length=255, blank=True, null=True)
    chat_id = models.CharField('id чата', max_length=255, blank=True, null=True)
    md = models.PositiveIntegerField('md', blank=True, null=True)
    chat_token = models.CharField('chat_token', max_length=255, blank=True, null=True)
    chat_key = models.CharField('chat_key', max_length=255, blank=True, null=True)
    apikey = models.CharField('apikey', max_length=255, blank=True, null=True)
    date_add = models.CharField('date_add', max_length=255, blank=True, null=True)
    date_trial = models.CharField('date_trial', max_length=255, blank=True, null=True)
    date_pay = models.CharField('date_pay', max_length=255, blank=True, null=True)
    date_subscription = models.CharField('date_subscription', max_length=255, blank=True, null=True)
    phone = models.CharField('phone', max_length=255, blank=True, null=True)
    name = models.CharField('name', max_length=255, blank=True, null=True)
    platform = models.CharField('platform', max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField('status', blank=True, null=True)
    is_premium = models.PositiveIntegerField('is_premium', blank=True, null=True)

    def __str__(self):
        return f'Чат[{self.external_id}]'

    class Meta:
        verbose_name = 'Информация о чате'
        verbose_name_plural = 'Информация о чатах'


class Contacts(models.Model):
    """Модель, хранящая информацию о контакте."""

    phone_number = models.CharField('Номер телефона', max_length=255, blank=True, null=True)
    name = models.CharField('Имя', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Информация о контакте'
        verbose_name_plural = 'Информация о контактах'

