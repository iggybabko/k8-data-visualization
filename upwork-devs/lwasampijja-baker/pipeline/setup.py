from setuptools import setup, find_packages


setup(
    name='codes',
    version='1.0.0',
    install_requires=['attrs',
                        'bokeh',
                        'certifi',
                        'chardet',
                        'cycler',
                        'decorator',
                        'idna',
                        'importlib-metadata',
                        'iniconfig',
                        'Jinja2',
                        'kiwisolver',
                        'MarkupSafe',
                        'matplotlib',
                        'mock',
                        'more-itertools',
                        'networkx',
                        'nose',
                        'numpy',
                        'packaging',
                        'pandas',
                        'Pillow',
                        'pluggy',
                        'py',
                        'pyparsing',
                        'pytest',
                        'pytest-mpl',
                        'python-dateutil',
                        'pytz',
                        'PyYAML',
                        'requests',
                        'scipy',
                        'seaborn',
                        'six',
                        'toml',
                        'tornado',
                        'typing-extensions',
                        'urllib3',
                        'zipp',
                      ],
    packages=find_packages()
)