from setuptools import setup, find_packages

setup(
    entry_points={
        'console_scripts': [
            'ascii-grid-to-png=ascii_grid_to_png.cli:cli',
        ],
    },
    name='ascii-grid-to-png',
    packages=find_packages(include=['ascii_grid_to_png'])
)
