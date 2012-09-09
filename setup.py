from setuptools import setup


__name__ = 'projectutils'
__version__ = '0.1'
__author__ = 'Jesse Panganiban'


def install_requires():
    with open('requirements') as f:
        install_requires = f.readlines()
    return install_requires

console_scripts = [
    'bootstrap.project = projectutils.core.main:main'
]
entry_points = {
    'console_scripts': console_scripts
}

setup(name=__name__,
      version=__version__,
      author=__author__,
      install_requires=install_requires(),
      entry_points=entry_points)
