from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
#from setuptools import setup, find_packages

from codecs import open


package_path = path.abspath(path.dirname(__file__))

with open(path.join(package_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(package_path, 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name='probadata',

    version=version,

    description='Probabilistic data structures (HyperLogLog, Bloom Filter, Count-Min Sketch, etc ...)',
    long_description=long_description,
    url='https://github.com/ampaho/probadata.git',
    author='Olalekan H. ABOU BAKAR',
    author_email='houdan@jolome.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
		'Topic :: Database :: Database Engines/Servers',
		'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='Probabilistic data structures hyperloglog bloom filter',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],
    
    #install_requires=['bitarray', 'mmh3'],
    
    install_requires=['bitarray>=0.3.4'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    
    packages=['probadata']

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #   'console_scripts': [
    #        'src=src:main',
    #    ],
    #},
)
