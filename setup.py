import huepy

from setuptools import find_packages, setup

name = 'huepy'
version = huepy.__version__

setup(
    name=name,
    version=version,
    url='https://github.com/s0md3v/hue',
    download_url='https://github.com/s0md3v/hue/tarball/master',
    author='Somdev Sangwan',
    author_email='s0md3v@gmail.com',
    description='Print awesomely in terminals.',
    keywords='hue, huepy, terminal color, python color',
    packages=find_packages(),
    py_modules=['huepy'],
    data_files=[('', ['LICENSE'])],
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])
