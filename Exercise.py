#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
'''
'''
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

    '''
# map()函数的使用方法
'''
def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))    
'''

# filter()函数的使用方法
'''
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
'''
'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始化序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
    '''

# yield运行规则，第一次循环，return；第二次从中断处开始
'''
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))
print("*"*20)
print(next(g))
'''
'''
# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
'''
'''
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
'''

#def is_odd(n):
#    return n % 2 == 1
#L = list(filter(is_odd, range(1, 20)))
#改造匿名函数
#L = list(filter(lambda x: x % 2 == 1, range(1,20)))
#print(L)

'''def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        b_time = time.time()
        print('begin call')
        value = fn(*args, **kw)
        print('end call')
        f_time = time.time()
        print('%s executed in %s ms' % (fn.__name__, str((f_time - b_time)* 1000)))
        return value
    return wrapper'''

'''
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.set_gender(gender)

    def get_gender(self) :
        return self.__gender

    def set_gender(self, gender) :
        if isinstance(gender, str) == False : raise ValueError('参数类型错误!')

        gender = gender.lower()
        if gender in ('male', 'female') :
            self.__gender = gender
        else :
            raise GenderError()
'''
'''
class GenderError(Exception) :
   

    def __init__(self) :
        pass
    def __str__(self):
        return '输入的性别错误! 只允许输入"male"或"female"(不区分大小写)'
'''


'''
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)
'''

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1