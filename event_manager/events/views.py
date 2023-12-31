from django.db import transaction, DatabaseError
from typing import Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Event
from .forms import CategoryForm, EventForm
from event_manager.utils import get_database


class UserIsAuthor(UserPassesTestMixin):
    """return True, if user is author or member of moderatoren group"""

    def test_func(self) -> bool:
        return (
            self.get_object().author == self.request.user
            # or self.request.user.groups.filter(name="moderators").exists()
        )


class ViewPermission(PermissionRequiredMixin):
    permission_required = ("events.view_event",)


class EventDeleteView(SuccessMessageMixin, UserIsAuthor, DeleteView):
    """Generische Delete-View. 

    Template: event_confirm_delete.html
    """
    model = Event
    success_message = "Event wurde erfolgreich gelöscht"
    success_url = reverse_lazy("events:events")


class EventUpdateView(SuccessMessageMixin, UserIsAuthor, UpdateView):
    model = Event
    form_class = EventForm
    # success_url = reverse_lazy("events:events")
    success_message = "Event wurde erfolgreich upgedated"


class EventCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Generische Create View. Nach dem Eintragen wird Weitergeleitet an 
    get_absolute_url im Model.

    Template: event_form.html
    """
    model = Event
    form_class = EventForm
    # success_url = reverse_lazy("events:events")
    success_message = "Event wurde erfolgreich eingetragen"

    def form_valid(self, form):
        """Wird aufgerufen, bevor es in die DB
        eingetragen wird."""
        # messages.info(self.request, "Three credits remain in your account.")
        form.instance.author = self.request.user
        return super().form_valid(form)


class EventSearchView(ListView):
    """Filtert Events nach einer Suche mit der Suchbox.

    /events/search?q=<SUCHBEGRIFF>
    """
    model = Event
    queryset = Event.objects.select_related("author", "category").all()

    def get_context_data(self, **kwargs):
        """Render-Context erweitern."""
        context = super().get_context_data(**kwargs)
        context["searched"] = self.request.GET.get("q")
        return context

    def get_queryset(self):

        q = self.request.GET.get("q")
        if not q:
            return Event.objects.none()

        qs = super().get_queryset()
        qs = qs.filter(name__contains=q)
        return qs


class EventListView(ListView):
    """Generische listview 

    events/?q=abc

    template liegt unter:
    events/event_list.html.
    object_list steht im Template zur verfügung

    """
    model = Event
    queryset = Event.objects.select_related("author", "category").all()
    paginate_by = 10
    # template_name = "events/events.html"
    # context_object_name = "events"


class EventDetailView(DetailView):
    """Generische Detailview.

    class EventDetailView(ViewPermission, DetailView). 

    template events/event_detail.html
    object steht im Template zur verfügung
    """
    model = Event


def get_data(request: HttpRequest) -> HttpResponse:
    """Diese View gibt JSON zurück.

    Die kann dann auch per JS fetch aufgerufen werden.
    """
    data = [12, 133, 34, 23, 14]

    return JsonResponse(data, safe=False)


def category_add(request: HttpRequest) -> HttpResponse:
    """
    Eine neue Kategorie eintragen.
    http://127.0.0.1/events/category/add
    """
    if request.method == "POST":
        # hier sollen die Daten in die DB eingetragen werden
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, "Category wurde erfolgreich angelegt!")
            # Weiterleiten auf gerade anlegte Kategorie
            # return redirect("events:category_detail", category.pk)
            return redirect(category)   # get_absolute_url() wird aufgerufen
            #  return redirect("events:categories") ## Weiterleiten auf Kategorieübersicht

        messages.error(request, "Category konnte nicht angelegt werden!")
    else:
        # hier soll ein leeres Formular engzeigt werden
        form = CategoryForm()

    return render(
        request,
        "events/category_add.html",
        {
            "form": form
        }
    )


def categories(request: HttpRequest) -> HttpResponse:
    """
    Übersicht aller Kategorien
    http://127.0.0.1/events/categories
    """
    # print("GET Daten:", request.GET.get("x"))
    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(
        request,
        "events/categories.html",
        context
    )


def category_detail(request: HttpRequest, pk: int):
    """
    Detailseite einer Kategorie
    http://127.0.0.1/events/category/3
    """
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404("Does not exist.")

    return render(
        request,
        "events/category_detail.html",
        {
            "category": category
        }
    )


@transaction.atomic
def test_db(request):
    try:
        result = Event.objects.all()
    except DatabaseError as e:
        print(e)
        return redirect("/")


def test(request: HttpRequest):
    """ 
    http://127.0.0.1/events/beispiel
    ein View ist ein Controller, der zwei Mindestanforderungen hat:
    - er erhält immer ein reqeust-Objekt als Argument
    - eine View MUSS immer ein Http-Response-Objekt zurückgeben
    - einzige Ausnahme: es wird eine Exception ausgelöst (zb. 404 Fehler)
    """
    d = [
        3,
        4
    ]

    return render(
        request,
        "events/render_test.html",
        {
            "test": d
        }
    )
