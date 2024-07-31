import os


def create_folder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError as err:
        print(f"==:== create_folder.err ==:== {err}")
