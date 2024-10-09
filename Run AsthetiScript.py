'''
Run your code with this file (open in Command Prompt or press the run button)










(C) Copyright Tariq Tayebi - AsthetiScript
~~~~~~ Do NOT edit this code ~~~~~~















'''

username = input("Enter your username: For example, if path is C://Users//monid, username is monid > ")

def preprocess_code(code):
    # Replace // with #
    code = code.replace('!', '#')
    code = code.replace('>', '.')
    code = code.replace('using', 'import')
    code = code.replace('should', 'if')
    code = code.replace('var', 'f')
    code = code.replace('std', 'AsthetiScript')
    code = code.replace('-', 'as')

    return code

def execute_external_file(file_path):
    print('\033[0;0m')
    # Read the content of the external file
    with open(file_path, 'r') as file:
        code = file.read()

    # Preprocess the code
    preprocessed_code = preprocess_code(code)
    # Execute the preprocessed code
    exec(preprocessed_code)

# Path to the external Python file
external_file_path = f'C:\\Users\\{username}\\Downloads\\Main.asth' #change your file here
while True:
    asin = input("\033[38;5;202m" + "/Asthetiscript > " + '\033[0;0m')

    try:
        if asin == 'run':
            print('\033[0;0m')
            execute_external_file(external_file_path)
            print('\033[38;5;202m')
            asin = input('\033[0;0m' + "/Asthetiscript > ")
            print('\033[0;0m')
        elif asin == 'exit':
            quit('Terminal Shut Down')
        elif asin == 'clear':
            for i in range(30):
                print()
        elif asin == "change_file_path":
            external_file_path = input("File name/path: ")
        elif asin == "\n":
            continue
        else:
            print('\033[31m' + asin + " is not the name of a command or function")
            print('\033[0;0m')
    except FileNotFoundError:
        print('\033[31m' + external_file_path + " is not the name of a file or path. \nCheck that it is correct, than restart ")
        print('\033[0;0m')
    except AttributeError as e:
        print('\033[31m' + f'Error AttributeError: {e}. This is likely a problem with your code' + '\033[0m')
    except ValueError as e:
        print('\033[31m' + f'Error AttributeError: {e}. This is likely a problem with your code.' + '\033[0m')
    except SyntaxError as e:
        print('\033[31m' + f'Error AttributeError: {e}. This is likely a problem with your code.' + '\033[0m')
