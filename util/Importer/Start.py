#Importer start modual

class Start():

    def __init__(self):
        #setup file path enviroment
        try:
            import os
            separator = "\\"
            filePathArray = []
            filePath = os.path.realpath(__file__)
            filePathArray = filePath.split(separator) #creates array out of string
            filePathArray.remove("itemImporter.py")
            dirPath = separator.join(filePathArray)
            os.chdir(dirPath) #sets work path

        except Exception as e:
            print(e)
            print("Error Setting Up Work Enviroment Path")
            print("Errors Expected")

        Start.imports()
        Main()
    
    def imports():
       #all moduals are imported within this function
        try:
            global os, Main
            import os, Main
            return

        except ModuleNotFoundError as e:
            print("Error Detected")
            e = str(e)
            return e
        else:
            pass

if __name__ == "__main__":
    Start()
else:
    pass