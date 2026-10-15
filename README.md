## sentinel1-sar-datacube-analysis

Implementation of a Cloud-Based Sentinel-1 SAR Data Cube for Time-Series and Seasonal Backscatter Analysis.

This project demonstrates cloud-based Sentinel-1 SAR data processing using STAC, Dask, xarray, and Zarr. Sentinel-1 RTC imagery is retrieved from Microsoft Planetary Computer, validated using acquisition metadata, and organized into a multi-temporal data cube.

The workflow includes VV/VH backscatter time-series analysis, seasonal visualization, Zarr data cube storage, and GeoTIFF export for QGIS.

### Result snapshots

[VV backscatter time series](docs/results/vv_backscatter_timeseries.png): Temporal variation of mean VV backscatter.

[VH backscatter time series](docs/results/vh_backscatter_timeseries.png): Temporal variation of mean VH backscatter.

[VV seasonal backscatter](docs/results/vv_seasonal_backscatter.png): Seasonal VV backscatter maps.

[VH seasonal backscatter](docs/results/vh_seasonal_backscatter.png): Seasonal VH backscatter maps.

[SAR satellite overlay](docs/results/vv_sar_satellite_overlay.png): Summer VV backscatter GeoTIFF visualized over satellite imagery in QGIS.

**Keywords:** Python, STAC, Microsoft Planetary Computer, Stackstac, xarray, Dask, Zarr, Rasterio, and QGIS.

**Acknowledgment:** Inspired by [Cloud Open-Source Geospatial Data Cube Workflows](https://github.com/e-marshall/cloud-open-source-geospatial-data-cube-workflows).
