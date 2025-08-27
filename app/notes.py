import json
import os
from datetime import datetime

DATA_PATH = os.path.join("data", "notes.json")

def add_note(title, body):
    # Cargar notas existentes
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            notes = json.load(f)
    else:
        notes = []

    # Generar nuevo ID
    new_id = notes[-1]["id"] + 1 if notes else 1

    # Crear nota
    note = {
        "id": new_id,
        "title": title,
        "body": body,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Guardar
    notes.append(note)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)

    print(f"✅ Nota #{new_id} agregada.")
