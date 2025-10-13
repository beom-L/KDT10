################### 35.5 연습문제 #######################
class Date :
    
    @staticmethod
    def is_date_valid(data):
        data = data.split('-')
        month = int(data[1])
        day   = int(data[2])
        return 12 >= month > 0 and 31 >= day > 0 


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')


# ################### 35.6 심사문제 ######################
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return cls(hour, minute, second)

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else :
    print("잘못된 시간 형식입니다.")


################## 36.8 연습문제 #####################
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new


x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)


################### 36.9 심사문제 ####################

class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')


class Bird(Animal, Wing):
    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

'''
먹다
파닥거리다
날다
True
True
'''

################## 37.2 연습문제 ###################
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

rect = Rectangle(x1=20, y1=20, x2=40, y2=30)

area = (rect.x2 - rect.x1) * (rect.y2 - rect.y1)

print(area)


################# 37.3 연습문제 ###################
import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

# 10 10 20 20 30 30 40 40
for i in range(3):
    length += math.sqrt((p[i+1].x - p[i].x)**2 + (p[i+1].y - p[i].y)**2)

print(length)