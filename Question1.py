'''using the python object oriented programming scheme (OOPS) kindly complete the following task as shown below:
a) create a python class called circle with constructor which will take a list as an 
argument for the task. The list is :[10,501,22,37,100,999,87,351]

b) create proper member variables inside the task if required and use 
them when needed. For example for this task create a class private variable named pi = 3.141

c) from the given list create two class methods are and perimeter which will be going to calculate the area  and perimeter
'''

class circle:
    #constructor will be initialized when called
    def __init__(self,mylist):
        self.mylist=mylist
        self.__pi=3.14
        self.area_list=[]
        self.perimeter_list=[]

    #defining method to calculate the area of the circle
    def calculate_area(self):
        for radius in mylist:
            area=self.__pi*radius*radius
            self.area_list.append(area)
        return self.area_list
    
    #defining method to calculate the perimeter of the circle
    def calculate_perimeter(self):
        for radius in mylist:
            perimeter= 2*self.__pi*radius
            self.perimeter_list.append(perimeter)
        return self.perimeter_list

#providing the list input which is given in the question
mylist=[10,501,22,37,100,999,87,351]

#initiallizing the constructor
circle_object = circle(mylist)

#calling both the methods   
print(circle_object.calculate_area())
print(circle_object.calculate_perimeter())