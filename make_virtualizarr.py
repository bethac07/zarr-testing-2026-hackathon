import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import virtualizarr
    import zarr
    import vizarr

    return os, vizarr, zarr


@app.cell
def _(os):
    filelist = os.listdir('/Users/bcimini/Desktop/test/BR00126735__2021-09-02T10_13_59-Measurement1/Images')
    filelist = [x for x in filelist if 'xml' not in x]
    filelist = [f"s3://cellpainting-gallery/cpg0024-bortezomib/source_4/images/2021_08_23_Batch12/images/BR00126735__2021-09-02T10_13_59-Measurement1/Images/{x}" for x in filelist]
    return


@app.cell
def _(zarr):
    real = zarr.open('/Users/bcimini/Desktop/test/BR00126735__2021-09-02T10_13_59-Measurement1.ome.zarr')
    return (real,)


@app.cell
def _(real):
    im = real.get('A/19/1/0')
    print(im.shape)
    return


@app.cell
def _(real, vizarr):
    viewer = vizarr.Viewer()
    viewer.add_image(source=real.get('A/19/1/0'), channel_axis=1)
    viewer
    return


@app.cell
def _(zarr):
    real_online = zarr.open('https://cellpainting-gallery.s3.amazonaws.com/cpg0004-lincs/broad/images/2016_04_01_a549_48hr_batch1/images_zarr/SQ00014812__2016-05-23T20_44_31-Measurement1.ome.zarr')
    return (real_online,)


@app.cell
def _(real_online):
    well = real_online.get('A/19/1/0')
    return (well,)


@app.cell
def _(vizarr, well):
    viewer_online = vizarr.Viewer()
    viewer_online.add_image(source=well)
    viewer_online
    return


if __name__ == "__main__":
    app.run()
