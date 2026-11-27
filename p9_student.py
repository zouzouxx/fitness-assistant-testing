class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def average(self):
        total = 0
        for s in self.scores:
            total = s + total
        return total / len(self.scores)

xiaoming = Student("小明", [80, 90, 85])
print(xiaoming.average())
print(xiaoming.name)
