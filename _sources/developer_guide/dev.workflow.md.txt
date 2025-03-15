# Staging and Release Workflow with CircleCI

This document describes how to manage the staging and release workflow for an open-source Python project published on PyPI using **CircleCI**.

---

## Branching Strategy

### Main Branches

1. **`main`**:

   - Contains stable releases published to **PyPI**.
   - Only updated when a stable release is ready.

2. **`dev`**:
   - Used for active development and integration.
   - Pre-releases to **TestPyPI** are tagged and published from here.

### Supporting Branches

- **Feature Branches (`feature/*`)**:
  - For developing new features or changes.
  - Merged into `dev` when complete.

---

## Versioning

Use **Semantic Versioning (SemVer)**:  
`MAJOR.MINOR.PATCH`

- **Pre-Releases**: Add alpha, beta, or release candidate tags:
  - `1.2.0-alpha1`
  - `1.2.0-beta1`
  - `1.2.0-rc1`
- **Stable Releases**: Use plain version numbers:
  - `1.2.0`

---

## Workflow Steps

### 1. Development Phase

- Work on new features in `feature/*` branches.
- Merge features into the `dev` branch.
- Run tests and validations in CI/CD pipelines.

### 2. Pre-Release to TestPyPI

- When ready for testing, tag a pre-release version (e.g., `v1.2.0-beta1`) on the `develop` branch.
- CircleCI automatically publishes the package to **TestPyPI** for validation.

### 3. Final Release to PyPI

- When the release is stable:
  1. Merge `dev` into `main`.
  2. Tag the release with a stable version (e.g., `v1.2.0`).
  3. CircleCI automatically publishes the package to **PyPI**.

---

## Tag-Driven Release Workflow

### Tag Naming

- **Pre-Releases**: Use tags like `v1.2.0-alpha1`, `v1.2.0-beta1`, `v1.2.0-rc1`.
- **Stable Releases**: Use tags like `v1.2.0`.

### CI/CD Behavior

1. **Pre-Release Tags** (`-alpha`, `-beta`, `-rc`):
   - Trigger publishing to **TestPyPI**.
2. **Stable Tags** (e.g., `v1.2.0`):
   - Trigger publishing to **PyPI**.

---

## Example CircleCI Config

Below is an example CircleCI configuration (`.circleci/config.yml`) for handling both **TestPyPI** and **PyPI** publishing:

```yaml
version: 2.1

executors:
  python-executor:
    docker:
      - image: circleci/python:3.9

jobs:
  test:
    executor: python-executor
    steps:
      - checkout
      - run:
          name: Install dependencies
          command: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
      - run:
          name: Run tests
          command: pytest --cov=.

  publish-testpypi:
    executor: python-executor
    steps:
      - checkout
      - run:
          name: Install dependencies
          command: |
            python -m pip install --upgrade pip
            pip install build twine
      - run:
          name: Build package
          command: python -m build
      - run:
          name: Publish to TestPyPI
          command: |
            python -m twine upload --repository testpypi dist/*
          environment:
            TWINE_USERNAME: << pipeline.parameters.testpypi_username >>
            TWINE_PASSWORD: << pipeline.parameters.testpypi_password >>

  publish-pypi:
    executor: python-executor
    steps:
      - checkout
      - run:
          name: Install dependencies
          command: |
            python -m pip install --upgrade pip
            pip install build twine
      - run:
          name: Build package
          command: python -m build
      - run:
          name: Publish to PyPI
          command: |
            python -m twine upload dist/*
          environment:
            TWINE_USERNAME: << pipeline.parameters.pypi_username >>
            TWINE_PASSWORD: << pipeline.parameters.pypi_password >>

workflows:
  version: 2
  test-and-deploy:
    jobs:
      - test
      - publish-testpypi:
          requires:
            - test
          filters:
            tags:
              only: /^v.*-(alpha|beta|rc)[0-9]*$/
      - publish-pypi:
          requires:
            - test
          filters:
            tags:
              only: /^v[0-9]+\.[0-9]+\.[0-9]+$/
```
