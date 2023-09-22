from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model

from events.factories import CategoryFactory, EventFactory


def create_user():
    user = get_user_model().objects.create_user(
        username="john",
        email="xxx@yy.de",
        password="abcd"
    )
    return user


class EventModelTests(TestCase):
    def setUp(self):
        category = CategoryFactory()
        self.event = EventFactory(
            category=category,
            author=create_user()
        )

    def test_invalid_event_name_too_short(self):
        """event name must be greater than 2 chars"""
        self.event.name = "aa"
        self.assertRaises(ValidationError, self.event.full_clean)
