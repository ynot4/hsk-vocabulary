import os
import ctypes.wintypes


def create_save_folder():
    CSIDL_PERSONAL = 5  # My Documents
    SHGFP_TYPE_CURRENT = 0  # Get current, not default value

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

    directory = buf.value + r"\(ynot)\hsk-vocabulary"
    if not os.path.exists(directory):
        os.makedirs(directory)

    save_location = directory + r"\config.py"

    if not os.path.exists(save_location):
        with open(save_location, "w") as f:
            f.write('''saved_dict = {"HSK 1": 1,
"HSK 2": 1,
"HSK 3": 1,
"HSK 4": 0,
"HSK 5": 0,
"HSK 6": 0,
}
canto_rom = "Yale (Tone Numbers)"
mand = "Standard Chinese"''')

    return save_location


save_location = create_save_folder()

import importlib.util


def get_dict():
    MODULE_PATH = save_location
    MODULE_NAME = "config"

    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    modulevar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulevar)

    dict = (modulevar.saved_dict)

    return dict


def get_canto_rom():
    MODULE_PATH = save_location
    MODULE_NAME = "config"

    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    modulevar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulevar)

    rom = (modulevar.canto_rom)

    return rom


def get_mand():
    MODULE_PATH = save_location
    MODULE_NAME = "config"

    spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
    modulevar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulevar)

    rom = (modulevar.mand)

    return rom
