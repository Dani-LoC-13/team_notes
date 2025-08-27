import sys
from app.notes import add_note

def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "add":
        title = sys.argv[2]
        body = sys.argv[3]
        add_note(title, body)
    else:
        print("Uso: python -m app.cli add \"Título\" \"Contenido\"")

if __name__ == "__main__":
    main()