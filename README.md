# Personal Media Tracker

Personal Media Tracker is a simple beginner-friendly Python CLI project.
It lets a user save and manage movies, TV shows, and books in one SQLite database.

This project is meant to feel like a homework assignment:
- one Python file
- one SQLite table
- no external libraries
- easy terminal menu
- clear functions and simple input

---

## What this project does

The program helps the user:
- add a new media item
- view all saved items
- filter or sort the saved list
- update an item
- delete an item

The data is stored in a local SQLite database file, so the records stay saved after the program closes.

---

## Tools used

This project uses:
- Python 3
- the built-in `sqlite3` library
- one SQLite table called `media`

No Flask, no tkinter, and no external packages are used.

---

## Media types supported

The program supports these media types:
- `movie`
- `tv show`
- `book`

For convenience, the user can also enter numbers when choosing media type:
- `1` = `movie`
- `2` = `tv show`
- `3` = `book`

If the user types `drama`, the program saves it as `tv show`.

---

## Status values supported

Suggested status values in the program:
- `plan to start`
- `in progress`
- `completed`

---

## Database information

When the program runs, it automatically creates a database file named:

`media_tracker.db`

It also creates one table named `media` if the table does not already exist.

### Table schema

- `id INTEGER PRIMARY KEY AUTOINCREMENT`
- `title TEXT NOT NULL`
- `media_type TEXT NOT NULL`
- `genre TEXT`
- `platform_or_source TEXT`
- `status TEXT`
- `rating REAL`
- `notes TEXT`

---

## Main menu

When the program starts, the user sees this menu:

```text
--- Personal Media Tracker ---
1. Add a media entry
2. View all entries
3. Filter or sort entries
4. Update an entry
5. Delete an entry
6. Quit
```

---

## Features

### 1. Add a media entry
The user enters:
- title
- media type
- genre
- platform or source
- status
- rating
- notes

### 2. View all entries
The program prints every saved record in a clear format.

### 3. Filter or sort entries
The user can:
- filter by media type
- filter by status
- sort by rating from highest to lowest
- sort by title in alphabetical order

### 4. Update an entry
The user enters an `id`, then updates only:
- status
- rating
- notes

### 5. Delete an entry
The user enters an `id`, confirms the action, and the selected record is deleted.

---

## How to run the program

### Step 1
Make sure Python 3 is installed.

### Step 2
Open a terminal in the folder that contains:
- `personal_media_tracker.py`

### Step 3
Run one of these commands:

```bash
python3 personal_media_tracker.py
```

or

```bash
python personal_media_tracker.py
```

---

## Example of media type input

When adding or filtering media, the program shows the choices clearly:

```text
Choose media type: 1 = movie, 2 = TV show, 3 = book
Enter media type (movie/TV show/book or 1/2/3): 1
```

This means the user can either type the word or type the number.

---

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

---

## Files in this project

- `personal_media_tracker.py` - main Python program
- `media_tracker.db` - SQLite database file created automatically after the program runs
- `README.md` - project explanation and run instructions

---

## Beginner notes

- The project uses functions to keep the code organized.
- The database and table are created automatically.
- The program handles simple invalid input cases.
- The program prints a message when no records are found.
- Records are stored in SQLite, so they stay saved for later use.
- The terminal output is kept simple and readable.

---

## Important note about GitHub Pages

This project is a **command-line program**, not a website.
So if it is uploaded to GitHub and opened with GitHub Pages, it will not work like a clickable web app.

GitHub Pages is for static web files such as:
- HTML
- CSS
- JavaScript

This project should be run locally in a terminal.
