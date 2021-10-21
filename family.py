class Family:
    place="kongad"

    def __init__(self,name,age):
        self.name=name
        self.age=age

santhosh=Family("Santhu",29)
praveen=Family("Jithu",20)
sushama=Family("Udayipp",25)

print("Santhosh is from {}".format(santhosh.__class__.place))
print("Praveen is from {}".format(santhosh.__class__.place))
print("Sushama is from{}".format(sushama.__class__.place))


print("{} is {} years old".format(santhosh.name,santhosh.age))
print("{} is {} years old".format(sushama.name,sushama.age))
print("{} is {} years old".format(praveen.name,praveen.age))