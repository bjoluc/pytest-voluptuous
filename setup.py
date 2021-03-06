from setuptools import setup, find_packages


setup(
    name='pytest-voluptuous',
    use_scm_version=True,
    description='Pytest plugin for asserting data against voluptuous schema.',
    long_description=open('README.rst').read() + '\n' + open('CHANGELOG.rst').read(),
    long_description_content_type='text/x-rst',
    license='ASL 2.0',
    author='F-Secure Corporation',
    author_email='opensource@f-secure.com',
    url='https://github.com/f-secure/pytest-voluptuous',
    packages=find_packages(),
    install_requires=open('requirements.in').readlines(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Intended Audience :: Developers',
        'Framework :: Pytest',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'pytest11': [
            'pytest_voluptuous = pytest_voluptuous.plugin',
        ],
    },
)
