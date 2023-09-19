from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model() # immer das aktuell ausgewählte User-Model


class DateMixin(models.Model):
    """
    abstrakte Klasse: erstellt selbst keine Tabelle, sondern wird von
    anderen Klassen geerbt. Diese Klassen implementieren dann die hier
    definierten Felder.
    """
    created_at = models.DateTimeField(auto_now_add=True)  # beim Anlegen aktueller Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # beim Updaten aktueller Timestamp

    class Meta:
        abstract = True


class Category(DateMixin):
    """Ein Kategorie-Model.
    
    Dient zum Beispiel zum Erstellen einer Datenbank-Tabelle.
    """
    name = models.CharField(max_length=100)  # Varchar 100
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)   # optional

    class Meta:
        ordering = ["name"]  # "-name" absteigend
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"

    def __str__(self) -> str:
        """Dunder String Methode: String-Repräsentation eines Objekts."""
        return self.name


class Event(DateMixin):

    class Group(models.IntegerChoices):
        SMALL = 2, "kleine Gruppe"
        MEDIUM = 5, "mittelgroße Gruppe"
        BIG = 10, "große Gruppe"
        UNLIMITED = 0, "ohne Limit"
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    name = models.CharField(max_length=100)  # Varchar 100
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    min_group = models.IntegerField(choices=Group.choices)  # mandatory, Dropdown im Formular
    date = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="events",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="events"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
