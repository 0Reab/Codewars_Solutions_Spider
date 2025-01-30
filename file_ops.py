import os


def create_dirs() -> None:
    # create directories for each coding challenge difficulty + retired ones
    try:
        os.mkdir('Retired')
        for n in range(1,8+1): os.mkdir(f'{n}_kyu')

    except FileExistsError: print('Directory already exists')
    except PermissionError: print('Permission denied unable to create directories'); exit(1)
    except Exception as er: print(f'Error occurred {er}'); exit(1)


def cleanup_filename(file_name: str) -> str:
    # remove illegal windows filename characters
    illegal_characters = [
        '#', '%', '&', '{', '}', '\\', '<', '>', '*', '?', '/', ' ', '$', '!', "'", '"', ':', '@', '+', '`', '|', '=',
    ]
    return ''.join([ char for char in file_name if char not in illegal_characters ])


def write_file(path, text) -> True | False:
    # Write content to a file in a given path
    try:
        with open(path, 'w', encoding='utf-8') as file:
            os.utime(path, None)
            file.write(text)
            return True

    except FileExistsError:
        print(f'File already exists {path}')
    except Exception as err:
        print(f'Failed to write to {path}, {err}')

    return  False

