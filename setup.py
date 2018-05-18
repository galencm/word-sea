from setuptools import find_packages, setup
setup(
name="word sea",
    version="0.1",
    description="",
    author="Galen Curwen-McAdams",
    author_email='',
    platforms=["any"],
    license="Mozilla Public License 2.0 (MPL 2.0)",
    include_package_data=True,
    data_files = [("", ["LICENSE.txt"])],
    url="",
    packages=find_packages(),
    install_requires=[],
    entry_points = {'console_scripts': ['ws = word_sea.visual_word_count:main',
                                        ],
                            },
)
