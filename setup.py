from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="aaanimal",
    version="0.1.0",
    rust_extensions=[RustExtension("aaanimal", "Cargo.toml", debug=False)],
    include_package_data=True,
    zip_safe=False,
)
