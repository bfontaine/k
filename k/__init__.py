# -*- coding: UTF-8 -*-

__version__ = '0.0.1'

class KEnum(int):
    pass

def make(name, names, start=0):
    """
    Create an enum names ``name``, with a given list of names for each member,
    e.g.: ::

        Foo = k.make("Foo", ["A", "B", "C"])

    Note that this can be reduced as ``Foo = k.make("Foo", "ABC")``.

    You can then use each value:

        >>> Foo.A
        0
        >>> Foo.B
        1
        >>> Foo.C
        2

    Types are matched, too. An enum member is of its enum type:

        >>> isinstance(Foo.A, Foo)
        True
        >>> A1 = k.make("A1", "X")
        >>> A2 = k.make("A2", "X")
        >>> A1.X
        0
        >>> A2.X
        0
        >>> A1.X == A2.X
        True
        >>> isinstance(A1.X, A2)
        False
        >>> isinstance(A2.X, A1)
        False

    An enum name is useful for debugging purposes, but you can use the same
    name for different enums if you like:

        >>> A = k.make("A", "X")
        >>> B = k.make("A", "X")
        >>> A == B
        False
        >>> isinstance(A.X, B)
        False
        >>> type(A.X)
        <class 'k.aA'>
        >>> type(B.X)
        <class 'k.aA'>
        >>> type(A.X) == type(B.X)
        False

    But enum members are ``int``s too:

        >>> A = k.make("A", "abcd")
        >>> isinstance(A.a, int)
        >>> A.b + 41
        42
    """
    klass = type(name, (KEnum,), {})

    for k, v in zip(names, range(start, len(names) + start)):
        setattr(klass, k, klass(v))

    return klass
