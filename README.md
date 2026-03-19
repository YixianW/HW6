# Personal Media Tracker

Personal Media Tracker is a simple Python homework project made for beginners.
It is a command-line program that stores movies, TV shows, and books in one SQLite database.

## Project idea
This project helps a user keep track of media in one place.
The program can:
- add a new item
- view saved items
- filter or sort the list
- update an item
- delete an item

The records stay saved because the program uses SQLite.

## Technology used
- Python 3
- built-in `sqlite3`
- one SQLite table named `media`
- no external libraries

## Supported media types
The program supports:
- `movie`
- `tv show`
- `book`

To make input easier, the user can type:
- `1` for movie
- `2` for tv show
- `3` for book

If the user types `drama`, the program will save it as `tv show`.

## Supported status values
- `plan to start`
- `in progress`
- `completed`

## Database file
When the program starts, it automatically creates:
- `media_tracker.db`

Inside the database, it creates one table called `media` with these columns:
- `id INTEGER PRIMARY KEY AUTOINCREMENT`
- `title TEXT NOT NULL`
- `media_type TEXT NOT NULL`
- `genre TEXT`
- `platform_or_source TEXT`
- `status TEXT`
- `rating REAL`
- `notes TEXT`

## Menu
```text
--- Personal Media Tracker ---
1. Add a media entry
2. View all entries
3. Filter or sort entries
4. Update an entry
5. Delete an entry
6. Quit
```

## Features
### Add a media entry
The user enters:
- title
- media type
- genre
- platform or source
- status
- rating
- notes

### View all entries
The program prints all saved records in a readable way.

### Filter or sort entries
The user can:
- filter by media type
- filter by status
- sort by rating from highest to lowest
- sort by title in alphabetical order

### Update an entry
The user enters an id and can update only:
- status
- rating
- notes

### Delete an entry
The user enters an id, sees the selected record, and confirms before deleting it.

## How to run
Open a terminal in the project folder and run:

```bash
python3 personal_media_tracker.py
```

If needed, you can also try:

```bash
python personal_media_tracker.py
```

## Example of media type input
```text
Choose media type: 1 = movie, 2 = TV show, 3 = book
Enter media type (movie/TV show/book or 1/2/3): 1
```

## Sample interaction
```text
--- Personal Media Tracker ---
1. Add a media entry
2. View all entries
3. Filter or sort entries
4. Update an entry
5. Delete an entry
6. Quit
Enter your choice: 1

--- Add a Media Entry ---
Enter title: Interstellar
Choose media type: 1 = movie, 2 = TV show, 3 = book
Enter media type (movie/TV show/book or 1/2/3): 1
Enter genre: Sci-Fi
Enter platform or source: Netflix
Enter status (plan to start/in progress/completed): completed
Enter rating: 5
Enter notes: Great movie
Entry added successfully.
```

## Files in this project
- `personal_media_tracker.py` - the main program
- `media_tracker.db` - the database file created automatically
- `README.md` - project explanation

## Important note
This project is a CLI program, not a website.
GitHub Pages is for static web pages, so this project should be run locally in a terminal.
