class fib(object):
    
    def __init__(self,num):
        self.num=num
        self.a,self.b=0,1
        self.idx=0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx<self.num:
            self.a,self.b=self.b,self.a+self.b
            self.idx+=1
            return self.a
        raise StopAsyncIteration()

f=fib(8)
print(next(f))

def avg():
    tatol,count=0,0
    avg_value=None
    while True:
        value=yield avg_value
        tatol,count=tatol+value,count+1
        avg_value=tatol/count

gen = avg()
next(gen)
print(gen.send(30))
print(gen.send(20))
print(gen.send(10))