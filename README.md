# sphinx action example

This is a barebones python package for learning how to how to automatically publish sphinx docs using github actions

## summary

* built a basic python package with a couple of documented methods, and tests
* on push the github action "python-package" runs the package tests
* added [sphinx docs](./docs)
* added and modifed the github static [html publish action](./.github/workflows/build_and_upload_sphinx.yml) to also run sphinx-build

The sphinx [doc page](https://smorken.github.io/sphinx_action_example/) is now updated on each push to the main branch