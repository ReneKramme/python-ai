import os
from functions.config import MAXCHAR
from google.genai import types # type: ignore

def get_file_content(working_directory, file_path):
    working_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir, file_path))
    valid_path = os.path.commonpath([working_dir, target_file]) == working_dir
    if not valid_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file) as f:
            content = f.read(MAXCHAR)
            if f.read(1):
                content += f'\n[...File "{file_path}" truncated at {MAXCHAR} characters]'
            return content
        
    except Exception as e:
        return f"Error: {str(e)}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieve the content of a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file within the working directory",
            ),
        },
        required=["file_path"],
    ),
)