from classes import text2img_base
import json
from webuiapi import WebUIApi
from pprint import pprint
import os
from main import url

'''
Run this when you've added something to the runpod
REMEMBER TO SET THE URL IN main.py TO THE PUBLIC LINK 
'''

tti = text2img_base(url)

def save_all():
    options = tti.get_current_settings()
    base = {}
    base["options"] = options

    with open("settings.json", "w") as json_file:
        json.dump(base, json_file)

    print("Available settings: ")
    pprint(options, indent=4)


    base = {}
    embeddings = tti.get_embeddings()
    loras = tti.get_loras()
    models = tti.get_models()
    samplers = tti.get_samplers()
    upscalers = tti.get_upscalers()
    base["embeddings"] = embeddings
    base["loras"] = loras 
    base["models"] = models
    base["samplers"] = samplers
    base["upscalers"] = upscalers

    with open("stuff.json", "w") as json_file:
        json.dump(base, json_file)

    print("Available shit: \n")
    pprint(base, indent=4)
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    save_all()