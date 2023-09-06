import setuptools


with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "PYRJrenderer"
AUTHOR_USER_NAME = "Rohii1515"
SRC_REPO = "PYRJrenderer"
AUTHOR_EMAIL = "rohidasjondhale1515@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A Python package for rendering",
    long_description = """
• Ready to use end-to-end project for real-world business use cases.
• This package is meant to render Websites, Docs, and Videos in Jupyter Notebooks for easy reference.
• Developed its documentation using the mkdocs-material library.
• This package is an OS-independent package as well as tested for multiple versions of python""",
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)