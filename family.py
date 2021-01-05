class Family:
    place="kongad"

    def __init__(self,name,age):
        self.name=name
        self.age=age

santhosh=Family("santhu",29)
praveen=Family("jithu",20)
sushama=Family("udayipp",26)

print("Santhosh is from {}".format(santhosh.__class__.place))
print("Praveen is from {}".format(praveen.__class__.place))
print("Praveen is from {}".format(sushama.__class__.place))

print("{} is {} years old".format(santhosh.name,santhosh.age))
print("{} is {} years old".format(praveen.name,praveen.age))
print("{} is {} years old".format(sushama.name,sushama.age))
