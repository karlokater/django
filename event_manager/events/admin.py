from django.contrib import admin
from django.db.models import QuerySet
from .models import Event, Category, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sub_title", "num_of_events")
    search_fields = ("name",)
    list_display_links = ("id", "name")

    @admin.display(description="Anzahl Ereignisse")
    def num_of_events(self, obj: Category):
        return obj.events.count()  # events => related manager


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "sub_title", "category", "is_active")
    list_display_link = ("id", "name")
    search_fields = ("name", "category__name")
    actions = ("make_inactive", "make_active")

    @admin.action(description="Setze Events inaktiv")
    def make_inactive(self, request, queryset: QuerySet):
        """Setze alle selektierten Einträge auf inkativ.

        queryset = alle aktuell ausgewählten Datensätze
        """
        queryset.update(is_active=False)

    @admin.action(description="Setze Events aktiv")
    def make_active(self, request, queryset: QuerySet):
        queryset.update(is_active=True)
