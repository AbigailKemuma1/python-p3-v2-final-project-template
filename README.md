# Train & Gain CLI
Here are the links to the videos giving a detailed explanation of what my cli project does:https://www.loom.com/share/19ee42f552534c049620db963f91a1ba and https://www.loom.com/share/d701f8889cf8490282a8b0bbbf8b6851 

Train & Gain is a Python Command-Line Interface (CLI) application designed to help users manage and track their fitness journey. With this app, users can log workouts, meals, progress, and goals, while admins can monitor all users and their activity. The project uses SQLAlchemy ORM for database management and follows Python best practices.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Files and Functions](#key-files-and-functions)
- [Database Models](#database-models)
- [Dependencies](#dependencies)
- [Screenshots](#screenshots)

---

## Features
- User authentication (login and registration)
- Add, view, and manage workouts, meals, progress, and goals
- Admin functionality to monitor and manage all users
- Detailed prompts and input validation to guide users
- One-to-many relationships between users and their workouts, meals, and goals
- Clean CLI menus for easy navigation

---

## Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:AbigailKemuma1/python-p3-v2-final-project-template.git
    cd python-p3-v2-final-project-template
    ```
2. Install dependencies and activate the virtual environment using Pipenv:
    ```bash
    pipenv install
    pipenv shell
    ```
3. Create the database tables:
    ```bash
    python -m create_tables
    ```
4. Launch the CLI application:
    ```bash
    python -m lib.cli
    ```

---

## Usage
When you start the application, you’ll see the main menu with options to log in as a user or admin, or to register as a new user.  

### User Actions
Once logged in as a user, you can:
- **View Workouts:** See all your past workouts with details.
- **Add Workout:** Log a new workout with type, duration, and calories burned.
- **Update Profile:** Edit your personal information like name, age, height, weight, and fitness goals.
- **Add Meal:** Record a meal with calories, protein, carbs, and fats.
- **View Meals:** Review all meals you’ve logged.
- **Log Progress:** Record your weight and optional notes.
- **View Progress:** Check your historical progress entries.
- **Set Goal:** Add a fitness goal with a target and deadline.
- **View Goals:** Review all goals and optionally update their status.

### Admin Actions
Admins have additional capabilities:
- View all users
- View workouts, meals, progress, and goals for any user
- Remove a user from the system

The menus are intuitive and will guide you through input validation, ensuring that only valid data is stored in the database.

---

## Project Structure

python-p3-v2-final-project-template/
├─ lib/
│ ├─ cli.py
│ ├─ helpers.py
│ ├─ debug.py
│ └─ models/
│ ├─ base.py
│ ├─ user.py
│ ├─ workout.py
│ ├─ meal.py
│ └─ goal.py
├─ create_tables.py
├─ Pipfile
└─ README.md


---

## Key Files and Functions

### `lib/cli.py`
This is the main script for the CLI. It contains the main menu logic and user/admin menus.

**Key Functions:**
- `main()`: Shows the main menu and handles user login, registration, and admin login.
- `user_menu(user_id)`: Allows users to manage workouts, meals, progress, and goals.
- `admin_menu()`: Allows admins to monitor users and their activities.

### `lib/helpers.py`
Contains utility functions to handle all database operations.

**Important Functions:**
- User authentication: `register_user()`, `login_user()`, `login_admin()`
- Profile updates: `update_user_profile()`
- Workouts: `add_workout()`, `view_workouts()`
- Meals: `add_meal()`, `view_meals()`
- Progress tracking: `log_progress()`, `view_progress()`
- Goals: `set_goal()`, `view_goals()`, `update_goal_status()`
- Admin utilities: `get_all_users()`, `remove_user()`

### `lib/models/base.py`
Contains the SQLAlchemy setup:
- `Base`: The declarative base for ORM models
- `engine`: Database engine connection
- `Session`: Factory to create sessions for transactions

### `lib/models/user.py`
Defines the `User` model with properties like `username`, `password`, `name`, `age`, `height`, `weight`, and `fitness_goal`. Includes methods for creating, updating, deleting, and retrieving users.

### `lib/models/workout.py`
Defines the `Workout` model, linked to a user. Stores `workout_type`, `duration`, and `calories_burned`. Provides ORM methods for CRUD operations.

### `lib/models/meal.py`
Defines the `Meal` model, linked to a user. Stores `meal_name`, `calories`, `protein`, `carbs`, and `fats`. Includes methods to manage meals.

### `lib/models/goal.py`
Defines the `Goal` model, linked to a user. Stores `goal_type`, `target`, `deadline`, and `status`. Includes methods for creating, updating, and retrieving goals.

### `create_tables.py`
Creates all tables in the database using SQLAlchemy ORM. This script should be run once before using the CLI.

---

## Database Models
The database includes the following tables:

- `User` – stores user profile and authentication data
- `Workout` – tracks workouts for each user (one-to-many relationship)
- `Meal` – tracks meals for each user (one-to-many relationship)
- `Goal` – tracks goals for each user (one-to-many relationship)

---

## Dependencies
- Python 3.8+
- SQLAlchemy
- Pipenv (for virtual environment management)

---

## Screenshots
**Main Menu:**
User Login

Register

Admin Login

Exit



**User Menu:**
View Workouts

Add Workout

Update Profile

Add Meal

View Meals

Log Progress

View Progress

Set Goal

View Goals

Logout


---
