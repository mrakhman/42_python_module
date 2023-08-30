# Package for 42 school project
Learn how to create python packages

How to create a package, files to include:
https://packaging.python.org/en/latest/tutorials/packaging-projects/

Commands:

## Create dist folder with .whl and .gz
`python -m build`

## Create account and create API key
https://test.pypi.org/account/register/

## Load package to PyPI
`python -m twine upload --repository testpypi dist/*`

## Install package
`pip install ./dist/ft_package_mrakhman-0.0.1.tar.gz`
`pip install ./dist/ft_package_mrakhman-0.0.1-py3-none-any.whl`

## Check 
`pip list`
`pip show -v ft_package_mrakhman`
