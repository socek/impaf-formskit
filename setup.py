# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'impaf',
    'formskit',
    'impaf-beaker',
]

if __name__ == '__main__':
    setup(
        name='impaf-formskit',
        version='0.1',
        description='Formskit plugin for Impaf.',
        license='Apache License 2.0',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        namespace_packages=['implugin'],
        install_requires=install_requires,
        include_package_data=True,
        zip_safe=False,
    )