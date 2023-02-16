from setuptools import find_packages, setup

setup(
    name="sierra",
    version="v2.2.0",
    author="Pranav and Siddhesh",
    author_email="brainstormyourwayin@gmail.com",
    description="Sierra is a micro templating library for web frameworks in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Apache Software License",
    url="http://github.com/BrainStormYourWayIn/sierra",
    project_urls={
        "Bug Tracker": "https://github.com/BrainStormYourWayIn/sierra/issues",
        "Documentation": "https://brainstormyourwayin.github.io/sierra.github.io/",
    },
    packages=find_packages(where="src"),
    keywords=[
        "css",
        "html",
        "web development",
        "web framework",
        "templating",
        "python to HTML",
        "python to CSS",
        "jinja",
        "django",
    ],
    install_requires=["pandas", "beautifulsoup4"],
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "src"},
    python_requires=">=3.4",
)
