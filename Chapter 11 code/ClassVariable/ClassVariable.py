# Sample class
class Sample():

    nObjects = 0  # This is a class variable
    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print('There are', Sample.nObjects, 'Sample objects')

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1

# Instantiate 4 objects
oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')

# Delete one object
del oSample3

# Let's see how many we have:
oSample1.howManyObjects()
