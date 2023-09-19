""" 
Generate Test Events

This module provides a management command to generate random
event data built with factory boy and the faker libary.
"""
import random
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from events.factories import CategoryFactory, EventFactory
from events.models import Category


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.description = "Generate random categories and events"
        
        parser.add_argument(
            "-e",
            "--events",
            type=int,
            required=True,
            help="Number of events"
        )

        parser.add_argument(
            "-c",
            "--categories",
            type=int,
            required=True,
            help="Number of categories"
        )

        parser.epilog = (
            "Usage example: python manage.py create_events events=100 categories=5"
        )

    def handle(self, *args, **kwargs):

        # delete all Objects from database
        Category.objects.all().delete()

        # in kwargs.get ist das Kommandozeilen-Argument von categoreis
        number_categories = kwargs.get("categories")  # kwargs["categories"]
        number_events = kwargs.get("events")
        users = get_user_model().objects.all()
        
        # create Category
        categories = CategoryFactory.create_batch(number_categories)

        for _ in range(number_events):
            EventFactory(
                author=random.choice(users),
                category=random.choice(categories)
            )
