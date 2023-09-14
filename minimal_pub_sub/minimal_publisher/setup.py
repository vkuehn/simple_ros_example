from setuptools import setup
import os
from glob import glob

package_name = 'minimal_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosusr',
    maintainer_email='rosusr@todo.todo',
    description='minimal_publisher',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'minimal_publisher = minimal_publisher.minimal_publisher:main'
        ],
    },
)
