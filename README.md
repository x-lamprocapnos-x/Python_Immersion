# Python_Immersion (Observation/Python Learning)

### This repository contains my personal reflections, journal entries, and screenshots from working on three separate Python/Django projects. The goal is to document my learning journey, provide insight into my understanding, and create a reference for future development work and interviews.

## **Repository Structure**
| Folder | Description |
|---|---|
| python-intro | My Foundational learning path through Python basics and a CLI recipe manager project|
| python-two | Reflections and screenshots from my first Django project following a course |
| bookstore_practice | Analysis and notes on building a bookstore inventory and sales app using Django |

## **1. Django Bookstore App**
A simple Django-based inventory and sales management system for a bookstore. This Project includes:

***Features***
- Add and categorize books (genre, format)
- Store customer data and notes
- Track sales with timestamps
- Link salespeople to Django users
- Unit tests for the Book model

***Apps Overview***
| App | Purpose |
|---|---|
| books | Book and genre data |
| customers | Customer records |
| sales | Sales tracking |
| salesperson | Profiles for salespeople |

***Tech Stack***
- Python 3.x
- Django 4.2
- SQLite3

## **2. Python-Intro (Foundational CLI App)**
A personal learning project designed to build up Python fundamentals, including:

***Key Lessons***
- Python syntax and data structures
- File handling
- Pickling and unpickling data
- CLI-based CRUD app using SQLAlchemy and MySQL

 ***Mini Pickle Demo***
 ```python
# Save dictionary to binary files
with open("recipe_binary.bin", "wb") as binary_file:
    pickle.dump(recipe, binary_file)

# Load and display the recipe
with open("recipe_binary.bin", "rb") as binary_file:
    loaded_recipe = pickle.load(binary_file)
```
***Full Recipe App Features***
- Add/search/edit/delete recipes
- Search by ingredients
- Difficulty calculated automatically
- CLI user input with validation

***Tech Stack***
- Python
- SQLAlchemy
- MySQL / MySQL Connector
- python-dotenv

***Known Issues***
- Terminal-only interaction
- No user authentication
- Manual data entry

## **3. Python-Two (A2_Recipe_App Observations)
This section contains journal entries, notes, and screenshots from my experience with the A2_Recipe_App, my very first Django project.

***Purpose***
The goal was to reflect after each lesson in the course, document key takeaways, and assess my grasp of new concepts.

***Tools Used***
- Markdown (for journaling)
- Snip & Sketch Tool (screenshots)
- Git & GitHub

***Contents***
| Folder | Description |
|---|---|
| learning_journal/ | Reflection journal entries after each major lesson |
| screenshots/ | 	Visual snapshots from key moments in the project |

## **General Notes**
- Each folder is self-contained and reflects a different stage of my learning.
- No setup is required to view reflections and screenshots — just browse the repo.
- All observations are based on hands-on work and real project interaction.

## **License**
This repository is released under the MIT License. You are free to view, use, and adapt any part of this repo for learning or personal use.