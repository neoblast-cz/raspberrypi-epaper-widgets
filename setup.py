from setuptools import setup, find_packages

setup(
    name='raspberrypi-epaper-widgets',
    version='0.1.0',
    author='David Huml',
    author_email='neoblast.cz@gmail.com',
    description='A project to display widgets on a Waveshare 7.5-inch e-paper display using Raspberry Pi.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'spidev',
        'Pillow',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)