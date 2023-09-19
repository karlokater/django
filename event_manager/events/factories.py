import factory
import random
from datetime import timedelta
from django.utils import timezone

from .models import Category, Event


categories = [
    "Sports",
    "Talk",
    "Cooking",
    "Freetime",
    "Hiking",
    "Movies",
    "Travelling",
    "Science",
    "Arts",
    "Pets",
    "Music",
    "Wellness",
]


class EventFactory(factory.django.DjangoModelFactory):
    """
    Hinweis: Wenn EventFactory aufgerufen wird, muss
    author und company im Konstruktor übergeben werden

    zb. 
    EventFactory(author=user, category=sport)
    """
    class Meta:
        model = Event
    
    name = factory.Faker("sentence")
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    min_group = factory.LazyAttribute(
        lambda _: random.choice(list(Event.Group))
    )
    date = factory.Faker(
        "date_time_between",
        start_date=timezone.now() + timedelta(days=1),
        end_date=timezone.now() + timedelta(days=60),
        tzinfo=timezone.get_current_timezone()
    )



class CategoryFactory(factory.django.DjangoModelFactory):
    """erstellt eine Kategorie aus einer vorgegebenen Liste."""

    class Meta:
        model = Category
    
    name = factory.Iterator(categories)
    sub_title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
