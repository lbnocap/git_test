from abc import ABCMeta,abstractmethod
class employee(object,metaclass=ABCMeta):
    #员工初始化
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name
    @abstractmethod
    def get_salary(self):
        #获得月薪
         pass
class manager(employee):
    #经理
    def get_salary(self):
        return 15000.0
class coder(employee):
    def __init__(self, name,work_hours=0):
        employee.__init__(self, name)
        self._work_hours=work_hours
    @property
    def work_hours(self):
        return self._work_hours
    @work_hours.setter
    def work_hours(self,work_hours):
        if work_hours>0:
            self._work_hours=work_hours
        else:
            0
    def get_salary(self):
        return 150*self._work_hours
class salesman(employee):
    def __init__(self, name,sales=0):
        employee.__init__(self,name)
        self._sales=sales
    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self,sales):
        if sales>0:
            self._sales=sales
        else:
            0
    
    def get_salary(self):
        return 1200+self._sales*0.5
def main():
    emps=[manager("刘波"),coder("干儿子"),salesman("干爹"),manager("bob"),salesman("tom"),coder("jerry")]
    for emp in emps:
        if isinstance(emp,coder):
            emp.work_hours=int(input("请输入%s本月的工作时间"%emp.name))
        elif isinstance(emp, salesman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()