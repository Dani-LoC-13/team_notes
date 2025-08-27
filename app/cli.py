import sys
from app.notes import add_note, list_notes, find_notes


def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1]

        if command == "add" and len(sys.argv) >= 4:
            title = sys.argv[2]
            body = sys.argv[3]
            add_note(title, body)

        elif command == "list":
            list_notes()

        elif command == "search" and len(sys.argv) >= 3:
            query = sys.argv[2]
            find_notes(query)

        else:
            print("⚠️ Comando inválido o argumentos faltantes.")
    else:
        print("Uso:")
        print("  python -m app.cli add \"Título\" \"Contenido\"")
        print("  python -m app.cli list")
        print("  python -m app.cli search \"palabra\"")

if __name__ == "__main__":
    main()


def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1]

        if command == "add" and len(sys.argv) >= 4:
            title = sys.argv[2]
            body = sys.argv[3]
            add_note(title, body)

        elif command == "list":
            list_notes()

        elif command == "search" and len(sys.argv) >= 3:
            query = sys.argv[2]
            find_notes(query)

        else:
            print("⚠️ Comando inválido o argumentos faltantes.")
    else:
        print("Uso:")
        print("  python -m app.cli add \"Título\" \"Contenido\"")
        print("  python -m app.cli list")
        print("  python -m app.cli search \"palabra\"")

if __name__ == "__main__":
    main()
