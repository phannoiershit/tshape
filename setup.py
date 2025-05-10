from setuptools import setup

setup(
    name="tshape",
    version="0.2.0",  # Tăng phiên bản
    packages=["shapes"],
    py_modules=[
        "shapes.custom",
        "shapes.hex",
        "shapes.ptg",
        "shapes.oct",
        "shapes.htt",
        "shapes.tag",
        "shapes.star",
        "shapes.sq",
    ],
    entry_points={
        "console_scripts": [
            "draw-regular=shapes.custom:main",
            "draw-hexagon=shapes.hex:main",
            "draw-pentagon=shapes.ptg:main",
            "draw-octagon=shapes.oct:main",
            "draw-heptagon=shapes.htt:main",
            "draw-triangle=shapes.tag:main",
            "draw-star=shapes.star:main",
            "draw-square=shapes.sq:main",
        ],
    },
    install_requires=[
        # Không có dependency ngoài Python chuẩn
    ],
    author="Bui Ngoc Phan vn",
    author_email="buiphan022109@gmail.com",
    description="Draw shape with 1 line",
    long_description=open("README.md").read(),  # Đọc từ README.md
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my-shape-drawer", # Thay thế bằng URL của bạn
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
