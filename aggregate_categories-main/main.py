import subprocess
import os
import time
from project_config import config

def run_script(script_name):
    """Run a Python script using subprocess and return created files."""
    print(f"Starting {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    
    # Print script output
    print(result.stdout)
    
    # Check if the script encountered any errors
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
        raise RuntimeError(f"Failed to run {script_name}")
    
    print(f"Finished {script_name}")
    
    # Assuming the script produces specific files, return those file paths
    # Modify this according to what each script generates
    script_output_map = {
        'clean_data.py': 'cleaned_data.csv',
        'filter_groups.py': 'filtered_groups.csv',
        'filter_subjects.py': 'filtered_subjects.csv',
        'aggregate.py': 'aggregated_data.csv',
        'convert.py': 'zendesk_categories.xlsx'
    }
    
    created_file = script_output_map.get(script_name, None)
    return [created_file] if created_file else []

def delete_files_after_timeout(file_paths, timeout=60):
    """Delete files after a timeout (in seconds)."""
    print(f"Waiting {timeout} seconds before deleting files...")
    time.sleep(timeout)  # Wait for the specified timeout (default is 60 seconds)

    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")

def main():
    # Retrieve the list of scripts from the config file
    scripts = config['scripts']

    # List to hold all created files
    all_created_files = []

    for script in scripts:
        print(f"Running {script}...")
        try:
            created_files = run_script(script)
            all_created_files.extend(created_files)
        except RuntimeError as e:
            print(e)  # Log the error but continue running other scripts

    # After running all scripts, call delete_files_after_timeout()
    if all_created_files:
        print(f"Files to delete: {all_created_files}")
        delete_files_after_timeout(all_created_files, timeout=60)
    else:
        print("No files created or files list is empty. Skipping deletion.")

if __name__ == "__main__":
    main()
