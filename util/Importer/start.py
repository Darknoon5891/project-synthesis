class Start():

    def __init__(self):
        #setup file path enviroment
        try:
            global os
            import os
            separator = "\\"
            filePathArray = []
            filePath = os.path.realpath(__file__)
            filePathArray = filePath.split(separator) #creates array out of string
            filePathArray.remove(filePathArray[-1]) #removes file name from path
            dirPath = separator.join(filePathArray)
            os.chdir(dirPath) #sets work path

        except Exception as e:
            print("Error Setting Up Work Enviroment Path")
            print("Errors Expected")

        try:
            global main

            import main

            return 

        except ModuleNotFoundError as e:
            print("Module Error Detected")

        #run required pre-main functions
   
        main.Main()
    

if __name__ == "__main__":
    Start()
else:
    print("please run via start")