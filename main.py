class Animal:
    education = 'Animals'
    group = 'Home'
    weight = 5
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print('Создался объект')



an1 = Animal(name='Dog', age=5, weight=3)
an2 = Animal(name='Cat', age=11, weight=10)
print(an1.name)
print(an2.name)
print(an1.age)
print(an2.age)
an1.weight - 3
an2.weight - 10
print(an1.weight)
print(an2.weight)
print(Animal.weight)


class Car:
    education = 'Auto'
    type = "sedan"
    age = 20
    def __init__(self, mark, model, age):
        self.mark = mark
        self.model = model
        self.age = age
        print('Создался объект')



cr1 = Car(mark='bmw', model=230, age=7)
cr2 = Car(mark='ford', model=150, age=10)
print(cr1.mark)
print(cr2.mark)
print(cr1.model)
print(cr2.model)
cr1.age - 7
cr2.age - 10
print(cr1.age)
print(cr2.age)
print(Car.age)