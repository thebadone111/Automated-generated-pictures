import os
import json

def get_filename(dictionary, iteration, seed: bool):
    try:
        if seed:
            filename = f"{iteration}_{dictionary}.png"
        else:
            parameters = dictionary.get("parameters", "").split(",")
            seed = {param.split(":")[0].strip(): param.split(":")[1].strip() for param in parameters[::-1][:17]}.get("Seed", "")
            filename = f"{iteration}_{seed['seed']}.png"
        return filename
    except Exception as e:
        print(f"Error in get_filename: {e}")
        filename = f"{iteration}_00000"
        return filename
    
def handle_dirs(t2i):
    try:
        cwd = os.getcwd()
        base_output_path = os.path.join(cwd, "output")
        os.makedirs(base_output_path, exist_ok=True)

        path = os.path.join(base_output_path, t2i.model)
        os.makedirs(path, exist_ok=True)

        int_list = [int(file.split("_")[0]) for file in os.listdir(path) if "_" in file]
        largest_int = max(int_list, default=0)
        return path, largest_int
    except Exception as e:
        print(f"Error in handle_dirs: {e}")
        exit()

def save_imgs(t2i, result):
    try:
        path, largest_int = handle_dirs(t2i)
        if path is None:
            return

        for j, i in enumerate(result.images):
            filename = get_filename(t2i.seed if t2i.seed != -1 else i.info, largest_int + j + 1, t2i.seed != -1)
            if filename is None:
                continue
            filepath = os.path.join(path, filename)
            logfile = os.path.join(path, filename[:-4] + "-log.txt")
            i.save(filepath)
            save_dict_to_file(logfile, i.info)
            print(f"Img saved to: {os.path.join(path, filename)}")
    except Exception as e:
        print(f"Error in save_imgs: {e}")
        exit()

def open_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as infile:
            return infile.read()
    except Exception as e:
        print(f"Error in open_file: {e}")
        exit()
    
def save_dict_to_file(filepath, content):
    try:
        with open(filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(content, indent=4, sort_keys=True))
    except Exception as e:
        print(f"Error in save_dict_to_file: {e}")
        exit()