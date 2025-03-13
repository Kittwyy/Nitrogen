import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
from ttkthemes import ThemedTk
from datetime import datetime

def get_autobahn_status(autobahn_id):
    """Ruft Statusinformationen für eine bestimmte Autobahn ab."""
    url = f"https://verkehr.autobahn.de/o/autobahn/{autobahn_id}/services/warning"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def format_time(time_str):
    """Formatiert Zeitstrings."""
    if time_str:
        try:
            dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
            return dt.strftime('%d.%m.%Y %H:%M:%S')
        except ValueError:
            return time_str
    return "Unbekannt"

def show_autobahn_status():
    """Zeigt Statusinformationen im Textfeld an."""
    autobahn_id = autobahn_combobox.get()
    status_data = get_autobahn_status(autobahn_id)
    status_text.delete(1.0, tk.END)

    if "error" in status_data:
        status_text.insert(tk.END, f"Fehler: {status_data['error']}")
        return

    if "warning" in status_data and status_data["warning"]:
        status_text.insert(tk.END, f"{'='*40}\n")
        status_text.insert(tk.END, f"  Warnungen für {autobahn_id}\n")
        status_text.insert(tk.END, f"{'='*40}\n")
        warnings = status_data["warning"]
        warnings.sort(key=lambda x: len(x.get("description", "")), reverse=True)

        for warning in warnings:
            title = warning.get("title", "Kein Titel")
            description = warning.get("description", "Keine Beschreibung")
            urgency = warning.get("urgency", "minor")
            extent = warning.get("extent", "Unbekannt")
            direction = warning.get("direction", "Unbekannt")
            time_str = warning.get("time", "Unbekannt")

            formatted_time = format_time(time_str)

            if urgency == "major":
                status_text.insert(tk.END, f"!!! WICHTIG !!! {title}\n")
                status_text.insert(tk.END, f"  Beschreibung: {description}\n")
                status_text.insert(tk.END, f"  Abschnitt: {extent}\n")
                status_text.insert(tk.END, f"  Richtung: {direction}\n")
                status_text.insert(tk.END, f"  Zeit: {formatted_time}\n")
            else:
                status_text.insert(tk.END, f"  {title}\n")
                status_text.insert(tk.END, f"    Beschreibung: {description}\n")
                status_text.insert(tk.END, f"    Abschnitt: {extent}\n")
                status_text.insert(tk.END, f"    Richtung: {direction}\n")
                status_text.insert(tk.END, f"    Zeit: {formatted_time}\n")
        status_text.insert(tk.END, f"{'-'*40}\n")
    else:
        status_text.insert(tk.END, f"{'='*40}\n")
        status_text.insert(tk.END, f"  Keine Warnungen für {autobahn_id}\n")
        status_text.insert(tk.END, f"{'='*40}\n")

def show_manual():
    """Zeigt das Autobahn-ID-Handbuch in einem Popup-Fenster an."""
    manual_text = """
    Autobahn-ID-Handbuch:
    A1: Hamburg - Saarbrücken
    A2: Oberhausen - Berlin
    A3: Niederlande - Österreich
    A4: Niederlande - Polen
    A5: Hattenbacher Dreieck - Weil am Rhein
    A6: Saarbrücken - Waidhaus
    A7: Flensburg - Füssen
    A8: Luxemburg - Österreich
    A9: Berlin - München
    A10: Berliner Ring
    ... (Weitere IDs können hinzugefügt werden)
    """
    messagebox.showinfo("Autobahn-ID-Handbuch", manual_text)

# GUI-Einrichtung
window = ThemedTk(theme="adapta")
window.title("Autobahn Status")

# Flexible Fenstergröße
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

# Style-Einstellungen
style = ttk.Style()
style.configure("TButton", padding=5, font=("TkDefaultFont", 12))
style.configure("TLabel", padding=5, font=("TkDefaultFont", 12))
style.configure("TCombobox", padding=5, font=("TkDefaultFont", 12))

# Autobahn-ID-Auswahl (Combobox)
autobahn_label = ttk.Label(window, text="Autobahn:")
autobahn_label.grid(row=0, column=0, pady=10)

autobahn_ids = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
autobahn_combobox = ttk.Combobox(window, values=autobahn_ids, state="readonly")
autobahn_combobox.grid(row=0, column=1, pady=10)
if autobahn_ids:
    autobahn_combobox.current(0)

# Statusanzeige
status_text = scrolledtext.ScrolledText(window, width=70, height=25)
status_text.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

# Handbuch-Button
manual_button = ttk.Button(window, text="Handbuch", command=show_manual)
manual_button.grid(row=2, column=0, pady=10)

# Anzeigen-Button
show_button = ttk.Button(window, text="Anzeigen", command=show_autobahn_status)
show_button.grid(row=2, column=1, pady=10)

window.mainloop()