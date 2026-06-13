from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fitness-ai-backend",
    version="1.0.0",
    author="EminSans1",
    description="FitAnalytics API - FastAPI fitness data processing backend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["main"],
    python_requires=">=3.10",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "pydantic>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "httpx>=0.25.0",
        ],
    },
)
