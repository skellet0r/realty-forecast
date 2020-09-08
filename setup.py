import setuptools

setuptools.setup(
    name="src",
    version="1.0.0",
    url="https://www.github.com/Skellet0r/realty-forecast",
    author="Edward Amor",
    license="GPL-3.0",
    author_email="edward.amor3@gmail.com",
    packages=["src"],
    install_requires=[
        "pandas",
        "scipy",
        "numpy",
        "statsmodels",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "plotly",
        "pmdarima",
    ],
)

