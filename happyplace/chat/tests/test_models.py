from django.test import TestCase
from chat.models import models, Message


class TestModels(TestCase):

    def setUp(self):
        self.project1 = models.objects.create(
            name='project 1',
            chat=10000
        )

        def test_project_is_assigned_slug(self):
            self.assertEquals(self.project1.slug, 'project-1')


