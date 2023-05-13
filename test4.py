from functools import wraps 
#定义一个装饰器名称的类
class  with_para_decorator: 
    #在类的__init__函数内接受装饰器参数，并赋值给类的实例参数，这样可以让其他函数随时使用
    #当然，如果装饰器没有参数，此处不转a,b即可，相当于类无参实例化
   def __init__(self,a,b):    
        self.a=a
        self.b=b
    #在类的__call__函数内接受被装饰函数，并具体定义装饰器
   def __call__(self,func):   
     @wraps(func)
     def wrap_function(arg1,arg2):  
        print('装饰带参数的函数，函数传的参数为：{0}, {1}'.format(arg1,arg2))
        print('带参数的装饰器，装饰器传的参数为：{0}, {1}'.format(self.a,self.b))
        return func(arg1,arg2)   
   
     return wrap_function
   #使用装饰器


@with_para_decorator(1,2)  
def need_decorate(a,b):   
  pass
need_decorate(4,5) 

class SetOnceMappingMixin:
    """自定义混入类"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


my_dict= SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)