""" Setup of fast-aoc package
"""
import io
import os
from setuptools import setup, find_packages


def parse_requirements(file):
    """ Parses any file with package requirements
    """
    required_packages = []
    with open(os.path.join(os.path.dirname(__file__), file)) as req_file:
        for line in req_file:
            if '/' not in line:
                required_packages.append(line.strip())
    return required_packages


def get_package_props():
    """ Collects package properties from the code
    """
    prop_names = ['version', 'author', 'email']
    props_dict = {}

    with open(os.path.join(os.path.dirname(__file__), 'fast_aoc', '__init__.py')) as props_file:
        for line in props_file:
            for prop_name in prop_names:
                if '__{}__'.format(prop_name) in line:
                    props_dict[prop_name] = line.split("=")[1].strip(' \n"\'')
                    break

    return tuple(props_dict[prop_name] for prop_name in prop_names)


def get_long_description():
    """ Collects description from README.md
    """
    return io.open('README.md', encoding="utf-8").read()


version, author, email = get_package_props()

setup(
    name='fast-aoc',
    python_requires='>=3.6',
    version=version,
    description='An interface for fast and efficient solving of Advent of Code problems',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords='fast_aoc, aoc, advent of code',
    url='https://github.com/AleksMat/fast-aoc',
    author=author,
    author_email=email,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'DEV': parse_requirements('requirements-dev.txt')
    },
    test_suite='tests',
    tests_require=parse_requirements('requirements-dev.txt'),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'aoc=fast_aoc.cli:aoc',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
