class parrot():

    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot cant swim")

class penguin():
     def fly(self):
        print("Penguin cant fly")
     def swim(self):
        print("Penguin can swim")

def flying_test(bird):
    bird.fly()

def swimming_test(bird):
    bird.swim()

blu=parrot()
peggy=penguin()

flying_test(blu)
flying_test(peggy)

swimming_test(blu)
swimming_test(peggy)