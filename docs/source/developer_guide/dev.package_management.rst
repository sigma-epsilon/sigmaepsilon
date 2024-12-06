==================
Package Management
==================

.. include:: ../global_refs.rst

Package management with Poetry
===============================

We use Poetry_ to manage the project and its dependencies because it offers superior 
dependency management compared to pip. Poetry gradually resolves conflicts between dependencies, 
ensuring that the correct package versions are installed and helping you avoid the dreaded 
dependency hell (ask me how I know). The key difference is that pip attempts to 
resolve all conflicts at once, which can take hours and still fail. In contrast, Poetry 
resolves conflicts incrementally when adding new dependencies, making it both faster and more 
reliable. Dependency management is not the only feature that Poetry offers, but this was the
decisive factor for us.

We won't cover all the features of Poetry here, but we will provide a brief
overview about the most frequently used commands. For a more detailed guide, please
refer to their documentation.

Installing Poetry
-----------------

First make sure that Poetry is installed on your system. If not, you can install it
using the following command:

.. code-block:: bash

    $ pip install poetry

Don't worry. This will be the only package that you have to install into your global Python 
enviroment, as Poetry handles all the rest and isolates your packages.

Setting up the `pyproject.toml` file
------------------------------------

Setting up a project with Poetry basically means creating a `pyproject.toml` file in the root
of your project. This file contains all the information about your project, such as the name,
version, dependencies, and so on. Look at other projects in the SigmaEpsilon ecosystem to see
how this file is structured and take inspiration from them.

Adding a dependency
-------------------

To add the project `pymeshfix` as a new dependency to the project, use the following 
command:

.. code-block:: bash

    $ poetry add pymeshfix --group test

This will add the package `pymeshfix` to the project and install it in the virtual environment.

Adding an experimental dependency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are only experimenting, use Pip to install the package. Let say you want to experiment 
with the `pymeshfix` library. Before adding it to the list of dependencies, you should simply 
install it using Pip. When you do that, be sure that you are in the virtual enviroment created 
by Poetry.

.. code-block:: bash

    $ poetry run pip install pymeshfix

Adding a dependency in development mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes -usually when working with other pacakges from the `sigmaepsilon` ecosystem, you would want 
to install them in editable mode, so that your modifications doesn't get lost. The proper way 
to do this is by using the following command inside a Poetry shell session:

.. code-block:: bash

    $ poetry run pip install "-e ..\sigmaepsilon.math [test,dev]"

This assumes that `sigmaepsilon.math` is in the same folder as `sigmaepsilon.mesh`.

The command would install `sigmaepsilon.math` in editable mode with optional dependencies for 
testing and development. Usually this is more than what you need (you just want your occasional 
changes to *sigmaepsilon.math* to not get lost) and you are good with

.. code-block:: bash

    $ poetry run pip install -e ..\sigmaepsilon.math

Installing the package for development
--------------------------------------

Navigate to the root of the project in a terminal and use the following command:

.. code-block:: bash

    $ poetry install --with dev,test,docs

This will create a virtual environment and install all the dependencies needed for
development, testing, and documentation. If you only want to install the dependencies
for the production environment, you can use the following command:

.. code-block:: bash

    $ poetry install

Compliance with third-party licenses
====================================

When you add a new dependency, you should also update the license file for third-party libraries using

.. code-block:: bash

    $ poetry run pip-licenses --format=plain --output-file=THIRD-PARTY-LICENSES --order=license

This command creates the file `THIRD-PARTY-LICENSES`, where the libraries are ordered according 
to the type of license they are distributed under. Note that `pip-licenses` goes through all 
the currently installed packages in the enviroment and therefore it is crucial that the package 
should be installed without optional dependencies. For this, you might need to delete the virtual 
enviroment and reinstall the package.

.. code-block:: bash

    $ poetry env remove <the-name-of-the-enviroment>
    $ poetry install

If you don't know what is the name of your enviroment, you can use

.. code-block:: bash

    $ poetry env list

and it will list your enviroments, with the active one being highlighted.

After you updated the license file of third-party libraries, you should check if the project complies with 
the licenses of direct and indirect dependencies.

Tracing back dependencies
=========================

If you wonder how a specific library ended up in the license file, you can use `pipdeptree`.

.. code-block:: bash

    $ poetry run pip install pipdeptree

Then to figure out how for instance the `triangle` library ended up in the licenses file, 
use this command:

.. code-block:: bash

    $ poetry run pipdeptree --reverse --packages triangle

and your output would include something like this:

.. code-block:: bash

    triangle==20230923
    └── sectionproperties==3.2.0 [requires: triangle>=20230923,<20230924]
        └── sigmaepsilon.mesh==2.3.3 [requires: sectionproperties>2.1.3]

It shows, that triangle is a direct dependency of `sectionproperties`, which is a direct 
dependency of `sigmaepsilon.mesh`.