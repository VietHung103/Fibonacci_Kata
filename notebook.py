import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #Step1: Only fibonacci signature function
    Define the test list -> expectation: all the tests would be f
    """)
    return


@app.function
def fibonacci(n):
    raise NotImplementedError


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Test list
    """)
    return


@app.function(hide_code=True)
def test_fibonacci_0():
    assert fibonacci(0) == 0


@app.function
def test_fibonacci_1():
    assert fibonacci(1) == 1


@app.function
def test_fibonacci_2():
    assert fibonacci(2) == 1


if __name__ == "__main__":
    app.run()
