try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = __import__('assist').__version__

setup(
    name="django-assist",
    packages=['assist'],
    version=version,
    author="Baye Wayly",
    author_email="havelove@gmail.com",
    url="https://github.com/waylybaye/django-assist",
)
