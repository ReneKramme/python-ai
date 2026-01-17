def write_file(working_directory, file_path, content):
    import os
    working_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir, file_path))
    valid_path = os.path.commonpath([working_dir, target_file]) == working_dir
    if not valid_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {str(e)}"
    
