import subprocess
import os
import time

class wrapper():

    def __init__(self, api_key:str, code:str):
        self.api_key = api_key
        self.code = code
        self.command = "runpodctl"
        self.cwd = os.getcwd()
        self.config()
    '''
    def run_cmd(self, cmd):
        process = subprocess.Popen(f"{self.runpod_path} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout, stderr
    '''
    def run_cmd(self, operation):
        full_command = f"{self.command} {operation}"
        # Start the process and open a pipe to its output
        process = os.popen(full_command)

        # Iterate over the output
        for line in process:
            print('Got line from subprocess: ', line.strip())

        # Check the exit status
        exit_status = process.close()
        if exit_status is not None:
            print(f"Command failed with exit status {exit_status}")
            
    def version(self):
        self.run_cmd("version")

    def send(self, filename):
        print("Sending file: ")
        self.run_cmd(f"send {filename}")

    def receive_file(self, code):
        stdout, stderr = self.run_cmd(f"receive {code}")
        self.handle_response(stderr, stdout)

    def start_pod(self, podId, bid=None):
        cmd = f"start pod {podId}"
        if bid:
            cmd += f" --bid={bid}"
        stdout, stderr = self.run_cmd(cmd)
        self.handle_response(stderr, stdout)

    def stop_pod(self, podId):
        stdout, stderr = self.run_cmd(f"stop pod {podId}")
        self.handle_response(stderr, stdout)

    def config(self):
        runpod_path = os.path.join(self.cwd, 'runpodctl.exe')
        current_path = os.environ["PATH"]
        os.environ['PATH'] = f"{runpod_path}:{current_path}"

    def get_pod(self):
        stdout, stderr = self.run_cmd(f"get pod")
        self.handle_response(stderr, stdout)
    
    def handle_response(self, error, output):
        if error:
            print(f'Error: {error}')
        else:
            print(f'Success: {output}')
