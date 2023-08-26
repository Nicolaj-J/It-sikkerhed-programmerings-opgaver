import platform
import os


cwd = os.getcwd()
while True:
    try:
        choice = int(input("Do you want to make a venv[1] or install pycodestyle and pipregs[2]? \n"))
        break
    except ValueError:
        print("Write 1 or 2 to select an option")
if choice == 1:
    virtual_env_name = input("Write the name of the venv: ")
    operating_system = platform.system()
    match operating_system:
        case "Linux":
            try:
                import virtualenv
            except ImportError:
                os.system("pip install virtualenv")
            os.system(f"virtualenv {virtual_env_name}")
            print("---"*10)
            print("Write the line below to activate the venv")
            print(f"source {virtual_env_name}/bin/activate")
        case "Windows":
            try:
                import virtualenv
            except ImportError:
                os.system("pip install virtualenv")
            os.system(f"virtualenv {virtual_env_name}")
            print("---"*10)
            print("Write the line below to activate the venv")
            print(f"{virtual_env_name}\\Scripts\\activate")
                
        case "Darwin":
            print("Your os is not supported yet")
elif choice == 2:
    try:
        import pycodestyle
    except ImportError:
        os.system("pip install pycodestyle")
    try:
        import pipreqs
    except ImportError:
        os.system("pip install pipreqs")