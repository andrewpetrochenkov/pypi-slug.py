import setuptools

setuptools.setup(
    name='pypi-slug',
    version='2020.11.8',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
