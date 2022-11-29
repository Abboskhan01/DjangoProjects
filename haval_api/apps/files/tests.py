import tempfile

from PIL import Image
from django.urls import reverse
from rest_framework import status

from shared.rest_framework.tests import BaseTest


class FileTest(BaseTest):
    list_url = 'files:file-list'
    detail_url = 'files:file-detail'

    def test_create(self):
        image = Image.new('RGB', (100, 100), 'white')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg', mode='w')
        image.save(tmp_file)

        with open(tmp_file.name, 'rb') as data:
            response = self.client.post(reverse(self.list_url), dict(file=data), format='multipart')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data['id']

    def test_create_data_fail(self):
        url = reverse(self.list_url)

        response = self.client.post(url, {}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
