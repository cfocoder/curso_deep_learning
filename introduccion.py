import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell
def _():
    import marimo as mo 

    return


@app.cell
def _():
    print("Hello")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
