from pathlib import Path


FILE_DIR = Path("files")
FILE_DIR.mkdir(exist_ok=True)


def get_file_path(filename):
    """Return a safe path inside the files directory."""
    filename = Path(filename).name
    return FILE_DIR / filename


def create_file(filename, content):
    path = get_file_path(filename)

    if path.exists():
        return False, f"File '{filename}' already exists."

    path.write_text(content, encoding="utf-8")
    return True, f"File '{filename}' created successfully."


def read_file(filename):
    path = get_file_path(filename)

    if not path.exists():
        return False, "File does not exist."

    try:
        content = path.read_text(encoding="utf-8")
        return True, content
    except Exception as e:
        return False, str(e)


def append_file(filename, content):
    path = get_file_path(filename)

    if not path.exists():
        return False, "File does not exist."

    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write("\n" + content)

        return True, "Content appended successfully."

    except Exception as e:
        return False, str(e)


def overwrite_file(filename, content):
    path = get_file_path(filename)

    if not path.exists():
        return False, "File does not exist."

    try:
        path.write_text(content, encoding="utf-8")
        return True, "File content overwritten successfully."

    except Exception as e:
        return False, str(e)


def rename_file(filename, new_filename):
    old_path = get_file_path(filename)
    new_path = get_file_path(new_filename)

    if not old_path.exists():
        return False, "Original file does not exist."

    if new_path.exists():
        return False, "A file with the new name already exists."

    try:
        old_path.rename(new_path)
        return True, "File renamed successfully."

    except Exception as e:
        return False, str(e)


def delete_file(filename):
    path = get_file_path(filename)

    if not path.exists():
        return False, "File does not exist."

    try:
        path.unlink()
        return True, "File deleted successfully."

    except Exception as e:
        return False, str(e)


def get_files():
    """Return all files in the files directory."""
    return sorted(
        [file for file in FILE_DIR.iterdir() if file.is_file()]
    )