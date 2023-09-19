from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .models import Category, Event


def categories(request: HttpRequest) -> HttpResponse:
    """
    Übersicht aller Kategorien
    http://127.0.0.1/events/categories
    """
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
    


def test(request: HttpRequest):
    """ 
    http://127.0.0.1/ereignisse/beispiel
    ein View ist ein Controller, der zwei Mindestanforderungen hat:
    - er erhält immer ein reqeust-Objekt als Argument
    - eine View MUSS immer ein Http-Response-Objekt zurückgeben
    - einzige Ausnahme: es wird eine Exception ausgelöst (zb. 404 Fehler)
    """
    print("Request-Methode:", request.method)
    print("Request-User:", request.user)
    obj = HttpResponse("hallo Welt")
    return obj
