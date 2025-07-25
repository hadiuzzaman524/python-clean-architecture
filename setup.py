from setuptools import setup, find_packages

setup(
    name='etl_covid_19',
    version='0.1',
    packages=find_packages(include=["etl_covid_19*", "config*"]),
    include_package_data=True,
)
