VGIN_LIDAR_LAYER = (
    "https://vginmaps.vdem.virginia.gov/arcgis/rest/services/Download/"
    "Virginia_LiDAR_Downloads/MapServer/1"
)

VGIN_LIDAR_QUERY = f"{VGIN_LIDAR_LAYER}/query"

VGIN_FOOTPRINTS_LAYER = (
    "https://vginmaps.vdem.virginia.gov/arcgis/rest/services/VA_Base_Layers/"
    "VA_Building_Footprints/FeatureServer/0"
)

VGIN_FOOTPRINTS_QUERY = f"{VGIN_FOOTPRINTS_LAYER}/query"

VGIN_PARCELS_LAYER = (
    "https://vginmaps.vdem.virginia.gov/arcgis/rest/services/VA_Base_Layers/"
    "VA_Parcels/FeatureServer/0"
)

VGIN_PARCELS_QUERY = f"{VGIN_PARCELS_LAYER}/query"

USGS_LIDAR_INDEX_LAYER = (
    "https://index.nationalmap.gov/arcgis/rest/services/3DEPElevationIndex/MapServer/8"
)

USGS_LIDAR_INDEX_QUERY = f"{USGS_LIDAR_INDEX_LAYER}/query"
USGS_TNM_PRODUCTS_API = "https://tnmaccess.nationalmap.gov/api/v1/products"

USGS_LIDAR_PUBLIC_BUCKET = "https://usgs-lidar-public.s3.amazonaws.com"

MSBFP2_LAYER = (
    "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/"
    "MSBFP2/FeatureServer/0"
)

MSBFP2_QUERY = f"{MSBFP2_LAYER}/query"

MAX_RECORD_COUNT = 2000
