from setuptools import setup

VERSION = '0.2'


setup(
    name='jinja2_standalone_compiler',
    packages=['jinja2_standalone_compiler', ],
    version=VERSION,
    author='Filipe Waitman',
    author_email='filwaitman@gmail.com',
    install_requires=[x.strip() for x in open('requirements.txt').readlines()],
    url='https://github.com/filwaitman/jinja2-standalone-compiler',
    download_url='https://github.com/filwaitman/jinja2-standalone-compiler/tarball/{}'.format(VERSION),
    keywords=['cache', 'caching', 'memcached', 'redis'],
    test_suite='tests',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    entry_points="""\
    [console_scripts]
    jinja2_standalone_compiler = jinja2_standalone_compiler:main_command
    """,
)
