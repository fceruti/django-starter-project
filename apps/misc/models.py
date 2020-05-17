import uuid

from django.db import models


class TimestampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class KeyModel(TimestampedModel):
    key = models.CharField(
        max_length=255, unique=True, db_index=True, null=False, blank=True
    )

    class Meta:
        abstract = True

    @property
    def short_key(self):
        return self.key[:8]

    def save(self, **kwargs):
        if not self.key:
            while True:
                new_key = str(uuid.uuid4())
                try:
                    self.__class__.objects.get(key=new_key)
                    continue
                except self.__class__.DoesNotExist:
                    self.key = new_key
                    break
        super().save(**kwargs)
