import setuptools

setuptools.setup(
    name="falconsign",
    version="0.1",
    packages=['falcon'],
    include_package_data=True,
    description='Implementation of NIST-recommended falcon-sign scheme.',
    long_description=open('README.md', 'r').read(),
    install_requires=[line.strip() for line in open('requirements.txt', 'r').readlines()]
 )
