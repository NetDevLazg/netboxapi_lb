import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='netboxapi_lb',
    version='2.0.6',
    author='Lazaro Mas',
    author_email='kentik.hanzo94@gmail.com',
    description='Python3 Package to call Netbox API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NetDevLazg/netboxapi_lb',
    project_urls={
        "Bug Tracker": "https://github.com/NetDevLazg/netboxapi_lb/issues"
    },
    license='MIT',
    packages=['netboxapi_lb'],
    install_requires=['requests', 'urllib3'],
)
