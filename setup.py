from setuptools import find_packages, setup
import colorxcode

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
    
setup(
    name = "colorxcode",
    version = colorxcode.__version__,
    description = "This is a color code conversion library.",
    packages = find_packages(exclude=([".env*", "build*", "dist*"])),
    include_package_data = True,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = "v.d.anh",
    author_email = "vdanhvt2000@gmail.com",
    url = "https://github.com/v-danh/colorxcode",
    license = "MIT",
    keywords = ["colorxcode", "conversion"],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    extras_require = {
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires = ">=3",
)