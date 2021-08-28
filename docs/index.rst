Aaanimal
========

Aaanimal is a Python extension module for generating mostly unique, friendly
names. The name is a play on GfyCat's `AdjectiveAdjectiveAnimal URL
nomenclature <GfyCat>`_. It is written in `Rust`_ using `PyO3`_.

Usage
------

Aaanimal only has one function. Use it wisely.

.. code-block:: python

   import aaanimal
   aaanimal.generate()  # 'crushable-badtempered-raptors'
   aaanimal.generate(adjectives=1, animals=1, separator="•")  # 'nautical•aphid'

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
please consider :ref:`contributing <contributing>`.

.. toctree::
   :hidden:
   :maxdepth: 1

   api
   changelog
   Code of Conduct <code-of-conduct>
   contributing

.. _GfyCat: https://gfycat.com/about
.. _Rust: https://www.rust-lang.org/
.. _PyO3: https://pyo3.rs/
.. _PyPI: https://pypi.org/
