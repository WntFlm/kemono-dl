from setuptools import setup, find_packages

setup(
    name="kemono-dl",  # 包名称
    # version="1.0.0",  # 版本号
    # author="WntFlm",  # 作者
    # author_email="wntflm@gmail.com",  # 作者邮箱
    # description="A short description of your package",  # 包描述
    packages=find_packages(),  # 自动发现包含的子包和模块
    install_requires=[],  # 包依赖关系
    package_data={"kemono-dl": ["src"]},
)
