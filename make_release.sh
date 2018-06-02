#!/bin/sh
# make package
python3 setup.py sdist bdist_wheel

# upload to pypi testing
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
#twine upload --repository testpypi dist/*


# upload to pypi
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
#twine upload --repository pypi dist/*
