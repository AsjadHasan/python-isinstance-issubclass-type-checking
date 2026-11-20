
"""
Type Checking with isinstance() and issubclass().

Demonstrates inheritance-aware type checking in Python.
"""


class Animal:
    """Parent class representing an animal."""

    pass


class Dog(Animal):
    """Child class inheriting from Animal."""

    pass


def main():
    """Check object instances and class inheritance."""

    # Create an object of Dog
    d = Dog()

    # Check object instances
    print(f"Is d an instance of Dog? {isinstance(d, Dog)}")
    print(f"Is d an instance of Animal? {isinstance(d, Animal)}")

    # Check class inheritance
    print(f"Is Dog a subclass of Animal? {issubclass(Dog, Animal)}")
    print(f"Is Animal a subclass of Dog? {issubclass(Animal, Dog)}")


if __name__ == "__main__":
    main()