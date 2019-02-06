import csv
import random
from Process import Process
from Plan import Plan
'''
Created on Jan 18, 2019

@author: Rahimah
'''

meals = []
meal_plan = []

''' reads the csv file and separates the rows to be processed as a meal object.
    meal object is then appended to meal list of objects. Meal objects are randomly selected for each day of the week.'''
class Read:
    def process_file(self, name):
        self.name = name
        with open(self.name, mode = 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter =',')
            for row in csv_reader:
                    meals.append(Process(row[0].lower(), row[1], row[2]))
                    
            self.create()
    
    def create(self):
        plan = 5
        day = 0
        for day in range(day, plan):
            b = self.get_rand('breakfast')
            l = self.get_rand('lunch')
            d = self.get_rand('dinner')
            meal_plan.append(Plan(b,l,d))
        
        self.print_plan()
    
    def print_plan(self):
        for i in range(0,len(meal_plan)):
            print( self.get_day(i), ": ", "\nbreakfast - ", meal_plan[i].breakfast, "\nlunch - ", meal_plan[i].lunch, "\ndinner - ", meal_plan[i].dinner, "\n")
            
            
    def get_rand(self, food_set):
        ran = random.choice(meals)
        if ran.food_type == food_set and ran.name is not None:
            return ran.name
        else: 
            return self.get_rand(food_set)
    def get_day(self, d):
        if d == 0:
            day = "Monday"
        elif d == 1:
            day = "Tuesday"
        elif d == 2:
            day = "Wednesday"
        elif d == 3:
            day = "Thursday"
        elif d == 4:
            day = "Friday"
        return day
        
def main():
    p = Read()
    p.process_file('meals.csv')
    
if __name__ == '__main__':
    main()
