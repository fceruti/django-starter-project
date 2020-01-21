from apps.misc.choices import Choices


def test_choices():
    class CarType(Choices):
        SUV = "SUV"
        SEDAN = ("SD", "Sedan")
        HATCHBACK = ("HB", "Hatchback")
        CONVERTIBLE = ("CV", "Convertible")
        COUPE = ("CP", "Coupe")

    assert set(CarType.keys()) == set(["SUV", "SD", "HB", "CV", "CP"])

    assert set(CarType.choices()) == set(
        [
            ("SUV", "SUV"),
            ("SD", "Sedan"),
            ("HB", "Hatchback"),
            ("CV", "Convertible"),
            ("CP", "Coupe"),
        ]
    )


def test_choices_accessor():
    class CarType(Choices):
        SUV = "SUV"
        SEDAN = ("SD", "Sedan")
        HATCHBACK = ("HB", "Hatchback")
        CONVERTIBLE = ("CV", "Convertible")
        COUPE = ("CP", "Coupe")

    assert CarType.SUV == "SUV"
    assert CarType.SEDAN == "SD"
