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
        want implement the details in your concrete class?"" 
 ``` 
       
#### Builder
The Builder Pattern is a creational pattern whose intent is to separate the construction of a complex object from its representation so that you can use the same construction process to create different representations.
The Builder Pattern tries to solve,
* How can a class create different representations of a complex object?
* How can a class that includes creating a complex object be simplified?
Here I have a director returning different types oof factories :

```python class FactoryDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return FactoryBuilder()\
            .set_building_type("Wonka Factory")\
            .set_wall_material("Chocolate")\
            .set_number_employees("99999 Oompa Loompas")\
            .set_number_departments(99)\
            .get_result()
 ```
 
#### Factory Method
The Factory Pattern is a creational pattern that defines an Interface for creating an object and defers instantiation until runtime. The chocolate_factory.py python file, will call the ChocolateFactory method get_chocolate(chocolate), and the ChocolateFactory will return it an object of which ever type of chocolate was requested. The client application can then use the new chocolate object how ever it desires and it’s interface allows.

```python
    CHOCO = ChocolateFactory.get_chocolate("DarkChocolate")
    print("Dark Chocolate contains", CHOCO.get_information())
    CHOCO = ChocolateFactory.get_chocolate("MilkChocolate")
    print("Milk Chocolate contains", CHOCO.get_information())
    CHOCO = ChocolateFactory.get_chocolate("WhiteChocolate")
    print("White Chocolate contains", CHOCO.get_information())
```

#### Abstract Factory
