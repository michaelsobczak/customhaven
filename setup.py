from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(name='gloomtools',
        description='gloomhaven custom content tools',
        long_description='',
        version='0.1.0',
        url='git@github.com:michaelsobczak/customhaven.git',
        author='M. Sobczak',
        author_email='michaelsobczak54@gmail.com',
        license='Apache2',
        classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3'
        ],
        packages=['gloomtools'],
        install_requires=[],
        setup_requires=["pytest-runner"],
        tests_require=["pytest"],
        entry_points={
            'console_scripts': [
                'cardgen = gloomtools.__main__:main'
            ]
        },
        include_package_data=True
)
