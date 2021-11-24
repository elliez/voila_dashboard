from setuptools import setup, find_packages

setup(
    name="example_package",
    version="0.2",
    description="Basic example package",
    url="https://github.com/elliez/voila_dashboard",
    author="elliez",
    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={"": "src"},  # Optional
    author_email="elliez@users.noreply.github.com",
    packages=['example_package', 'example_package_dashboard'],  # Required
    zip_safe=False,
)
