import uuid
from collections import Callable

from django.db import models


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


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class KeyModel(TimestampedModel):
    key = models.CharField(
        max_length=255, unique=True, db_index=True, null=False, blank=True)

    class Meta:
        abstract = True

    @property
    def short_key(self):
        return self.key[:8]

    def save(self, *args, **kwargs):
        if not self.key:
            while True:
                new_key = str(uuid.uuid4())
                try:
                    self.__class__.objects.get(key=new_key)
                    continue
                except self.__class__.DoesNotExist:
                    self.key = new_key
                    break
        super().save(*args, **kwargs)
