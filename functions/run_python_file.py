def run_python_file(working_directory, file_path, args=None):
    import os
    import subprocess
    
    working_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir, file_path))
    valid_path = os.path.commonpath([working_dir, target_file]) == working_dir
    if not valid_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        command = ["python", target_file]
        if args:
            command.extend(args)
        completed_run = subprocess.run(command, check=True, timeout=30, cwd=working_dir,capture_output=True, text=True)
        output = ""
        if completed_run.returncode != 0:
            output += f'Process exited with code {completed_run.returncode}\n'
        if not completed_run.stdout and not completed_run.stderr:
            output += "No output produced.\n"
        else:
            if completed_run.stdout:
                output += f'STDOUT:\n{completed_run.stdout}\n'
            if completed_run.stderr:
                output += f'STDERR:\n{completed_run.stderr}\n'
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
        
        