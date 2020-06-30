import setuptools

setuptools.setup(
    name='pypi-slug',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
