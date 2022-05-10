from copy import deepcopy
import toml, os, sys


yeses = ["y", "ye", "yes"]
nos = ["no", "n"]
valid_answers = yeses + nos
modinfo = {
    "display_name": None,
    "description": None,
    "version": None,
    "category": None,
    "authors": None
}


def get_category(mod_subpaths: list):
    categories = {
        "fighter": "Fighter",
        "stage": "Stage",
        "effect": "Effect",
        "stream;": "Audio",
        "ui": "UI"
    }
    mod_subpaths.sort()
    for subpath in mod_subpaths:
        if subpath in categories:
            return categories[subpath]
    return "Misc"

def main(mods_path, ask_name, ask_author, ask_desc, ask_ver, ask_cat):
    for paths in os.listdir(mods_path):
        if "info.toml" not in os.listdir(os.path.join(mods_path, paths)):
            print(f"Mod found! Directory name is {os.path.basename(paths)}.")
        else:
            continue
        new_toml = deepcopy(modinfo)
        subdirs = [d for d in os.listdir(os.path.join(mods_path, paths)) if "info.toml" not in os.listdir(os.path.join(mods_path, paths))]
        if ask_cat in nos:
            new_toml["category"] = get_category(subdirs)
        else:
            new_toml["category"] = input("Please input the category for this mod.\n")

        if ask_name in nos:
            new_toml["display_name"] = os.path.basename(paths)
        else:
            new_toml["display_name"] = input("Please input a display name for this mod.\n")

        if ask_author in nos:
            new_toml["authors"] = "null"
        else:
            new_toml["authors"] = input("Please input the author(s) for this mod.\n")

        if ask_desc in nos:
            new_toml["description"] = "null"
        else:
            new_toml["description"] = input("Please input the description for this mod.\n")

        if ask_ver in nos:
            new_toml["version"] = "0.0"
        else:
            new_toml["version"] = input("Please input the version for this mod.\n")

        with open(os.path.join(mods_path, paths, "info.toml"), "w+") as fp:
            toml.dump(new_toml, fp)

if __name__ == "__main__":
    path = sys.argv[1]
    ask_name = input("Would you like me to ask for the Display Name on each toml generation?\nIf this is no, the display name will be the name of the directory\n")
    while ask_name not in valid_answers:
        print(f"Invalid answer! valid answers are: \n{valid_answers}")
        ask_name = input("Would you like me to ask for the Display Name on each toml generation?\n")
    ask_author = input("Would you like me to ask for the author on each toml generation?\nIf no, the author will be blank.\n")
    while ask_author not in valid_answers:
        print(f"Invalid answer! valid answers are: \n{valid_answers}")
        ask_author = input("Would you like me to ask for the author on each toml generation?\n")
    ask_desc = input("Would you like me to ask for the description on each toml generation?\nIf no, the description will be blank.\n")
    while ask_desc not in valid_answers:
        print(f"Invalid answer! valid answers are: \n{valid_answers}")
        ask_desc = input("Would you like me to ask for the description on each toml generation?\n")
    ask_ver = input("Would you like me to ask for the version number on each toml generation?\nIf no, the program will default to \"0.0\"\n")
    while ask_ver not in valid_answers:
        print(f"Invalid answer! valid answers are: \n{valid_answers}")
        ask_ver = input("Would you like me to ask for the version number on each toml generation?\n")
    ask_cat = input("Would you like me to ask for the category on each toml generation?\nIf no, the program will try to guess which category it is, which may be inaccurate.\n")
    while ask_cat not in valid_answers:
        print(f"Invalid answer! valid answers are: \n{valid_answers}")
        ask_cat = input("Would you like me to ask for the category on each toml generation?\n")
    main(path, ask_name.lower(), ask_author.lower(), ask_desc.lower(), ask_ver.lower(), ask_cat.lower())
