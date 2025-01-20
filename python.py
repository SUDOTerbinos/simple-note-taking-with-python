import os

NOTES_FILE = "notes.txt"

def show_menu():
    print("\nSimple Note-Taking App")
    print("1. Create a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

def create_note():
    note = input("Enter your note: ")
    with open(NOTES_FILE, "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = file.readlines()
            if notes:
                print("\nYour Notes:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
            else:
                print("No notes found.")
    else:
        print("No notes found.")

def delete_notes():
    if os.path.exists(NOTES_FILE):
        os.remove(NOTES_FILE)
        print("All notes deleted.")
    else:
        print("No notes to delete.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
