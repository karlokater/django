from django import forms 
from .models import Category, Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            ),
        }


class CategoryForm(forms.ModelForm):
    """erstellt auf Basis des Models ein Formular.
    """
    class Meta:
        model = Category
        fields = "__all__"  # ["name", "description"]
