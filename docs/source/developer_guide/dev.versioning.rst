==========
Versioning
==========

Projects in the SigmaEpsilon ecosystem follow the principles of `Semantic Versioning`_ (SemVer) to 
ensure clear and predictable versioning for developers and users.

Semantic Versioning
-------------------

Semantic Versioning is a widely adopted versioning scheme designed to convey meaning about the underlying changes with each release. A version number consists of three parts:

``MAJOR.MINOR.PATCH``

- **MAJOR**: Incremented when making incompatible changes to the API.
- **MINOR**: Incremented when adding functionality in a backwards-compatible manner.
- **PATCH**: Incremented for backwards-compatible bug fixes.

For example:
- ``1.0.0``: The first stable release.
- ``1.1.0``: A new feature is added in a backwards-compatible way.
- ``1.1.1``: A bug is fixed without affecting the existing functionality.

Rules and Guarantees
--------------------

1. **MAJOR Version**: Changes that break backwards compatibility will result in a MAJOR version bump. Examples include:
   - Removing public APIs.
   - Modifying existing APIs in ways that are not backwards-compatible.

2. **MINOR Version**: New features that are fully backwards-compatible will result in a MINOR version bump. Examples include:
   - Adding new functions or methods.
   - Introducing new classes or modules without altering existing functionality.

3. **PATCH Version**: Bug fixes or improvements that do not affect the public API will result in a PATCH version bump. Examples include:
   - Fixing incorrect behavior or errors.
   - Optimizing performance without changing functionality.

Examples of Versioning
-----------------------

- If a new feature is added to the library that does not break existing functionality, the version will change from ``1.2.3`` to ``1.3.0``.
- If a critical bug is fixed, the version will change from ``1.2.3`` to ``1.2.4``.
- If a breaking change is introduced, the version will change from ``1.2.3`` to ``2.0.0``.

Stability
---------

We aim to provide a stable and reliable library. Major version releases (e.g., ``1.0.0``, ``2.0.0``) will signify a commitment to a stable API, ensuring minimal breaking changes between updates.

References
----------

For more details on Semantic Versioning, visit the official `Semantic Versioning`_ website.

.. _Semantic Versioning: https://semver.org/
