from models.base import Session
from models.user import User
from models.workout import Workout
from models.meal import Meal
from models.goal import Goal
from models.admin import Admin


session = Session()

def user_menu(user_id):
    while True:
        print("\n--- User Menu ---")
        print("1. View Workouts")
        print("2. Add Workout")
        print("3. Update Profile")
        print("4. Add Meal")
        print("5. View Meals")
        print("6. Log Progress")
        print("7. View Progress")
        print("8. Set Goal")
        print("9. View Goals")
        print("10. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            workouts = Workout.find_by_user(session, user_id)
            for w in workouts:
                print(w.id, w.user_id, w.workout_type, w.duration, w.calories_burned)

        elif choice == "2":
            workout_type = input("Workout Type: ")
            duration = input("Duration (minutes): ")
            calories = input("Calories Burned: ")
            try:
                duration = float(duration)
                calories = float(calories)
            except ValueError:
                print("Duration and calories must be numbers.")
                continue
            Workout.create(session, user_id=user_id, workout_type=workout_type, duration=duration, calories_burned=calories)
            print(f"Workout '{workout_type}' added successfully!")

        elif choice == "3":
            user = User.find_by_id(session, user_id)
            new_name = input("New name (leave blank to keep current): ")
            new_age = input("New age: ")
            new_height = input("New height: ")
            new_weight = input("New weight: ")
            new_goal = input("New fitness goal: ")
            user.name = new_name if new_name.strip() else user.name
            user.age = int(new_age) if new_age.strip() else user.age
            user.height = float(new_height) if new_height.strip() else user.height
            user.weight = float(new_weight) if new_weight.strip() else user.weight
            user.fitness_goal = new_goal if new_goal.strip() else user.fitness_goal
            session.commit()
            print("Profile updated successfully!")

        elif choice == "4":
            name = input("Meal name: ")
            calories = float(input("Calories: "))
            protein = float(input("Protein (g): "))
            carbs = float(input("Carbs (g): "))
            fats = float(input("Fat (g): "))
            Meal.create(session, user_id=user_id, name=name, calories=calories, protein=protein, carbs=carbs, fats=fats)
            print("Meal added successfully!")

        elif choice == "5":
            meals = Meal.find_by_user(session, user_id)
            for m in meals:
                print(m.id, m.user_id, m.name, m.calories, m.protein, m.carbs, m.fats)

        elif choice == "6":
            weight = float(input("Weight (kg): "))
            note = input("Notes: ")
            Goal.create(session, user_id=user_id, goal_type="weight log", target=weight, status=note)
            print("Progress logged!")

        elif choice == "7":
            workouts = Workout.find_by_user(session, user_id)
            for w in workouts:
                print(w.id, w.user_id, w.workout_type, w.duration, w.calories_burned)

        elif choice == "8":
            goal_type = input("Goal (e.g. 'Lose 5kg'): ")
            target = float(input("Target value: "))
            deadline = input("Deadline: ")
            Goal.create(session, user_id=user_id, goal_type=goal_type, target=target, status=deadline)
            print("Goal set!")

        elif choice == "9":
            goals = Goal.find_by_user(session, user_id)
            for g in goals:
                print(g.id, g.user_id, g.goal_type, g.target, g.status)
            goal_id = input("Enter goal ID to update or Enter to skip: ")
            if goal_id.strip():
                status = input("New status: ")
                goal = session.query(Goal).filter_by(id=int(goal_id)).first()
                goal.status = status
                session.commit()
                print("Goal status updated!")

        elif choice == "10":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View All Users")
        print("2. View Workouts by User")
        print("3. View Meals by User")
        print("4. View Goals by User")
        print("5. Remove a User")
        print("6. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            users = User.get_all(session)
            for u in users:
                print(u.id, u.username, u.name)

        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            workouts = Workout.find_by_user(session, user_id)
            for w in workouts:
                print(w.id, w.user_id, w.workout_type, w.duration, w.calories_burned)

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            meals = Meal.find_by_user(session, user_id)
            for m in meals:
                print(m.id, m.user_id, m.name, m.calories, m.protein, m.carbs, m.fats)

        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            goals = Goal.find_by_user(session, user_id)
            for g in goals:
                print(g.id, g.user_id, g.goal_type, g.target, g.status)

        elif choice == "5":
            user_id = int(input("Enter user ID to remove: "))
            confirm = input(f"Remove user {user_id}? (y/n): ")
            if confirm.lower() == "y":
                user = User.find_by_id(session, user_id)
                session.delete(user)
                session.commit()
                print("User removed successfully!")

        elif choice == "6":
            print("Admin logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def main():
    print("=== Welcome to Train & Gain CLI ===")
    while True:
        print("\n1. User Login")
        print("2. Register")
        print("3. Admin Login")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            user = session.query(User).filter_by(username=username, password=password).first()
            if user:
                print(f"\nWelcome, {user.name}! 💪")
                user_menu(user.id)
            else:
                print("Invalid user login. Try again.")

        elif choice == "2":
            username = input("Choose username: ")
            password = input("Choose password: ")
            name = input("Full name: ")
            age = int(input("Age: "))
            height = float(input("Height (m): "))
            weight = float(input("Weight (kg): "))
            goal = input("Fitness goal: ")
            new_user = User(
                username=username,
                password=password,
                name=name,
                age=age,
                height=height,
                weight=weight,
                fitness_goal=goal
            )
            session.add(new_user)
            session.commit()
            print("User registered successfully! Please log in.")

        elif choice == "3":
            username = input("Admin username: ")
            password = input("Password: ")
            admin = session.query(Admin).filter_by(username=username, password=password).first()
            if admin:
                print(f"\nWelcome, Admin {admin.username}!")
                admin_menu()
            else:
                print("Invalid admin login. Try again.")

        elif choice == "4":
            print("Goodbye! 👋")
            session.close()
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
