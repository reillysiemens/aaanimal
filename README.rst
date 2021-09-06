Aaanimal
========

.. image:: https://img.shields.io/github/workflow/status/reillysiemens/aaanimal/Test/main.svg?style=flat-square&label=tests
    :target: https://github.com/reillysiemens/aaanimal/actions?query=workflow%3ATest
    :alt: GitHub Actions test status

.. image:: https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10-blue?style=flat-square
   :target: https://www.python.org/downloads/
   :alt: Python versions

.. image:: https://img.shields.io/badge/license-ISC-purple?style=flat-square
    :target: https://github.com/reillysiemens/aaanimal/blob/main/LICENSE
    :alt: License

.. image:: https://img.shields.io/badge/code%20style-black-black?style=flat-square
    :target: https://github.com/psf/black
    :alt: Any color you like

Aaanimal is a Python extension module for generating friendly, mostly unique
names. The name is a play on GfyCat's `AdjectiveAdjectiveAnimal URLs`_. It is
written in `Rust`_ using `PyO3`_.

Usage
------

Aaanimal only has one function. Use it wisely.

.. code-block:: python

   import aaanimal
   aaanimal.generate()  # 'crushable-badtempered-raptors'
   aaanimal.generate(adjectives=1, animals=1, separator=" ✨ ")  # 'nautical ✨ aphid'

Installation
------------

The module is distributed to `PyPI`_.

.. code-block:: sh

   pip install aaanimal

You shouldn't need a Rust compiler unless you want to build from source.

Platform Support
++++++++++++++++

There is currently only support for Linux, but the plan is to support Windows
(and possibly FreeBSD) as well. If you'd like to help make either a reality,
please consider contributing.

.. _AdjectiveAdjectiveAnimal URLs: https://gfycat.com/about
.. _Rust: https://www.rust-lang.org/
.. _PyO3: https://pyo3.rs/
.. _PyPI: https://pypi.org/
