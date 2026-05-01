import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import virtualizarr

    return (os,)


@app.cell
def _(os):
    filelist = os.listdir('/Users/bcimini/Desktop/test/BR00126735__2021-09-02T10_13_59-Measurement1/Images')
    filelist = [x for x in filelist if 'xml' not in x]
    filelist = [f"s3://cellpainting-gallery/cpg0024-bortezomib/source_4/images/2021_08_23_Batch12/images/BR00126735__2021-09-02T10_13_59-Measurement1/Images/{x}" for x in filelist]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
