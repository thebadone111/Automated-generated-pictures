from webuiapi import WebUIApi
import asyncio
from file_handler_copy import save_imgs
import random

class text2img_base:
    def __init__(self, url: str):
        self.url = url
        self.api = WebUIApi(baseurl=f'{url}/sdapi/v1')
        self.org_prompt: str = ""
        self.prompt: str = ""
        self.negative_prompt: str = ""
        self.hr_prompt: str = ""
        self.hr_neg_prompt: str = ""
        self.denoise_str: int = 0.3
        self.styles: list = []
        self.seed: int = -1
        self.subseed: int = -1
        self.subseed_str: int = 0
        self.sampler: str = ""
        self.batch_size: int = 1
        self.steps: int = 50
        self.cfg_scale: int = 7
        self.width: int = 768
        self.height: int = 768
        self.restore_face: bool = False
        self.tiling: bool = False
        self.upscaler: str = ""
        self.model = ""
        self.enable_hr: bool = True
        self.hr_scale:int = 2
        self.restore_faces: bool = False
        self.save_grid: bool = False
        self.save_samples: bool = False
        self.send_img: bool = True
        self.save_img: bool = True
        self.s_churn: int = 1
        self.hr_step: int = 0
        self.extras: list = []
        self.photo_types = []

    async def task_gen_img(self, use_async = False):
        task = await self.api.txt2img(enable_hr=self.enable_hr,        
                    denoising_strength=self.denoise_str,
                    hr_scale=self.hr_scale,
                    hr_upscaler=self.upscaler,
                    hr_second_pass_steps=self.hr_step,
                    prompt=self.prompt,
                    styles=self.styles,
                    seed=self.seed,
                    subseed=self.subseed,
                    subseed_strength=self.subseed_str,
                    sampler_name=self.sampler,
                    batch_size=self.batch_size,
                    steps=self.steps,
                    cfg_scale=self.cfg_scale,
                    width=self.width,
                    height=self.height,
                    restore_faces=self.restore_faces,
                    tiling=self.tiling,
                    do_not_save_grid=self.save_grid,
                    do_not_save_samples=self.save_samples,
                    negative_prompt=self.negative_prompt,
                    send_images=self.send_img,
                    save_images=self.save_img,
                    s_churn=self.s_churn,
                    use_async=use_async
                    )
        
        return task

    def generate_images(self, num_of_imgs):
        result = asyncio.run(self.gen_img(num_of_imgs))
        return result
    
    async def gen_img(self, num_of_imgs):
        progress_task = asyncio.create_task(self.get_progress())
        
        images = []
        counter = 0
        for imgs in range(0, num_of_imgs):
            imgs += 1
            print(f"Generating picture: {imgs}")
            if len(self.extras) == 0:
                temp_prompt = self.org_prompt.replace("<<extras>>", "")
            else:
                if counter > len(self.extras):
                    counter = 0
                extras_string = self.extras[counter] + ", "
                temp_prompt = self.org_prompt.replace("<<extras>>", extras_string)

            types_string = random.choice(self.photo_types)
            self.prompt = temp_prompt.replace("<<type>>", types_string)
            print(f"Generating with prompt: \n {self.prompt}")
            img = await self.task_gen_img(True)
            save_imgs(self, img)
            images.append(img)
            print(f"Done with picture: {imgs}")
            counter += 1

        progress_task.cancel()
        try:
            await progress_task
        except asyncio.CancelledError:
            pass

        return images   
    
    async def get_progress(self):
        while True:
            prog = self.api.get_progress()
            print(f"Progress: {round(float(prog['progress']) * 100, 1)}%")
            print(f"Eta: {round(prog['eta_relative'], 2)}s")
            await asyncio.sleep(1)

    def get_models(self):
        models = self.api.get_sd_models()
        model_names = [model['model_name'] for model in models]
        return model_names
    
    def get_samplers(self):
        samplers = self.api.get_samplers()
        sampler_names = [sampler['name'] for sampler in samplers]
        return sampler_names
    
    def get_styles(self):
        styles = self.api.get_prompt_styles()
        return styles

    def get_loras(self):
        loras = self.api.get_loras()
        lora_names = [lora['name'] for lora in loras]
        return lora_names
    
    def get_embeddings(self):
        embs = self.api.get_embeddings()
        loaded_keys = list(embs["loaded"].keys())
        return loaded_keys

    def get_upscalers(self):
        scalers = self.api.get_upscalers()
        scaler_names = [scaler['name'] for scaler in scalers]
        return scaler_names
    
    def get_current_settings(self):
        options = self.api.get_options()
        return options

    def set_settigns(self, options: dict):
        response = self.api.set_options(options)
        return response
    

if __name__ == "__main__":
    tti = text2img_base()
    tti.export_settings("config.json")