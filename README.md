<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/pypi-slug.svg?maxAge=3600)](https://pypi.org/project/pypi-slug/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/pypi-slug.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/pypi-slug.py/actions)

### Installation
```bash
$ [sudo] pip install pypi-slug
```

#### Examples
```python
>>> import pypi_slug
>>> pypi_slug.getslug('0-._.-._.-._.-._.-._.-._.-0')
'0-0'
>>> pypi_slug.getslug('00print_lol')
'00print-lol'
>>> pypi_slug.getslug('00SMALINUX')
'00smalinux'
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>