"""
Personal Media Tracker
A simple beginner-friendly CLI project that uses sqlite3 and one table called media.
"""

import sqlite3


# Name of the SQLite database file.
DB_NAME = "media_tracker.db"

# Allowed choices for the user.
MEDIA_TYPES = ["movie", "tv show", "book"]
MEDIA_TYPE_NUMBERS = {"1": "movie", "2": "tv show", "3": "book"}
STATUS_OPTIONS = ["plan to start", "in progress", "completed"]


def create_table():
    """Create the media table if it does not already exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # This project uses exactly one table called media.
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
    connection.close()


def display_entries(entries):
    """Print database records in a readable format."""
    if not entries:
        print("\nNo entries found.")
        return

    print("\n--- Media Entries ---")
    for entry in entries:
        print(f"ID: {entry[0]}")
        print(f"Title: {entry[1]}")
        print(f"Media Type: {entry[2]}")
        print(f"Genre: {entry[3]}")
        print(f"Platform/Source: {entry[4]}")
        print(f"Status: {entry[5]}")
        print(f"Rating: {entry[6]}")
        print(f"Notes: {entry[7]}")
        print("-" * 30)


def normalize_media_type(media_type):
    """Convert similar inputs into one standard media type."""
    media_type = media_type.strip().lower()

    # Let the user type a number instead of the whole word.
    if media_type in MEDIA_TYPE_NUMBERS:
        return MEDIA_TYPE_NUMBERS[media_type]

    # These extra options make the input a little more flexible.
    if media_type in ["tv", "tv show", "tvshow", "show", "drama"]:
        return "tv show"

    return media_type


def get_valid_media_type():
    """Ask until the user enters a supported media type."""
    while True:
        print("Choose media type: 1 = movie, 2 = TV show, 3 = book")
        media_type = normalize_media_type(
            input("Enter media type (movie/TV show/book or 1/2/3): ")
        )
        if media_type in MEDIA_TYPES:
            return media_type
        print("Invalid media type. Please choose movie, TV show, or book.")


def get_valid_status():
    """Ask until the user enters a valid status."""
    while True:
        status = input("Enter status (plan to start/in progress/completed): ").strip().lower()
        if status in STATUS_OPTIONS:
            return status
        print("Invalid status. Please choose plan to start, in progress, or completed.")


def get_rating_input(allow_blank=False):
    """Get a rating from the user and keep the input simple."""
    while True:
        rating_text = input("Enter rating: ").strip()

        if allow_blank and rating_text == "":
            return None

        if rating_text == "":
            return None

        try:
            return float(rating_text)
        except ValueError:
            print("Invalid rating. Please enter a number or leave it blank.")


def add_entry():
    """Add a new media entry to the database."""
    print("\n--- Add a Media Entry ---")

    # Title is required, so keep asking until the user enters something.
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

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO media (title, media_type, genre, platform_or_source, status, rating, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (title, media_type, genre, platform_or_source, status, rating, notes),
    )

    connection.commit()
    connection.close()

    print("Entry added successfully.")


def view_all_entries():
    """Show all entries in the media table."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM media")
    entries = cursor.fetchall()

    connection.close()
    display_entries(entries)


def filter_or_sort_entries():
    """Show a small menu for filtering or sorting records."""
    print("\n--- Filter or Sort Entries ---")
    print("1. Filter by media type")
    print("2. Filter by status")
    print("3. Sort by rating from highest to lowest")
    print("4. Sort by title in alphabetical order")

    choice = input("Choose an option: ").strip()

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    if choice == "1":
        media_type = get_valid_media_type()
        cursor.execute("SELECT * FROM media WHERE media_type = ?", (media_type,))
        entries = cursor.fetchall()
        display_entries(entries)

    elif choice == "2":
        status = get_valid_status()
        cursor.execute("SELECT * FROM media WHERE status = ?", (status,))
        entries = cursor.fetchall()
        display_entries(entries)

    elif choice == "3":
        # NULL ratings will appear last in this order.
        cursor.execute("SELECT * FROM media ORDER BY rating DESC")
        entries = cursor.fetchall()
        display_entries(entries)

    elif choice == "4":
        cursor.execute("SELECT * FROM media ORDER BY title ASC")
        entries = cursor.fetchall()
        display_entries(entries)

    else:
        print("Invalid option.")

    connection.close()


def entry_exists(entry_id):
    """Return True if the given id exists in the table."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM media WHERE id = ?", (entry_id,))
    result = cursor.fetchone()

    connection.close()
    return result is not None


def update_entry():
    """Update only status, rating, and notes for an existing entry."""
    print("\n--- Update an Entry ---")

    try:
        entry_id = int(input("Enter the id of the entry to update: ").strip())
    except ValueError:
        print("Invalid id. Please enter a number.")
        return

    if not entry_exists(entry_id):
        print("That id does not exist.")
        return

    print("Enter the new values below.")
    status = get_valid_status()
    rating = get_rating_input(allow_blank=True)
    notes = input("Enter notes: ").strip()

    connection = sqlite3.connect(DB_NAME)
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
    connection.close()

    print("Entry updated successfully.")


def delete_entry():
    """Delete an entry after asking the user for confirmation."""
    print("\n--- Delete an Entry ---")

    try:
        entry_id = int(input("Enter the id of the entry to delete: ").strip())
    except ValueError:
        print("Invalid id. Please enter a number.")
        return

    if not entry_exists(entry_id):
        print("That id does not exist.")
        return

    confirm = input("Are you sure you want to delete this entry? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete canceled.")
        return

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM media WHERE id = ?", (entry_id,))

    connection.commit()
    connection.close()

    print("Entry deleted successfully.")


def main():
    """Run the Personal Media Tracker menu."""
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


# This makes sure main() only runs when the file is executed directly.
if __name__ == "__main__":
    main()
