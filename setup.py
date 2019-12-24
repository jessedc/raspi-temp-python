from setuptools import find_packages, setup

setup(
    name="raspi-temp-python",
    version="0.0.1",
    description="Report Raspberry Pi CPU and GPU temperature data to influxdb",
    author="Jesse Collis",
    author_email="jesse@jcmultimedia.com.au",
    url="https://github.com/jessedc/raspi-temp-python",
    packages=find_packages(exclude=["*.tests"]),
    install_requires=[
        "influxdb>=5.2"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    entry_points={
        "console_scripts": [
            "temp = temperature.__main__:main",
        ],
    },
)
