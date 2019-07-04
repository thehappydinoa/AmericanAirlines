from setuptools import setup

setup(
    name='AmericanAirlines',
    version='2.0.0',
    packages=['american_airlines'],
    url='https://github.com/thehappydinoa/AmericanAirlines',
    license='',
    author='thehappydinoa',
    author_email='thehappydinoa@gmail.com',
    description='Used to get flight info on American Airlines airplanes.',
    entry_points={'console_scripts': [
        'american = american_airlines.cli:main']},
    install_requires=['requests']
)
