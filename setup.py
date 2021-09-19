import setuptools
from prioritize.version import __version__

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='prioritize',
    version=__version__,
    author='Tim Pogue',
    description='A package to help organize tasks based on priorities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Accoustium/prioritize',
    project_urls={
        'Bug Tracker': 'https://github.com/Accoustium/prioritize/issues',
    },
    package_dir={'': 'prioritize'},
    packages=setuptools.find_packages(where='prioritize'),
    python_requires='>=3.6',
)
