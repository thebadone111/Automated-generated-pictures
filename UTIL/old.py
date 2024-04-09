'''
def entry():
    # Get user inputs
    # Model
    models = t2i.get_models()
    model_select = int(input("Choose your model(num only): "))
    t2i.model = models[model_select]["title"]
    os.system('cls')

    # Sampler
    samplers = t2i.get_samplers()
    sample_select = int(input("Choose your sampler(num only): "))
    t2i.sampler = samplers[sample_select]["name"]
    os.system('cls')

    # Prompt style
    also_prompt = "a"
    styles = t2i.get_styles()
    style_select = int(input("Choose your style: "))
    if style_select == -1:
        t2i.styles = []
    else:
        t2i.styles = [styles[style_select]["name"]]
        also_prompt = input("Do you also want to use the prompt? (Y/n): ")
        also_prompt = also_prompt.lower()
        if also_prompt == "n":
            t2i.prompt = ""
            t2i.hr_prompt = ""
        also_neg_prompt = input("Do you also want to use the negative prompt? (Y/n): ")
        also_neg_prompt = also_neg_prompt.lower()
        if also_neg_prompt == "n":
            t2i.negative_prompt = ""
            t2i.hr_neg_prompt = ""
    os.system('cls')

    # Use async (run the requests in parallel)
    while True:
        use_async = "n"
        async_select = input("Do you want to run the requests in parallel? (Y/n): ")
        async_select = async_select.lower()
        if len(async_select) != 1:
            os.system('cls')
            continue
        elif async_select != "n" and async_select != "y":
            os.system('cls')
            continue
        else:
            break
    
    if use_async == "n":
        use_async = False
    elif use_async == "y":
        use_async = True
    else:
        use_async = False

    # Choose seed
    seed = input("Choose your seed (default and random -1): ")
    if len(seed) > 0:
        int(seed)
        t2i.seed = seed

    sub_seed = input("Choose your sub seed (default and random -1): ")
    if len(sub_seed) > 0:
        int(sub_seed)
        t2i.subseed = sub_seed

    subseed_str = input("Choose your subseed strength (default 0): ")
    if len(subseed_str) > 0:
        float(subseed_str)
        t2i.subseed_str = subseed_str

    # Choose lora
    while True:
        loras = t2i.get_loras()
        lora_select = input("Choose the lora you want to add to the prompt (-1 to exit): ")
        
        try:
            lora_select = int(lora_select)
            if lora_select == -1:
                break
            strength = input("Choose the strength of your lora: ")
            strength = float(strength)
            lora = loras[lora_select]
            t2i.org_prompt = f"{t2i.org_prompt}, <lora:{lora['alias']}:{strength}>"
        except:
            print("That did not work try again")
            continue
    
    # Customize prompt
        # ethnic
    ethincity = input("Choose the ethinicity of the model: ")
    t2i.org_prompt = t2i.org_prompt.replace("<<ethnicity>>", ethincity)
        # extras
 
    #full_extra = ""
    #while True:
    #    extra = input("Choose the extras you want to add to the prompt (Leave blank to exit): ")
    #    try:
    #        if len(extra) == 0:
    #            break
    #        full_extra += extra + ", "
    #    except:
    #        print("That did not work try again")
    #        continue
    #t2i.prompt = t2i.prompt.replace("<<extras>>", full_extra)


    print(f"You chose: ")
    print(f"    Sampler - {samplers[sample_select]['name']}")
    print(f"    Model - {models[model_select]['title']}") 
    print(f"    Style - {styles[style_select]['name']}")
    print(f"    Seed - {t2i.seed}")
    if also_prompt != "a":
        print(f"        Also prompt: {also_prompt}")
        print(f"        Also negative prompt: {also_neg_prompt}")
    print(f"Your prompt: {t2i.org_prompt}")
    con = input("Do you want to continue (Y/n): ")
    if con.lower() != "y":
        return
    options = {}
    options['sd_model_checkpoint'] = t2i.model
    res = api.set_options(options)
    if res:
        print(res, type(res))
    len_extra = len(extras)
    itter = int(input(f"How many pictures do you wish to generate (You have added {len_extra} extras, cannot run more than that): "))
    main(use_async, itter)
'''