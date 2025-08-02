import pandas as pd

# REQUIRED_COLUMNS specifies the expected columns in the Excel file.
# 'Period' and 'Execution Time' are in milliseconds.
# 'Deadline' is based on Rate Monotonic Scheduling (RMS).
# 'Resource Requirements' is currently not used in the system.
REQUIRED_COLUMNS = [
    'Task ID', 
    'Priority', 
    'Period', 
    'Execution Time', 
    'Deadline',
]

def load_tasks_from_excel(file_path):
    """
    Loads task definitions from an Excel file and validates column headers.

    Parameters:
    - file_path (str): Path to the Excel file (.xlsx)

    Returns:
    - List[dict]: List of task dictionaries
    """

    try:
        df = pd.read_excel(file_path)

        # Validate column names
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise ValueError(f"Missing columns in Excel file: {missing}")

        # Optional: convert 'Resource Requirements' from string to list
        df['Resource Requirements'] = df['Resource Requirements'].apply(eval)

        tasks = df.to_dict(orient='records')
        return tasks

    except Exception as e:
        print(f"[ERROR] Failed to load tasks: {e}")
        return []
