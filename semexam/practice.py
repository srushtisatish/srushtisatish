class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def hike(self,salary):
        self.salary=salary
        if salary<10000:
            total_salary=salary+(salary*30)/100
        elif 10000<=salary<20000:
            total_salary=salary+(salary*20)/100
        print(total_salary)
obj=Employee("raj",123)
obj.hike(15000)
