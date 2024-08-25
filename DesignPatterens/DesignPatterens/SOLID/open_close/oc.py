from enum import Enum


class Color(Enum):
    RED=1
    GREEN=2
    BLACK=3

class Size(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3

class Product:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size


# OCP open for extension , closed for modification


## BAD APPROACH
class ProductFilter:
    def filter_by_color(self,products,color):
        for p in products:
            if p.color==color:
                yield p

    def filter_by_size(self,products,size):
        for p in products:
            if p.size==size:
                yield p

    def filter_by_size_and_color(self,products,size,color):
        for p in products:
            if p.size==size and p.color==color:
                yield p

    def filter_by_size_or_color(self,products,size,color):
        for p in products:
            if p.size==size or p.color==color:
                yield p



## SPECIFICATION

class Specification:
    def is_satisfied(self,item):
        pass

class Filter:
    def filter(self,items,spec):
        pass


## FILTER BY COLOR

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color=color
    def is_satisfied(self,item):
        return item.color==self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self,*args):
        self.args=args

    def is_satisfied(self,item):
        return all(map(
            lambda spec:spec.is_satisfied(item),self.args
        ))
class BetterFilter(Filter):
    def filter(self,items,spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item



#TEST

if __name__ =='__main__':
    apple=Product("Apple",Color.GREEN,Size.LARGE)
    apple1 = Product("Apple2", Color.RED, Size.SMALL)
    apple3 = Product("Apple3", Color.GREEN, Size.LARGE)
    products=[apple,apple1,apple3]

    # old
    pf=ProductFilter()
    print("Green products old--------")
    for p in pf.filter_by_color(products,Color.GREEN):
        print(f"Product name {p.name} is Green")

    ## better filer
    bf=BetterFilter()
    green=ColorSpecification(Color.GREEN)
    for p in bf.filter(products,green):
        print(f"Product name {p.name} is Green")

    # large products
    large=SizeSpecification(Size.LARGE)
    for p in bf.filter(products,large):
        print(f"Product name {p.name} is Large")

    ## large green
    print("------------------------------------")
    large_green=AndSpecification(large,green)
    for p in bf.filter(products,large_green):
        print(f"Product name {p.name} is Large")
