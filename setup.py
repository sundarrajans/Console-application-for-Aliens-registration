from setuptools import setup, find_packages

setup(
    name='aliens_on_earth',
    version='1.0.0',
    author='Sundar',
    author_email='sundarrajan.s66@gmail.com',
    packages=find_packages(exclude=[]),
    scripts=['register'],
    url='https://github.com/sundarrajans/Console-application-for-Aliens-registration',
    description='Aliens-on-Earth is an application to register Aliens details.' ,
    long_description=open('README.md').read(),
    install_requires=[
        "reportlab == 3.1.8"

	
       ],
)
