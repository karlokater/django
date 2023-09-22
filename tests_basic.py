""" 
Wie funktioniert Unit-Testing (Modultest): Testet eine Funktionalität

"""


def summe(a, b):
    return a + b


def test_summe():
    assert summe(3, 4) == 7  # Behauptung
    assert summe(0, -1) == -1, "0 und -1 ist -1"  # Behauptung


test_summe()
