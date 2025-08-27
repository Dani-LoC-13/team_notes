import json
import os

DATA_PATH = os.path.join("data", "notes.json")

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
