from collections import Callable


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
