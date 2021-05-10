class employee():
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.id=id
        self.salary=salary
emp1=employee("Praveen", 20, "A1A", 50000)
emp2=employee("Jithu", 20, "A2A", 60000)
print(emp1.__dict__ ,"\n",emp2.__dict__)
