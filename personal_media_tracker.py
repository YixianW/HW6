"""Personal Media Tracker - a simple beginner-friendly SQLite CLI project."""

import sqlite3


DB_NAME = "media_tracker.db"
# Keep these values lowercase because user input is converted to lowercase.
MEDIA_TYPES = ["movie", "tv show", "book"]
MEDIA_TYPE_NUMBERS = {"1": "movie", "2": "tv show", "3": "book"}
STATUS_OPTIONS = ["plan to start", "in progress", "completed"]
MEDIA_TYPE_HELP_TEXT = "Choose media type: 1 = movie, 2 = TV show, 3 = book"


def create_table():
    """Create the media table if it does not already exist."""
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                media_type TEXT NOT NULL,
                genre TEXT,
                platform_or_source TEXT,
                status TEXT,
                rating REAL,
                notes TEXT
            )
            """
        )
        connection.commit()


def display_entries(entries):
    """Print records in a clean format."""
    if not entries:
        print("\nNo entries found.")
        return

    print("\n--- Media Entries ---")
    for entry in entries:
        print(f"ID: {entry[0]}")
        print(f"Title: {entry[1]}")
        print(f"Media Type: {entry[2]}")
        print(f"Genre: {entry[3] or 'N/A'}")
        print(f"Platform/Source: {entry[4] or 'N/A'}")
        print(f"Status: {entry[5] or 'N/A'}")
        print(f"Rating: {entry[6] if entry[6] is not None else 'N/A'}")
        print(f"Notes: {entry[7] or 'N/A'}")
        print("-" * 30)


def normalize_media_type(media_type):
    """Convert user input into one standard media type."""
    media_type = media_type.strip().lower()

    if media_type in MEDIA_TYPE_NUMBERS:
        return MEDIA_TYPE_NUMBERS[media_type]

    if media_type in ["tv", "tv show", "tvshow", "show", "drama"]:
        return "tv show"

    return media_type


def get_valid_media_type():
    """Ask the user to enter a valid media type."""
    while True:
        # Show the number choices every time so the user knows what 1, 2, and 3 mean.
        print(MEDIA_TYPE_HELP_TEXT)
        media_type = normalize_media_type(
            input("Enter media type (movie/TV show/book or 1/2/3): ")
        )

        if media_type in MEDIA_TYPES:
            return media_type

        print("Invalid media type. Please choose movie, TV show, or book.")


def get_valid_status():
    """Ask the user to enter a valid status."""
    while True:
        status = input(
            "Enter status (plan to start/in progress/completed): "
        ).strip().lower()

        if status in STATUS_OPTIONS:
            return status

        print("Invalid status. Please choose plan to start, in progress, or completed.")


def get_rating_input(allow_blank=False):
    """Ask the user to enter a rating."""
    while True:
        rating_text = input("Enter rating: ").strip()

        if rating_text == "":
            if allow_blank:
                return None
            return None

        try:
            return float(rating_text)
        except ValueError:
            print("Invalid rating. Please enter a number or leave it blank.")


def get_entry_by_id(entry_id):
    """Return one entry that matches the given id."""
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM media WHERE id = ?", (entry_id,))
        return cursor.fetchone()


def add_entry():
    """Add a new media entry."""
    print("\n--- Add a Media Entry ---")

    while True:
        title = input("Enter title: ").strip()
        if title:
            break
        print("Title cannot be empty.")

    media_type = get_valid_media_type()
    genre = input("Enter genre: ").strip()
    platform_or_source = input("Enter platform or source: ").strip()
    status = get_valid_status()
    rating = get_rating_input()
    notes = input("Enter notes: ").strip()

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO media (title, media_type, genre, platform_or_source, status, rating, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (title, media_type, genre, platform_or_source, status, rating, notes),
        )
        connection.commit()

    print("Entry added successfully.")


def view_all_entries():
    """Display all saved entries."""
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM media ORDER BY id ASC")
        entries = cursor.fetchall()

    display_entries(entries)


def filter_or_sort_entries():
    """Filter or sort entries with a small menu."""
    print("\n--- Filter or Sort Entries ---")
    print("1. Filter by media type")
    print("2. Filter by status")
    print("3. Sort by rating from highest to lowest")
    print("4. Sort by title in alphabetical order")

    choice = input("Choose an option: ").strip()

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()

        if choice == "1":
            media_type = get_valid_media_type()
            cursor.execute("SELECT * FROM media WHERE media_type = ? ORDER BY id ASC", (media_type,))
            entries = cursor.fetchall()
            display_entries(entries)

        elif choice == "2":
            status = get_valid_status()
            cursor.execute("SELECT * FROM media WHERE status = ? ORDER BY id ASC", (status,))
            entries = cursor.fetchall()
            display_entries(entries)

        elif choice == "3":
            cursor.execute("SELECT * FROM media ORDER BY rating DESC, title ASC")
            entries = cursor.fetchall()
            display_entries(entries)

        elif choice == "4":
            cursor.execute("SELECT * FROM media ORDER BY title ASC")
            entries = cursor.fetchall()
            display_entries(entries)

        else:
            print("Invalid option.")


def update_entry():
    """Update status, rating, and notes for one entry."""
    print("\n--- Update an Entry ---")

    try:
        entry_id = int(input("Enter the id of the entry to update: ").strip())
    except ValueError:
        print("Invalid id. Please enter a number.")
        return

    entry = get_entry_by_id(entry_id)
    if entry is None:
        print("That id does not exist.")
        return

    print("Current entry:")
    display_entries([entry])
    print("Enter the new values below.")

    status = get_valid_status()
    rating = get_rating_input(allow_blank=True)
    notes = input("Enter notes: ").strip()

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE media
            SET status = ?, rating = ?, notes = ?
            WHERE id = ?
            """,
            (status, rating, notes, entry_id),
        )
        connection.commit()

    print("Entry updated successfully.")


def delete_entry():
    """Delete one entry after confirmation."""
    print("\n--- Delete an Entry ---")

    try:
        entry_id = int(input("Enter the id of the entry to delete: ").strip())
    except ValueError:
        print("Invalid id. Please enter a number.")
        return

    entry = get_entry_by_id(entry_id)
    if entry is None:
        print("That id does not exist.")
        return

    print("Entry to delete:")
    display_entries([entry])
    confirm = input("Are you sure you want to delete this entry? (y/n): ").strip().lower()

    if confirm != "y":
        print("Delete canceled.")
        return

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM media WHERE id = ?", (entry_id,))
        connection.commit()

    print("Entry deleted successfully.")


def main():
    """Run the program menu."""
    create_table()

    while True:
        print("\n--- Personal Media Tracker ---")
        print("1. Add a media entry")
        print("2. View all entries")
        print("3. Filter or sort entries")
        print("4. Update an entry")
        print("5. Delete an entry")
        print("6. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_all_entries()
        elif choice == "3":
            filter_or_sort_entries()
        elif choice == "4":
            update_entry()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
