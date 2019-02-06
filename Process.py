'''
Created on Jan 31, 2019

@author: Rahimah
'''

class Process(object):
    '''
    This class creates food objects
    '''
    def __init__(self, food_type, name, calories):
        '''
        Constructor
        '''
        self.food_type = food_type
        self.name = name
        self.calories = calories
        
    
    def get_type(self):
        return self.food_type
    
    def get_name(self):
        return self.name
    
    def get_calories(self):
        return self.calories
    
