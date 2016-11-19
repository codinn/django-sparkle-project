from setuptools import setup
import sparkle
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
if os.path.exists(os.path.join(dirpath, '__init__.py'))]

setup(
    name = "django-sparkle-project",
    version = sparkle.__version__,
    description = 'Django-sparkle-project is a Django application to make it easy to publish updates for your mac application using sparkle',
    long_description = README,
    url = 'http://github.com/ruuti/django-sparkle-project',
    author = 'Miikka Värri',
    author_email = 'miikka.varri@gmail.com',
    license = 'BSD',
    zip_safe = False,
    packages = get_packages('sparkle'),
    package_data=get_package_data('sparkle'),
    include_package_data = True,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)