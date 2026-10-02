# Fiboncci TDD Kata 
The project related to Refresher in Computer Science in Master 1 Data Science. The aims of this project
are:
- Using uv to control python env, create project.
- Unit test.
- Working with marimo.
- Applied github's knowledge of previous project.
- Publish the interactive notebook to Github page via WASM.
- Follow more professional structure of one project

## Structure of this project
```
fibonacci-tdd-kata
        |
        |
        |
        |_____ .github/workflows (contain all workflows of github repo)
        |
        |
        |_____ src( main code for developers)
        |
        |
        |_____ tests (contain all unit tests)
        |
        |
        |
        |_____ notebooks (file notebook)
```
## Publish Package
In this project i aslo public the fibonacci_tdd_kata package using PyPI, you can access to follow links https://pypi.org/project/fibonacci-tdd-kata-viethung103/ to install package by following way:

```bash
pip install fibonacci-tdd-kata-viethung103
# or
uv add fibonacci-tdd-kata-viethung103
```

## Interactive notebook (WASM)
You can clone project home github by using:
```bash
git clone https://github.com/VietHung103/Fibonacci_Kata.git
cd Fibonacci_Kata
uv sync --all-groups
```
Then, build and preview it locally:

```bash
uv run marimo export html-wasm notebooks/fibonacci_explorer.py -o site --mode run
uv run python -m http.server -d site
# open http://localhost:8000
```
## Publish Github Page
You can follow below link to visit my github page about this project :  https://viethung103.github.io/Fibonacci_Kata/
