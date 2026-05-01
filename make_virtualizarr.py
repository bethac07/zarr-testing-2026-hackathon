import marimo

__generated_with = "0.23.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import os
    import virtualizarr as vz
    import zarr
    import vizarr
    from obstore.store import HTTPStore, from_url, S3Store

    from virtualizarr.registry import ObjectStoreRegistry
    from virtualizarr import open_virtual_datatree
    from virtual_tiff import VirtualTIFF
    from virtualizarr import open_virtual_dataset

    return (
        HTTPStore,
        ObjectStoreRegistry,
        S3Store,
        VirtualTIFF,
        open_virtual_dataset,
        open_virtual_datatree,
        os,
        vizarr,
        zarr,
    )


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
def _(real, vizarr):
    #credit here and below - https://github.com/hms-dbmi/vizarr/blob/main/python/notebooks/IDR_example.ipynb
    viewer = vizarr.Viewer()
    viewer.add_image(source=real.get('A/19/1/0'), channel_axis=1,visibilities=[True]*5+[False]*3, 
        contrast_limits=[[0, 20000] for _ in range(8)],)
    viewer
    return


@app.cell
def _(HTTPStore, vizarr, zarr):
    #credit here and below - https://github.com/hms-dbmi/vizarr/blob/main/python/notebooks/IDR_example.ipynb

    # Create a remote store backed by obstore
    url = "https://cellpainting-gallery.s3.amazonaws.com/cpg0004-lincs/broad/images/2016_04_01_a549_48hr_batch1/images_zarr/SQ00014812__2016-05-23T20_44_31-Measurement1.ome.zarr"
    store = zarr.storage.ObjectStore(HTTPStore.from_url(url), read_only=True)
    real_online = zarr.open_group(store=store, mode="r")
    viewer_online = vizarr.Viewer()
    viewer_online.add_image(source=real_online.get('A/19/1/'),channel_axis=1,visibilities=[True]*5, 
        contrast_limits=[[0, 100] for _ in range(5)],)
    viewer_online
    return


@app.cell
def _(vizarr, zarr):
    # Create a remote store backed by obstore
    # This is currently not working becaue this bucket returns 403 and not 404 for missing files; I cannot at this time figure out how to do this
    url_copy = "https://cimini-lab-public.s3.amazonaws.com/zarr_att1/BR00126735__2021-09-02T10_13_59-Measurement1.ome.zarr"
    from aiohttp.client_exceptions import ClientResponseError

    store_copy = zarr.storage.FsspecStore.from_url(url_copy, allowed_exceptions=["404"])
    real_online_copy = zarr.open_group(store=store_copy, mode="r")
    viewer_online_copy = vizarr.Viewer()
    viewer_online_copy.add_image(source=real_online_copy.get('A/19/1/'), channel_axis=1,visibilities=[True]*5+[False]*3, 
        contrast_limits=[[0, 20000] for _ in range(8)],)
    viewer_online_copy
    return


app._unparsable_cell(
    r"""
    #copying here and below - https://github.com/zarr-developers/VirtualiZarr/blob/main/examples/V2/goes_basic.py

    # --- Configuration ---
    bucket = "s3://noaa-goes16"
    url = (
        "s3://noaa-goes16/ABI-L2-MCMIPF/2024/099/18/"
        "OR_ABI-L2-MCMIPF-M6_G16_s20240991800204_e20240991809524_c20240991810005.nc"
    """,
    name="_"
)


@app.cell
def _(
    ObjectStoreRegistry,
    S3Store,
    VirtualTIFF,
    open_virtual_datatree,
    vizarr,
):


    # Access a public Sentinel-2 COG from AWS
    ex_store = S3Store("sentinel-cogs", region="us-west-2", skip_signature=True)
    ex_registry = ObjectStoreRegistry({"s3://sentinel-cogs/": ex_store})
    ex_url = "s3://sentinel-cogs/sentinel-s2-l2a-cogs/12/S/UF/2022/6/S2B_12SUF_20220609_0_L2A/B04.tif"
    parser = VirtualTIFF(ifd_layout="nested")

    vdt = open_virtual_datatree(url=ex_url, parser=parser, registry=ex_registry,loadable_variables=[])
    viewer_vdt = vizarr.Viewer()
    viewer_vdt.add_image(source=vdt['2']['2'].to_numpy)
    viewer_vdt
    return ex_registry, ex_url, parser


@app.cell
def _(ex_registry, ex_url, open_virtual_dataset, parser):

    vdt_1 = open_virtual_dataset(url=ex_url, parser=parser, registry=ex_registry,loadable_variables=['x','y'])
    return (vdt_1,)


@app.cell
def _(vdt_1):
    vdt_1
    return


if __name__ == "__main__":
    app.run()
