__all__ = ['getslug']

import re


def getslug(name):
    slug = re.sub(r'[^a-z0-9]', "-", name.lower())
    slug = re.sub(r'^-|-$', '', slug)
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug
