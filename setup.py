from setuptools import setup, find_packages

setup(
    name="FetchGitHubStats",
    version="0.0.3",
    author="Ashlin Darius Govindasamy",
    author_email="adgrules@hotmail.com",
    url="https://www.adgstudios.co.za",
    description="Returns GitHub Users Repo's data to Pandas Dataframe",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT', 
    install_requires=["pandas","requests"]
)
