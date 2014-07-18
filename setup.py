from setuptools import setup


with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='Flask-Celery',
    version='0.1',
    download_url='https://github.com/lixm/flask-celery/',
    license='BSD',
    author='comyn',
    author_email='me@xueming.li',
    description='Celery for Flask',
    long_description=long_description,
    py_modules=['flask_celery'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Celery',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
