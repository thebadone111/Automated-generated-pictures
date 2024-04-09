from file_handler import open_file
from classes import text2img_base
import os

'''
This section of the code is used to establish a connection to the API tunnel of the runpod.
1. Modify the webui-user.sh file to add --share
2. Restart the pod
3. Open a terminal and run "tail -f /workspace/logs/webui.log"
Find the .gradio.live link and paste it below (public link)
'''

url = "https://.....gradio.live"

t2i = text2img_base(url)
cwd = os.getcwd()
prompt_path = os.path.join(cwd, "prompts/prompt.txt")
neg_prompt_path = os.path.join(cwd, "prompts/negative_prompt.txt")
hr_prompt_path = os.path.join(cwd, "prompts/hr_prompt.txt")

'''
This section of the code is used to set various parameters for the image generation.
1. The prompt: This will be the same for all the pictures (base prompt)
        Change the prompt.txt file for changes here
        You can have stuff after <<extras>>, add them straight on, do not add ', ', that is done automatically
2. The loras: check the stuff.json file / run restart.py# Load the prompts from the files
3. Negative prompt is the negative prompt (embeddings, run restart.py / check stuff.json)
    with open(prompt_path, 'r') as file:
        prompt = file4. hr_prompt / hr_lora is the high res / upscaler prompt and loras
        Add the extras you want on top of the normal prompt
5. Extras, these are the different prompts for each photo to generate,
    If you try to generate more photos than what you have extras then you will it will loop around
'''
prompt = open_file(prompt_path).replace("\n", "")
negative_prompt = open_file(neg_prompt_path).replace("\n", "")
lora = "<lora:lora_name:0.5>"


hr_prompt = open_file(hr_prompt_path).replace("\n", "")
hr_lora = "<lora:lora_name:0.5>"

extras = [
    "",
]

type_photo = [
        "modernist photo"
]

'''type_photo = [
        "beauty photo", # 0
        "candid photo", # 1 
        "glamour photography",
        "high fashion photography",
        "modernist photo",
        "pictorialist style photo",
        "street fashion photography" # 6
]'''

'''
This section of the code is used to set the picture settings.
For a full list of settings, refer to classes.py
'''

amount_of_pictures: int = 1 # Amount of pictures you wish to generate


def setup():
    global prompt
    global negative_prompt
    global hr_prompt
    global lora
    global hr_lora
    global type_photo
    global extras
    t2i.width = 512
    t2i.height = 512
    t2i.steps = 40
    t2i.hr_step = 20 # Upscaler steps
    t2i.hr_scale = 2 # Upscale by x
    t2i.cfg_scale = 8
    t2i.denoise_str = 0.3
    t2i.upscaler = "R-ESRGAN 4x+"
    t2i.model = "model name"
    t2i.sampler = "DPM++ 2M SDE Karras"
    t2i.photo_types = type_photo # Random from the list above
    t2i.seed = -1 # -1 random
    t2i.subseed = -1 # -1 random
    t2i.subseed_str = 0
    clip_skip: float = 2.0
    t2i.batch_size = 1
    sd_vae: str = "Automatic"
    sd_vae_as_default: bool = True 

    # Set class vars, permanent
    prompt = prompt + ", " +  lora
    hr_prompt = hr_prompt + ", " + hr_lora
    t2i.org_prompt = prompt
    t2i.negative_prompt = negative_prompt
    t2i.hr_prompt = hr_prompt if hr_prompt != "" else prompt
    t2i.hr_neg_prompt = negative_prompt
    t2i.extras = extras
    options = {}
    options['sd_model_checkpoint'] = t2i.model
    options['CLIP_stop_at_last_layers'] = clip_skip
    options['sd_vae_as_default'] = sd_vae_as_default
    options['sd_vae'] = sd_vae
    res = t2i.set_settigns(options)

def main(itter = 1):
    # generate picture
    res = t2i.generate_images(itter)
    #print(res)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    setup()
    main(itter=amount_of_pictures)
    print("Done!!")