import os
from setuptools import (
  setup,
  find_packages,
)
import cmsplugin_userprofiles


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='cmsplugin-userprofiles',
    version=cmsplugin_userprofiles.__version__,
    classifiers = (
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ),
    packages=find_packages(),
    install_requires=(
        'django-cms',
    ),
    author='Zenobius Jiricek',
    author_email='airtonix@gmail.com',
    description='DjangoCMS plugin that allows for placement of userprofiles',
    long_description = read('README.md'),
    license='BSD',
    keywords='django-cms, django-profiles, plugin, pages',
    url='http://github.com/airtonix/cmsplugin-userprofiles',
    include_package_data=True,
    zip_safe = False,
)
