from flask import Flask
from time import sleep


code = 0

# def textC(self):
#     print(self)
class text:
    def __init__(self, message):
        self.message = message
        self.print_message()
    def print_message(self):
        print(self.message)
        

    def reset_formatting():
        print('\033[0;0m')
    def plain(self):
        print('\033[0;0m' + self)
    def red(self):
        print('\033[31m' + self)
    def green(self):
        print('\033[32m' + self)
    def yellow(self):
        print('\033[33m' + self)
    def blue(self):
        print('\033[34m' + self)
    def purple(self):
        print('\033[35m' + self)
    def cyan(self):
        print('\033[36m' + self)
    def white(self):
        print('\033[38m' + self)
    def black(self):
        print('\033[30m' + self)
    def customcode(code, self):
        print(f"\033[{code}m"+self)
    def bold(self):
        print('\033[1m'+self)
    def underline(self):
        print('\033[4m'+self)
    def italic(self):
        print('\033[3m'+self)
    def strikethrough(self):
        print('\033[9m'+self)
    def orange(self):
        print('\033[38;5;202m' + self)


class pause:
    def __init__(self):
        sleep(int(self) / 1000)
    def secs(self):
        sleep(int(self))
    def mins(self):
        sleep(int(self) * 60)

def web(self):
    app = Flask(__name__)
    @app.route('/')
    def hello_world():  # put application's code here
        return self
    app.run()
    quit()

def conditional(condition, true, false): #not working
    return {True: true, False: false}[condition]



