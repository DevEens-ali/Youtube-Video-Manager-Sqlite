# Youtube-Video-Manager-Sqlite
A beginner-friendly Python + SQLite project demonstrating CRUD (Create, Read, Update, Delete) operations through a command-line YouTube Video Manager.



#  YouTube Video Manager (Python + SQLite)

A simple command-line based **YouTube Video Manager** built using **Python** and **SQLite**. This project demonstrates the implementation of **CRUD (Create, Read, Update, Delete)** operations with a local database.

It is designed as a beginner-friendly project to understand how Python interacts with a database using the built-in `sqlite3` module.

---

##  Features

*  View all videos
*  Add a new video
*  Update an existing video
*  Delete a video
*  Success messages after each operation
*  Handles invalid IDs while updating or deleting
*  Displays a message when the database is empty

---

##  Technologies Used

* Python 3
* SQLite3 (Built-in Python Module)

---

##  Database Structure

**Table: `videos`**

| Column | Type                  |
| ------ | --------------------- |
| id     | INTEGER (Primary Key) |
| name   | TEXT                  |
| time   | TEXT                  |

---

## 📸 Menu

```text
Welcome to the YouTube Video Manager

1. List All Videos
2. Add Video
3. Update Video
4. Delete Video
5. Exit
```

---

##  CRUD Operations

### Create

Add a new video to the database.

### Read

Display all stored videos.

### Update

Modify the name or duration of an existing video.

### Delete

Remove a video using its ID.

---

##  Concepts Practiced

* Functions
* Loops
* Conditional Statements
* SQLite Database
* SQL Queries
* CRUD Operations
* Python `sqlite3` Module
* Error Handling
* Database Transactions

---

##  How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Open the project folder.

3. Run the Python file.

```bash
python UtubeWithdatabase.py
```

4. Start managing your videos.

---

##  Future Improvements

* Search videos by name
* Sort videos
* Store upload date
* Add video category
* Add video description
* Build a GUI version using Tkinter
* Build a Web version using Flask or Django

---

##  Learning Purpose

This project was created for learning purposes to understand how Python performs CRUD operations using SQLite. It serves as a foundation for building larger applications such as Todo Lists, Library Management Systems, Student Management Systems, and Web Applications.

---

##  If you like this project

Give it a  on GitHub and feel free to fork it for learning and improvements.
