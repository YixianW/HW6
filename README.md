# Personal Media Tracker

This is a simple Python homework project made for beginners.
It is a **command-line (CLI)** program that helps a user keep track of:

- movies
- TV shows
- books

The program uses:

- Python
- the built-in `sqlite3` library
- one SQLite table called `media`

---

## Important note

This project is **not a website**.
It runs in the **terminal/command prompt**, not in GitHub Pages.

That means:

- GitHub is a good place to upload the code
- GitHub Pages is **not** the right place to run this project
- to use the program, you need to run the Python file locally

---

## Features

The program includes full CRUD features:

### 1. Create
Add a new media entry with:
- title
- media type
- genre
- platform or source
- status
- rating
- notes

### 2. Read
- View all entries
- Filter by media type (`movie`, `TV show`, or `book`)
- Filter by status
- Sort by rating from highest to lowest
- Sort by title in alphabetical order

### 3. Update
Update only:
- status
- rating
- notes

### 4. Delete
Delete an entry by id after confirmation.

---

## Database information

The program automatically creates a database file named:

`media_tracker.db`

It also automatically creates one table named:

`media`

Schema used in the table:

- `id INTEGER PRIMARY KEY AUTOINCREMENT`
- `title TEXT NOT NULL`
- `media_type TEXT NOT NULL`
- `genre TEXT`
- `platform_or_source TEXT`
- `status TEXT`
- `rating REAL`
- `notes TEXT`

---

## Supported values

### Media types
- `movie`
- `tv show`
- `book`

You can also type:
- `1` for `movie`
- `2` for `tv show`
- `3` for `book`

If a user types `drama`, the program will save it as `tv show` to keep the filter options consistent.

### Status values
- `plan to start`
- `in progress`
- `completed`

---

## How to run the program

### Step 1: Make sure Python is installed
You need Python 3 on your computer.

### Step 2: Open the project folder in a terminal
Go to the folder that contains:

- `personal_media_tracker.py`

### Step 3: Run the file
Use this command:

```bash
python3 personal_media_tracker.py
```

If your computer uses `python` instead of `python3`, you can try:

```bash
python personal_media_tracker.py
```

---

## Menu shown in the program

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

## Simple sample interaction

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

- `personal_media_tracker.py` -> the main Python program
- `media_tracker.db` -> the SQLite database file created automatically when the program runs

---

## Beginner-friendly notes

- The project uses functions to keep the code organized.
- The database is created automatically.
- The program handles simple invalid input cases.
- The media type filter supports `movie`, `tv show`, and `book`.
- Users can type `1`, `2`, or `3` for media type, and the program always shows what each number means.
- If there are no records, it clearly prints a message.
- The output is designed to be easy to read in the terminal.

---

## Why GitHub Pages looks blank

If you upload this project and open it with GitHub Pages, you may see a blank page or nothing useful to click.
That is normal because this project is a **CLI program**, not a webpage.

GitHub Pages works for files like:
- HTML
- CSS
- JavaScript

This project uses:
- Python
- sqlite3
- terminal input/output

So it should be run locally in a terminal, not as a GitHub Pages site.
