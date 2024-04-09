Setup:

Move the python files into a folder.
Create a outputs folder
    MAKE SURE ITS NAME IS "outputs"

In the outputs folder the code will create a folder for each model you use.
In these fodlers is where the pictures will be created. 
    DO NOT ADD FILES, CREATE FILES, OR RENAME FILES IN THESE FODLERS OR THE "outputs" FOLDER

In your terminal before trying to run anything, run the following commands
    python3 -m pip install -r requirements.txt

    MAKE SURE THE TERMINAL IS IN THE SAME DIRECTORY AS THE PYTHON FILES AND THE requirements.txt file

Start the runpod using the template:
    Stable Diffusion Kohya_ss ComfyUI Ultimate

press connect
press port 8888 for jynper notebook (Moving files and setup)
press port 3000 for a1111 webui

On first startup:
connect to jynper notebook: Jup1t3R
on the left side you will have the files
go to the stable-diffusion folder   
find the file "webui-user.sh"
open it with editor 
in the command_line_args add --share
ex: 
COMMAND_LINE_ARGS = "*all the other shit* --share"

After you have added this restart the pod

Log into the jynper notebook after restarting pod.
Open and run the following command:
    tail -f /workspace/logs/webui.log

copy the public link (ending with .gradio.live) into the code. 

change the shit you need in prompts/ and main.py
and run main.py

in the terminal should be either
    python main.py
or
    python3 main.py

in vs code:
left side, debug, run and debug
or
top right, play button
