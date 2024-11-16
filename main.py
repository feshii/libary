class  libary:
    def __init__(self, name, version):
        self.name = name
        self.version = version
    def display(self):
        print(f"Name: {self.name}, Version: {self.version}")
l1 = libary("Django", 3.0)
l1.display()