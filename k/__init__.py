# -*- coding: UTF-8 -*-

__version__ = '0.0.1'


class KEnum(int):
    pass


def make(name, names, start=0):
    """
    Create an enum named ``name``, with a given list of names for each member.
    """
    klass = type(name, (KEnum,), {})

    for k, v in zip(names, range(start, len(names) + start)):
        setattr(klass, k, klass(v))

    return klass
