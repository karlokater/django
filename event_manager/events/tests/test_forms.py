from datetime import timedelta
from django.utils import timezone

from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from events.factories import CategoryFactory, EventFactory
from events.models import Category, Event


def create_user():
    user = get_user_model().objects.create_user(
        username="john",
        email="xxx@yy.de",
        password="abcd"
    )
    return user


class EventFormTest(TestCase):
    """Testet das Event-Formular."""

    def setUp(self):
        """Wird VOR jedem Test ausgeführt!"""
        self.user = create_user()
        self.client = Client()  # der "Browser"
        self.client.force_login(self.user)
        self.category = CategoryFactory()
        self.payload = {
            "name": "Testname für Event",
            "description": "eine Testbeschreibung",
            "sub_title": "Test-Subtitle",
            "min_group": 10,
            "date": timezone.now() + timedelta(days=2),
            "category": self.category.pk,
        }

    def test_name_too_short(self):
        """Prüfen, ob ein Objekt NICHT in die DB eingetragen wird, 
        wenn der name kleiner als 3 Zeichen ist."""
        ...

    def test_legal_event_inserted(self):
        """Prüfen, ob ein valider Event eingetragen wurde.
        Methode muss mit test_ anfangen
        """
        response = self.client.post(
            reverse("events:event_create"),
            self.payload
        )

        self.assertEqual(response.status_code, 302)
        event_exists = Event.objects.filter(name=self.payload["name"]).exists()
        self.assertTrue(event_exists)
