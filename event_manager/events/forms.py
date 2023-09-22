from django import forms
from .models import Category, Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
            "tags": forms.CheckboxSelectMultiple()

        }


class EventUpdateForm(EventForm):
    """Eigenes Formular für Update Aktion."""
    class Meta(EventForm.Meta):
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    """erstellt auf Basis des Models ein Formular.
    """
    class Meta:
        model = Category
        fields = "__all__"  # ["name", "description"]
