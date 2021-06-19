from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="adjective-adjective-animal",
    version="0.1.0",
    rust_extensions=[
        RustExtension("adjective_adjective_animal", "Cargo.toml", debug=False)
    ],
    include_package_data=True,
    zip_safe=False,
)
