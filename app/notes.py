import json
import os
from datetime import datetime

DATA_PATH = os.path.join("data", "notes.json")

def add_note(title, body):
    # Cargar notas existentes con manejo de errores
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()
            notes = json.loads(content) if content else []
    except (FileNotFoundError, json.JSONDecodeError):
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

def list_notes():
    if not os.path.exists(DATA_PATH):
        print("⚠️ No hay notas registradas.")
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        notes = json.load(f)

    for note in notes:
        print(f"[{note['id']}] {note['title']} ({note['created_at']})")
    return notes

def find_notes(query):
    if not os.path.exists(DATA_PATH):
        print("⚠️ No hay notas registradas.")
        return []

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        notes = json.load(f)

    resultados = [
        note for note in notes
        if query.lower() in note["title"].lower() or query.lower() in note["body"].lower()
    ]

    if resultados:
        for note in resultados:
            print(f"[{note['id']}] {note['title']} → {note['body']}")
    else:
        print(f"🔍 No se encontraron notas que coincidan con: '{query}'")

    return resultados
