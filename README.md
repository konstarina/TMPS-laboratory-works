# ***TMPS Labaratory Work #1***

### Author: Constantinova Carina
----

## Objectives:

* Get familiar with the Creational Design Patterns;
* Choose a sppecific domain;
* Implement at least 3 CDPs for the specific domain;

## Creational Design Pattern:
 - [ ] Singleton
 - [x] Prototype
 - [x] Builder
 - [ ] Object Pooling
 - [x] Factory Method
 - [x] Abstract Factory

## Implementation:
#### Prototype
Prototype Design Pattern is good when creation of new objects may require more resources than there are available or you want to use. We can use deep copy (copies and creates new references for all levels) or shallow (creates the copies with new references in memory, but the underlying data will point to the same location of the original copy ) depending on our needs.

```python 
class IProtoType(metaclass=ABCMeta):
  
    """interface with clone method"""
    @abstractstaticmethod
    def clone():

        """The clone, deep or shallow, is up to how you 
        want implement the details in your concrete class?"""```
       
