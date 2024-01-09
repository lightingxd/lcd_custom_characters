from time import sleep
import pip

class textcolor:
	green = "\033[32m"
	blue = "\033[34m"
	yellow = "\033[33m"
	red = "\033[31m"
	reset = "\033[0m"

print(textcolor.green + "Now the script will install the libraries specified in requirements.txt" + textcolor.reset)
sleep(5)

try:
    #file = open('requirements.txt', 'r')
    #requirements = file.read()
    #filtered = " ".join(line.strip() for line in requirements.splitlines())
    
    def install(package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        else:
            pip._internal.main(['install', package])
    
    if __name__ == "__main__":
         install("-r requirements.txt")
    print(textcolor.green + 'Installing complete! ' + textcolor.reset)
except FileNotFoundError:
      print(textcolor.red + 'requirements.txt not found.' + textcolor.reset)
except PermissionError:
      print(textcolor.red + 'Permission denied.' + textcolor.reset)

