# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 07:26:59 2025

@author: Hp
"""

#L20 - fitness tracker oop example

# =============================================================================
# class SimpleWorkout(object):
#     def __init__(self, start, end, calories):
#         self.start = start
#         self.end = end
#         self.calories = calories
#         self.icon = '😒'
#         self.kind = 'workout'
#     def get_calories(self):
#         return self.calories
#     def get_start(self):
#         return self.start
#     def get_end(self):
#         return self.end
#     def set_calories(self, calories):
#         self.calories = calories
#     def set_start(self, start):
#         self.start = start
#     def set_end(self, end):
#         self.end = end
#         
# # -- a very simple class initiated
#         
# # print(SimpleWorkout.__dict__.keys())
# # print()
# # print(SimpleWorkout.__dict__.values())
# =============================================================================

from dateutil import parser
class Workout(object):
    cal_per_hr = 200   #class variable, everyone in class can read this, and from ourside the class def by usinng Workout.cal_per_hr
    
    def __init__(self, start, end, calories=None):
        self.start = parser.parse(start)  #so start and endtime are now a datetime object - we made it by the module parser, and now we can perform operations on them
        self.end = parser.parse(end)
        self.calories = calories #may be none if not mentioned
        self.icon = '😒'
        self.kind = 'Workout'
        
    def get_calories(self):
        if self.calories == None:
            return Workout.cal_per_hr*(self.end - self.start).total_seconds() / 3600 
        #total_sseconds() comes from parser module and converts every time into seconds
        else:
            return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def set_calories(self, calories):
        self.calories = calories
    def set_start(self, start):
        self.start = start
    def set_end(self, end):
        self.end = end
        
    def __str__(self):
        """Return a text-based graphical depiction of the workout"""
        width = 16
        retstr =  f"|{'–'*width}|\n"
        retstr += f"|{' ' *width}|\n"
        retstr += f"| {self.icon}{' '*(width-3)}|\n"  #assume width of icon is 2 chars - len('🏃🏽‍♀️');  doesn't do what you'd epxect
        retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
        retstr += f"|{' ' *width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
        cal_str = f"{round(self.get_calories(),1)}"
        retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"

        retstr += f"|{' ' *width}|\n"
        retstr +=  f"|{'_'*width}|\n"

        return retstr
    
    
########## YOU TRY IT ##########
w_one = Workout('Jan 1 2021 3:30pm', 'Jan 1 2021 4:00pm')
print(w_one.get_calories())

w_two = Workout('Jan 1 2021 3:35pm', 'Jan 1 2021 4:00pm', 300)
print(w_two.get_calories())
########## ########## ##########

#sublasses start
class RunWorkout(Workout):
    def __init__(self, start, end, elev=0, calories=None, route_gps_points=None):
        super().__init__(start, end, calories)  #calls parent's init method, we don't need to use Workout.__init__ everytime
        self.icon = '🏃🏻'     #overriding
        self.kind = 'Running'     #overriding
        self.elev = elev
        
    def get_elev(self):
        return self.elev
    def set_elev(self, e):
        self.elev = e
    def get_calories(self):
        if (self.route_gps_points != None):
            dist = 0
            lastP = self.route_gps_points[0]
            for p in self.route_gps_points[1:]:
                dist += gpsDistance(lastP,p)
                lastP = p
            return dist * RunWorkout.cals_per_km
        else:
            return super().get_calories()
        
    def __str__(self):
        super().__str__()
    
        
rw = RunWorkout("12/23/2021 5:00am", "12/23/2021 6:00am", 400)
print(rw)