__all__ = ['getslug']

import re

def getslug(name):
    slug = re.sub(r'[^a-z0-9]', "-", name.lower())
    while '--' in slug:
        slug = slug.replace('--','-')
    return slug
