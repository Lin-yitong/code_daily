import time
######函数基础############

def add(a,b=10):
    return a+b

def show(*args,**kwargs):
    print(args)
    print(kwargs)

print(add(1,10))
print(add(10))

show(1,2,3,name='mike',age=35)

def hello():
    print("hello")

print(hello())
print(type(hello))

# hello是函数本身。加括号才是执行
a = hello
a()


########## 函数可以作为参数传递 ###########

def add(a,b=10):
    return a+b

def multiply(a,b=10):
    return a*b

def calculate(func,a,b=10):
    return func(a,b)

res1 = calculate(add,1,5)
res2 = calculate(multiply,1)
print(res1,res2)


##########  闭包 ############
def make_multipy(x):

    def multiply(y):
        return x * y

    return multiply

double = make_multipy(2)
triple = make_multipy(3)

print(double(10))
print(triple(10))


######## 装饰器 #######
def log(func):
    def wrapper(*args, **kwargs):
        print("执行开始")
        res = func(*args, **kwargs)
        print("执行结束")
        return res

    return wrapper

@log
def add(a,b=10):
    return a+b

print("decorate")
print(add(10,40))


# def time_count(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         func(*args, **kwargs)
#         end = time.perf_counter()
#         return end-start
#     return wrapper
#
# @time_count
# def write(num):
#     for i in range(num):
#         print(i)
#
#
# print(write(20))


# 装饰器不应该改变原函数的返回值
def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f"耗时：{end-start}")
    return wrapper

@time_count
def write(num):
    for i in range(num):
        print(i)


write(10)
