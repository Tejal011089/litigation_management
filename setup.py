from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='litigation_management',
    version=version,
    description='Litigation Management Details',
    author='GNU',
    author_email='saurabh.p@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
