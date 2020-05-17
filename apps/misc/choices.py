class ChoicesMeta(type):
    def __getattribute__(cls, name):
        if name and not name.startswith("_"):
            try:
                value = cls.__dict__[name]
                if not callable(value):
                    if isinstance(value, tuple):
                        return value[0]
                    else:
                        return value
            except KeyError:
                pass
        return super().__getattribute__(name)


class Choices(metaclass=ChoicesMeta):
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


    convertibles = Car.objects.filter(type=CarType.CONVERTIBLE)
    """

    @classmethod
    def choices(cls):
        for attr_name in dir(cls):
            if attr_name.startswith("_"):
                continue
            if attr_name in ["keys", "choices"]:
                continue
            value = cls.__dict__[attr_name]
            if not callable(value):
                if isinstance(value, tuple):
                    yield value
                else:
                    yield value, attr_name

    @classmethod
    def keys(cls):
        return [choice[0] for choice in cls.choices()]
