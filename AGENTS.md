# Instructions for Coding Agents

This is the master folder for all projects in the sigmaepsilon namespace.

The namespace is organized as a collection of namespace Python packages, each with it's own repository.

## Critical Rules

Never read the .env file in the repository.

The commit messages shouldn't include any details on ownership at all.

Never add "Co-Authored-By: Claude..." or similar AI contributor lines to commit messages. Commit messages are not the place to make ownership statements — ownership of code is governed by company policies and agreements between employer and employee, or by the individual repository owner if no organization is involved.

## References and Attribution

Code built on published work (papers, books, theses, preprints, other open-source code) must credit its source, in the same change:

1. Add the source to `docs/source/references.bib` of the repository that holds the implementation, not the one that only uses it. Create the file if it doesn't exist (the docs use `sphinxcontrib-bibtex`). Only include details that you verified, such as a DOI.
2. Link the code to the source: cite it in the `References` section of the docstring of the class or function that implements it, and in the docs page that describes it.
3. Benchmarks and reference values used in tests are sources too: cite them in the docstring of the test module.

Never present an adapted method or algorithm without naming where it came from.
