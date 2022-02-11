from typing import Optional

import requests


class WhatsAppIntegration():
    """Класс для работы с сервисом интеграции с WhatsApp."""

    base_url = 'https://dev.wapp.im/v3/'
    get_new_chat_url = 'chat/spare'

    X_TASKTEST_TOKEN = 'f62cdf1e83bc324ba23aee3b113c6249'

    def get_new_chat(self, crm: str, domain: str):
        """Получает новый чат"""

        url = self.base_url + self.get_new_chat_url
        params = {'crm': crm, 'domain': domain}
        headers = {'X-Tasktest-Token': self.X_TASKTEST_TOKEN}
        response = requests.get(url=url, params=params, headers=headers)
        return response

    def work_with_chat(self, id: int, method: str, token: str, requests_method: str,
                       full: Optional[int] = None, json_for_post: Optional[dict] = None):
        """Работает с чатом по указанному методу"""

        response = {}
        method_url = f'instance{id}/{method}'
        url = self.base_url + method_url
        params = {'full': full, 'token': token}
        headers = {'X-Tasktest-Token': self.X_TASKTEST_TOKEN}
        if requests_method == 'get':
            response = requests.get(url=url, params=params, headers=headers)
        if requests_method == 'post':
            response = requests.post(url=url, params=params, headers=headers, json=json_for_post)
        return response
