from runpodctl_wrapper import wrapper

api_key = "4PU8543LX8X8GW4BKFIQAUBYDC5YXZZKHUCXIEL0"
api = wrapper(api_key, "mtvgi030214")
api.version()

def main():
    filename = input("Enter the filename you wish to transfer: ")
    api.send(filename)
    

if __name__ == "__main__":
    main()