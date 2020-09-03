import setuptools

setuptools.setup(
    name='pypi-slug',
    version='0.1.0',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
