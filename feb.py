class people:
    name=""
    age=0
    _weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print("{} 说 我今年{}岁了".format(self.name,self.age))
class student(people):
    grade=""
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("{} 说 我今年{}岁了读{}年级了".format(self.name, self.age,self.grade))
class speaker(people):
    topic=""
    def __init__(self,n,a,w,t):
        people.__init__(self,n,a,w)
        self.topic=t
    def speak(self):
        print("我是{} 我今年{}岁了，演讲的主题是{}".format(self.name, self.age,self.topic))
class sample(student,speaker):
    __f=""
    def __init__(self,n,a,w,g,t,f):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,a,w,t)
        self.__f=f
    def speak(self):
        print("我是{} 我今年{}岁了读{}年级了，演讲的主题是{}".format(self.name, self.age, self.grade,self.topic))
    def __foo(self):
        print("这是私有方法")
    def fool(self):
        print("这是私有变量：{}".format(self.__f))
    def __str__(self):
        return "sample({},{},{},{},{},{})".format(self.age,self.grade,self.topic,self.__f,self.name,self._weight)
    def __add__(self, other):
        return sample(self.age+other.age,self.name+other.name,self.__f+other.__f,self.topic+other.topic,self._weight+other._weight,self.grade+other.grade)

test=sample("liubp",26,10,10,'python','siyou')
test_1=sample("liubo",20,20,20,'java','共有')
test.speak()
print(test+test_1)
