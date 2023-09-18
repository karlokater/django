from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


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
