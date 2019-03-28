from setuptools import setup

long_description = """
Koala is an end-to-end solution for modeling marketcheck data. This will serve as the baseline repo for any priceflow/TrueCar collab.
"""


setup(
    name="koala",
    packages=["koala"],  # this must be the same as the name above
    version="0.1",
    description="koala is a package for modeling Marketcheck price listings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bryan Galvin",
    author_email="bcgalvin@gmail.com",
    url="https://github.com/priceflow/koala",
    license="MIT",
    entry_points={"console_scripts": ["automl_gs=automl_gs.automl_gs:cmd"]},
    python_requires=">=3.5",
    include_package_data=True,
    install_requires=[
        "pandas",
        "scikit-learn",
        "autopep8",
        "PyAthena[SQLAlchemy]",
        "boto3",
    ],
)
