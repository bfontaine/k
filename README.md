# k

[![Pypi package](https://img.shields.io/pypi/v/k.png)](https://pypi.python.org/pypi/k)
[![downloads count](https://img.shields.io/pypi/dm/k.png)](https://pypi.python.org/pypi/k)

``k`` is an enum-like for Python.

## Install

    [sudo] pip install k

The library works with both Python 2.x and 3.x.

## Usage

Create an enum named ``name``, with a given list of names for each member, e.g.:

```python
import k

Foo = k.make("Foo", ["A", "B", "C"])
```

You can then use each value:

```pycon
>>> Foo.A
0
>>> Foo.B
1
>>> Foo.C
2
```

Types are matched, too. An enum member is of its enum type:

```pycon
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
```

An enum name is useful for debugging purposes, but you can use the same name for different enums if you like:

```pycon
>>> A = k.make("A", "X")
>>> B = k.make("A", "X")
>>> A == B
False
>>> isinstance(A.X, B)
False
>>> type(A.X)
<class 'k.A'>
>>> type(B.X)
<class 'k.A'>
>>> type(A.X) == type(B.X)
False
```

But enum members are ``int``s too:

```pycon
>>> A = k.make("A", "abcd")
>>> isinstance(A.a, int)
>>> A.b + 41
42
```