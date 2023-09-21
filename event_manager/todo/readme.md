# Todo Liste

## Projektvision (Zielsetzung)
Was ist das Ziel des Projekts? Wer sind die Stakeholder (Beteiligten)? 
Wo soll das Projekt laufen, techn. Umgebung.

Beteiligte sind Admin-User und auth. User. 

## Beschreibung der Aktion
- User soll Todos anlegen können
- User soll Todos löschen kann
- User soll Todos Übersicht einsehen
- User soll Todo Detailseite einsehen

## Use Case Diagramm schreiben / zeichnen 
Wer sind die Akteure? Welche Aktionen dürfen/können sie 
ausführen? Welche Aktionen beinflussen andere Funktionen?

zb. Lucid-Chart
https://www.lucidchart.com


## Datenmodell
- UML Klassendiagramme
- Entity Relationship Diagramm (ERD) (bei größeren Projekten)


## Django mögliche Vorgehensweise
- mit den Views anfangen (nur Skizze ohne Return oder DB-Operation) (views.py)
- dann dazu die Urls anlegen (urls.py) und dir urls.py in den Projekturls inkludieren
- die Models aus dem Datenmodell ableiten (UML-Klassendiagramm oder ERD), models.py
- nicht vergessen, die App in den settings.py registieren.
- Templates für die Aktionen anlegen (entsprechender der Views)
- Views implementieren mit DB-Zugriff etc



