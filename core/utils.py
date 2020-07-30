def image_parse(match, model):
    try:
        image = model.image_set.get(shortuuid=match.group('shortuuid'))
    except model.image_set.model.DoesNotExist:
        image = None

    return image


def image_sub(content, repl):
    import re

    IMAGE_RE = r'\[image (?P<shortuuid>[a-z\d]+)\]'

    return re.sub(IMAGE_RE, repl, content)


def unique_boolean(field, subset=[]):
    """
    Allows to specify a unique boolean for a model.
    """

    from functools import wraps

    def cls_factory(cls):
        def factory(func):
            @wraps(func)
            def decorator(self):
                kwargs = {field: True}
                for arg in subset:
                    if getattr(self, arg):
                        kwargs[arg] = getattr(self, arg)
                if getattr(self, field):
                    try:
                        tmp = self.__class__.objects.get(**kwargs)
                        if self != tmp:
                            setattr(tmp, field, False)
                            tmp.save()
                    except self.__class__.DoesNotExist:
                        if getattr(self, field) is not True:
                            setattr(self, field, True)
                else:
                    if self.__class__.objects.filter(**kwargs).count() == 0:
                        setattr(self, field, True)
                return func(self)
            return decorator
        if hasattr(cls, 'save'):
            cls.save = factory(cls.save)
        return cls

    return cls_factory
