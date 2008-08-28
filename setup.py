import os
from setuptools import setup
from setuptools import find_packages

NAME = 'CMFUid'

here = os.path.abspath(os.path.dirname(__file__))
package = os.path.join(here, 'Products', NAME)

def _package_doc(name):
    f = open(os.path.join(package, name))
    return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'
README = ( _package_doc('README.txt')
         + _boundary
         + _package_doc('CHANGES.txt')
         + _boundary
         + "Download\n========"
         )

setup(name='Products.%s' % NAME,
      version=_package_doc('version.txt').strip(),
      description='Uid product for the Zope Content Management Framework',
      long_description=README,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        ],
      keywords='web application server zope zope2 cmf',
      author="Zope Corporation and contributors",
      author_email="zope-cmf@zope.org",
      url="http://pypi.python.org/pypi/Products.CMFUid",
      license="ZPL 2.1 (http://www.zope.org/Resources/License/ZPL-2.1)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      install_requires=[
          #'Zope >= 2.10.4',
          'setuptools',
          'Products.CMFCore',
          'Products.GenericSetup >= 1.3.3, <= 1.3.999',
          ],
      entry_points="""
      [zope2.initialize]
      Products.%s = Products.%s:initialize
      """ % (NAME, NAME),
      )
