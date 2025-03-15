# Documenting

Proper documentation is essential for maintaining and scaling any software project. This guide provides instructions on how to document your code effectively using Sphinx, a powerful documentation generator. By following these steps, you can ensure that your project's documentation is clear, comprehensive, and easy to navigate.

## Codumenting Code

We use NumPy style docstrings to annotate classes. Click [here](https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html) to read more about this.

## Sphinx

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

### Installation

To install Sphinx, you can use pip:

```shell
pip install sphinx
```

### Quick Start

To quickly set up Sphinx for your project, you can use the `sphinx-quickstart` command:

```shell
sphinx-quickstart
```

This command will guide you through creating the basic configuration for your documentation.

### Building Documentation

Once you have your documentation source files ready, you can build the HTML version of your documentation by running:

```shell
cd docs
poetry run make html
```

To generate a PDF version of your documentation, you can use:

```shell
poetry run make latexpdf
```

By following these steps, you can create and maintain high-quality documentation for your project.
