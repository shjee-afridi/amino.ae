from setuptools import setup, find_packages

requirements = [
    "requests",
    "websocket-client==1.3.1", 
    "setuptools", 
    "json_minify", 
    "six",
    "aiohttp",
    "websockets"
]

with open("README.md", "r") as stream:
    long_description = stream.read()

setup(
    name="amino.ae",
    license="MIT",
    author="Reaper",
    version="1.0.0.0",
    author_email="animeempire10@gmail.com",
    description="JOIN DISCORD FOR SUPPORT https://discord.gg/NnKWCtY2F8",
    url="https://github.com/BlackReaper33/amino.ae",
    packages=find_packages(),
    long_description=long_description,
    install_requires=requirements,
    keywords=[
        'aminoapps',
        'amino.fix',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
        'minori'
    ],
    python_requires='>=3.6',
)
