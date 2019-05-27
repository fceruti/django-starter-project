from collections import Callable


class Choices:
    """
    Helper class to create choices from django models. Every property you
    add is a choice. If you define as value a string, then the value is
    the database entry, while the property name is the display name. If
    you pass a tuple, the first element is the database entry, and the
    second the display name.

    Usage:

    class CarType(Choices):
        SUV = 'SUV',
        SEDAN = ('SD', 'Sedan')
        HATCHBACK = ('HB', 'Hatchback')
        CONVERTIBLE = ('CV', 'Convertible')
        COUPE = ('CP', 'Coupe')

    class Car(models.Model):
        type = models.CharField(max_length=10, choices=CarType.choices())
    """

    @classmethod
    def choices(cls):
        for attr_name in dir(cls):
            value = getattr(cls, attr_name)
            if all([
                attr_name,
                not attr_name.startswith('_'),
                not isinstance(value, Callable)
            ]):
                if isinstance(value, tuple):
                    yield value
                else:
                    yield value, attr_name

    @classmethod
    def keys(cls):
        return [choice[0] for choice in cls.choices()]
