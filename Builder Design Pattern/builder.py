from abc import ABCMeta


class IFactoryBuilder(metaclass=ABCMeta):
    """The Builder Interface"""

    @staticmethod
    def set_wall_material(value):
        """Set the wall_material"""

    @staticmethod
    def set_building_type(value):
        """Set the building_type"""

    @staticmethod
    def set_number_employees(value):
        """Set the number of employees"""

    @staticmethod
    def set_number_departments(value):
        """Set the number of departments"""

    @staticmethod
    def get_result():
        """Return the factory"""


class FactoryBuilder(IFactoryBuilder):
    """The Concrete Builder."""

    def __init__(self):
        self.factory = Factory()

    def set_wall_material(self, value):
        self.factory.wall_material = value
        return self

    def set_building_type(self, value):
        self.factory.building_type = value
        return self

    def set_number_employees(self, value):
        self.factory.employees = value
        return self

    def set_number_departments(self, value):
        self.factory.departments = value
        return self

    def get_result(self):
        return self.factory


class Factory:
    """The Product"""

    def __init__(self, building_type="Factory", employees=100, departments=50, wall_material="Brick"):
        self.wall_material = wall_material
        self.building_type = building_type
        self.employees = employees
        self.departments = departments

    def __str__(self):
        return "This is the {0} {1} with {2} employees(s) and {3} departments(s).".format(
            self.wall_material, self.building_type, self.employees, self.departments
        )


class FactoryDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return FactoryBuilder()\
            .set_building_type("Wonka Factory")\
            .set_wall_material("Chocolate")\
            .set_number_employees("99999 Oompa Loompas")\
            .set_number_departments(99)\
            .get_result()


class AmazonDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return FactoryBuilder()\
            .set_building_type("Empire Amazon")\
            .set_wall_material("Online marketplace")\
            .set_number_employees(1000000)\
            .set_number_departments(200).get_result()


if __name__ == "__main__":
    FACTORY = FactoryDirector.construct()
    EMPIRE = AmazonDirector.construct()
    print(FACTORY)
    print(EMPIRE)
