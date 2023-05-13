class thing(object):
    def __init__(self,name,price,weight):
        self.name=name
        self.price=price
        self.weight=weight

    @property
    def value(self):
        return self.price/self.weight

def input_thing():
    print("输入物品信息")
    name,price,weight=input("name"),input("price"),input("weight")
    return name,int(price),int(weight)

def main():
    max_weight,num_of_things=int(input("请输入总重量")),int(input("请输入物品数量"))
    all_thing=[]
    for _  in range(num_of_things):
        all_thing.append(thing(*input_thing()))
    all_thing.sort(key=lambda x:x.value,reverse=True)
    total_weight=0
    total_price=0
    for thing1 in all_thing:
            if total_weight+thing1.weight<=max_weight:
                print(f"小头拿走了{thing1.name}")
                total_price+=thing1.price
                total_weight+=thing1.weight
    print(f"小偷一共偷了{total_price}美元")

if __name__=="__main__":
            main()
