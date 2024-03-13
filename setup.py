from setuptools import setup

setup(
    name="diffroomacoustics",
    version="1.0.0",
    description="A Differentiable Room Acoustics Simulator written in PyTorch",
    url="https://github.com/pirl-lab/diffroomacoustics",
    author="pirl-lab",
    license="MIT",
    packages=["ism", "metrics"],
    install_requires=["numpy", "torch", "torchaudio"],
)
