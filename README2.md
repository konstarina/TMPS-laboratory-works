# ***TMPS Labaratory Work #2***
# ***Structural Design Patterns***

### Author: Constantinova Carina
----

## Objectives:

* Get familiar with the Structural Design Patterns;
* As a continuation of the previous laboratory work;
* Implement at least 3 CDPs for the specific domain;

## Creational Design Pattern:
 - [x] Adapter
 - [ ] Bridge
 - [ ] Composite
 - [x] Decorator
 - [x] Flyweight
 - [ ] Proxy

## Implementation:
#### Adapter
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.
The adapter design pattern solves these problems:
* How can a class be reused that does not have an interface that a client requires?
* How can classes that have incompatible interfaces work together?
* How can an alternative interface be provided for a class?
```python 
class ClassBAdapter(IA):
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        """calls the class b method_b instead"""
        self.class_b.method_b()

```
[Screenshot](adapter.png)

#### Decorator
The decorator pattern is a structural pattern, that allows you to attach additional responsibilities to an object at run time.
The decorator pattern is used in both the Object Oriented and Functional paradigms.
The decorator pattern is different than the Python language feature of Python Decorators in it’s syntax, but the application of it is the same, in the way that it is essentially a wrapper.
The Decorator pattern adds extensibility, without modifying the original function.
[Screenshot](decorator.png)

#### Flyweight
[Screenshot](flyweight.png)
