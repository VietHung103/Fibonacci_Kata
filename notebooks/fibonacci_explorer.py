# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fibonacci-tdd-kata-viethung103",
#     "marimo>=0.10",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_tdd_kata import fibonacci

    GOLDEN_RATIO = (1 + 5**0.5) / 2


@app.cell
def _():
    mo.md(r"""
    # Fibonacci Explorer

    Pick a range of indices `n` and see the values `F(n)`, how fast they grow,
    and how the the ratio `F(n+1)/F(n)` can reach the golden ratio. This notebool
    uses the published `fibonacci_tdd_kata` package — it does not reimplement the function.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(0, 200, value=0, label="Range start")
    end = mo.ui.slider(0, 200, value=30, label="Range end")
    log_scale = mo.ui.checkbox(label="Log scale", value=True)
    mo.hstack([start, end, log_scale])
    return end, log_scale, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    ns = list(range(lo, hi + 1))
    values = [fibonacci(n) for n in ns]
    mo.ui.table(
        [{"n": n, "F(n)": str(v), "Number of digits": len(str(v))} for n, v in zip(ns, values)],
        selection=None,
    )
    return ns, values


@app.cell
def _(log_scale, ns, values):
    fig, ax = plt.subplots()
    ax.plot(ns, [float(v) for v in values], marker="o", color="#4c72b0")
    if log_scale.value and any(v > 0 for v in values):
        ax.set_yscale("log")
    ax.set_xlabel("n")
    ax.set_ylabel("F(n)")
    ax.set_title("Growth of F(n)")
    fig
    return


@app.cell
def _(ns, values):
    pairs = [(n, b / a) for n, a, b in zip(ns, values, values[1:]) if a > 0]
    if pairs:
        fig2, ax2 = plt.subplots()
        ax2.plot([n for n, _ in pairs], [r for _, r in pairs], marker="o", color="#dd8452")
        ax2.axhline(GOLDEN_RATIO, linestyle="--", color="#55a868", label="φ ≈ 1.618")
        ax2.set_xlabel("n")
        ax2.set_ylabel("F(n+1) / F(n)")
        ax2.set_title("Ratio of consecutive terms → golden ratio")
        ax2.legend()
        _out = fig2
    else:
        _out = mo.md("_Pick a range with at least two terms (and n ≥ 1) to see the ratio._")
    _out
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
