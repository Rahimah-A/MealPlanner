'''
Created on Feb 4, 2019

@author: Rahimah
'''
class Plan(object):
    '''this class creates a meal object'''
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        
    def get_breakfast(self):
        return self.breakfast
    
    def get_lunch(self):
        return self.lunch
    
    def get_dinner(self):
        return self.dinner
    