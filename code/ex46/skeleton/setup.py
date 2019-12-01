try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'projectname'
    'packages': ['NAME'],
    'version': '0.1',
    'description': 'My Project',
    'author': 'My Name',
    'author_email': 'My email.',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'install_requires': ['pytest'],
    'scripts': [],
}

setup(**config)
