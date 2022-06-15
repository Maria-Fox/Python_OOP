"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self,start = 0):
        ''' Create a serial number generator. Using start as the beginning number of the serial number'''
        self.start = self.next = start
        # why are we having this self also equal next? 

    def __repr__ (self):
        '''Show representation '''
        return f"Serial Number generator beginning = {self.start}, the next = {self.next}"

    def generate(self):
        '''Get start of serial numb. and return next serial number'''
        self.next += 1
        return self.next - 1 

    def reset(self):
        '''Return to original start value'''
        self.next = self.start 


# To run in ipython you create a variable with the class of SeriaalGenerator and pass in the starting value. Ex: 
# first_attepmpt = SerialGenerator(100)
# Then, when you need to generate or reset you use the variable name . mwthod(). Ex:
# first_attepmpt.generate() - do not add argument as self was assigned earlier during inititaion 
