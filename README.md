# Autobahn Status Anwendung

Diese Python-Anwendung ruft Statusinformationen von der Autobahn-Website ab und zeigt sie in einem benutzerfreundlichen GUI an.

**Hinweis:** Dieses Projekt dient ausschließlich Bildungszwecken.

## Funktionen

* **GUI:**
    * Benutzerfreundliches GUI mit `tkinter` und `ttkthemes`.
    * Auswahl der Autobahn-ID über eine Combobox.
    * Anzeige der Statusinformationen in einem scrollbaren Textfeld.
    * "Handbuch"-Button, der eine Liste der Autobahn-IDs und ihrer Beschreibungen anzeigt.
* **Statusanzeige:**
    * Formatierte Anzeige von Warnungen mit Titel, Beschreibung, Abschnitt, Richtung und Zeit.
    * Hervorhebung wichtiger Warnungen (urgency "major").
    * Farbliche Kennzeichnung der Warnungen basierend auf ihrer Wichtigkeit.
* **API-Daten:**
    * Abruf von Statusinformationen von der Autobahn-API.
* **Benutzer-Interaktion**:
    * Ein Button, der, wenn er gedrückt wird, die Informationen aktualisiert.
    * Ein Button, der, wenn er gedrückt wird, eine Hilfsliste anzeigt.

## Voraussetzungen

* Python 3.x
* Bibliotheken: `tkinter`, `requests`, `ttkthemes`

## Installation

1.  Stellen Sie sicher, dass Python 3.x installiert ist.
2.  Installieren Sie die erforderlichen Bibliotheken:

    ```bash
    pip install requests ttkthemes
    ```

3.  Laden Sie das Skript `main.py` herunter oder klonen Sie das Repository.

## Verwendung

1.  Führen Sie das Skript aus:

    ```bash
    main.py
    ```

2.  Wählen Sie eine Autobahn-ID aus der Combobox aus.
3.  Klicken Sie auf den Button "Anzeigen", um die Statusinformationen anzuzeigen.
4.  Klicken Sie auf den Button "Handbuch", um eine Liste der Autobahn-IDs und ihrer Beschreibungen anzuzeigen.
5.  Das Fenster kann beliebig in der Größe verändert werden.

## Bekannte Probleme

* Die Autobahn-API liefert keine detaillierten Geodaten für betroffene Abschnitte. Daher können Autobahnabschnitte auf der Karte nicht genau markiert werden.
* Die API kann inkonsistent sein, was zu Fehlern beim Abrufen von Daten führen kann.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.

## Zusätzlicher Hinweis

Diese Anwendung wurde erstellt, um die Nutzung von API-Daten und die Erstellung von GUI-Anwendungen zu demonstrieren. Sie ist ausschließlich für Bildungszwecke bestimmt.
