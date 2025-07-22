task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
if time_bound == "yes":
    reminder = " that requires immediate attention today."
else:
    reminder = ". Consider completing it when you have free time."

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task{reminder}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{reminder}")
    case "low":
        print(f"Reminder: '{task}' is a low priority task{reminder}")
    case _:
        print("Invalid priority level.")