from __future__ import annotations

class MyClass(object):
    def __init__(self, my_number: int = 0):
        self.my_number: int = my_number

    def say(self, string: str = "Hello"):
        print(string)

    def show_my_number(self):
        print(self.my_number)