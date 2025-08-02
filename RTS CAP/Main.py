from TaskLoader import load_tasks_from_excel

file_path = "/workspaces/Real-time-system-RL/RTS CAP/Simulated Data/Book.xlsx"

tasks = load_tasks_from_excel(file_path)

for task in tasks:
    print(task)
