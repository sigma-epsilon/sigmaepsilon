# Package Management with Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

## Installation

To install Poetry, you can use the following command:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

## Creating a New Project

To create a new project, use the `new` command:

```sh
poetry new my-project
```

## Adding Dependencies

To add a dependency to your project, use the `add` command:

```sh
poetry add requests
```

## Installing Dependencies

To install all the dependencies for your project, use the `install` command:

```sh
poetry install
```

## Updating Dependencies

To update the dependencies to their latest versions, use the `update` command:

```sh
poetry update
```

## Publishing a Package

To publish your package to PyPI, use the `publish` command:

```sh
poetry publish --build
```

## Conclusion

Poetry simplifies the process of managing dependencies and packaging in Python projects, making it easier to maintain and distribute your code.
