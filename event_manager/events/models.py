from django.db import models


class Category(models.Model):
    """Ein Kategorie-Model.
    
    Dient zum Beispiel zum Erstellen einer Datenbank-Tabelle.
    """
    name = models.CharField(max_length=100)  # Varchar 100
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)   # optional

    def __str__(self) -> str:
        """Dunder String Methode: String-Repräsentation eines Objekts."""
        return self.name


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # beim Anlegen aktueller Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # beim Updaten aktueller Timestamp
    name = models.CharField(max_length=100)  # Varchar 100
    description = models.TextField(null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="events"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
