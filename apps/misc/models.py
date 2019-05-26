import uuid
from collections import Callable

from django.db import models


class Choices:
    @classmethod
    def choices(cls):
        for attr_name in dir(cls):
            if all([
                attr_name,
                not attr_name.startswith('_'),
                not isinstance(getattr(cls, attr_name), Callable)
            ]):
                if isinstance(getattr(cls, attr_name), tuple):
                    yield (getattr(cls, attr_name)[1],
                           getattr(cls, attr_name)[0])
                else:
                    yield getattr(cls, attr_name), attr_name

    @classmethod
    def name(cls, target_val):
        for attr in dir(cls):
            if attr and not attr.startswith('_') \
                    and not isinstance(getattr(cls, attr), Callable):
                val = getattr(cls, attr)
                if isinstance(val, tuple):
                    if val[1] == target_val:
                        return val[0]
                if val == target_val:
                    return attr
        return ''

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
