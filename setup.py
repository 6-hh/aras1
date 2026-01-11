from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aras1",
    version="1.0.2", 
    author="W4_M4",
    author_email="",
    description="Instagram, TikTok, Yopmail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/6-hh/aras1",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: Arabic",
    ],
    python_requires=">=3.6",
    keywords="aras Logo 2",
    project_urls={
        "Bug Reports": "https://github.com/6-hh/aras1/issues",
        "Source": "https://github.com/6-hh/aras1",
        "Telegram": "https://t.me/W4_M4",
    },
