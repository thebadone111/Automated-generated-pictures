import os
import json 

def get_filename(dicotionary, itter, seed: bool):
    if seed:
        filename = f"{itter}_{dicotionary}.png"
        return filename
    else:
        arr = dicotionary["parameters"].split(",")
        arr = arr[::-1]
        arr = arr[:17]
        dicotionary2 = {}
        for elem in arr:
            t, d = elem.split(":", 1)
            dicotionary2[t.replace(" ", "", 1)] = d.replace(" ", "", 1)
        seed = dicotionary2["Seed"]
        filename = f"{itter}_{seed}.png"
        return filename

def handle_dirs(t2i):
    cwd = os.getcwd()
    base_output_path = os.path.join(cwd, "output")
    base_dirs = os.listdir(base_output_path)

    path = os.path.join(base_output_path, t2i.model)
    if t2i.model not in base_dirs:
        os.mkdir(path)

    dirs = os.listdir(path)
    int_list = []

    for files in dirs:
        inter, seed = files.split("_")
        int_list.append(int(inter))

    if len(int_list) == 0:
        int_list.append(0)

    largest_int = max(int_list)
    return path, largest_int

def save_imgs(t2i, result):
    path, largest_int = handle_dirs(t2i)

    for j, i in enumerate(result.images):
        if t2i.seed != -1:
            filename = get_filename(t2i.seed, largest_int + j + 1, True)
        else:
            filename = get_filename(i.info, largest_int + j + 1, False)
        filepath = str(path) + "\\" +  filename
        logfile = str(path) + "\\" + filename[:-4] + "-log.txt"
        #i.save(filename, pnginfo=pnginfo)
        i.save(filepath)
        save_dict_to_file(logfile, i.info)
        print(f"Img saved to: {path}\\{filename}")
        largest_int += 1

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
def save_dict_to_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(json.dumps(content, indent=4, sort_keys=True))