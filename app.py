from osgeo import gdal,ogr,osr
from itertools import groupby 

def receives_two_anchored_rasters(picture1,picture2):
    image1=gdal.Open(f'pictuers/{picture1}')
    image2=gdal.Open(f'pictuers/{picture2}')
    gt1=image1.GetGeoTransform()
    gt2=image2.GetGeoTransform()
    pixelSizeX1 =gt1[1]
    pixelSizeY1 =-gt1[5]
    pixelSizeX2 =gt2[1]
    pixelSizeY2 =-gt2[5]
    if((image1.RasterXSize/(pixelSizeX1*pixelSizeY1))>(image2.RasterXSize/(pixelSizeX2*pixelSizeY2))):
        return 'image 1'
    return 'image 2'

def create_raster():
    image3=gdal.Open('pictuers/3.jpg')
    a=gdal.Translate('pictuers/6.jpg', image3, projWin = (0,0,image3.RasterXSize,image3.RasterYSize/2))
    image2=gdal.Open('pictuers/2.jpg')
    b=gdal.Translate('pictuers/6.jpg', image2, projWin =(0,image2.RasterYSize/2,image2.RasterXSize,image2.RasterYSize))
    g = gdal.Warp("pictuers/6.jpg", [a,b],transformerOptions = [ 'SRC_METHOD=NO_GEOTRANSFORM', 'DST_METHOD=NO_GEOTRANSFORM'],width=2500,height=1400)
    g = None # Close file and flush to disk
    
def open_file_tiff(dataset,band):
    format = 'GTiff'
    gdal.SetConfigOption('GDAL_TIFF_INTERNAL_MASK','YES')
    
    out_driver=gdal.GetDriverByName(format)
    outdataset = out_driver.Create('mask.tif', dataset.RasterXSize, dataset.RasterYSize, dataset.RasterCount)
    outdataset.CreateMaskBand(gdal.GMF_PER_DATASET)
    
    gt=dataset.GetGeoTransform()
    outdataset.SetGeoTransform(gt)
    
    prj = dataset.GetProjectionRef()
    outdataset.SetProjection(prj)
    outband = outdataset.GetRasterBand(1)
    outmaskband=outband.GetMaskBand()
    outmaskband.WriteArray(band)
 
def maxlong(arr):
    try:    
        return len(max([list(group) for _, group in groupby(arr)], key=len))
    except:
        return 0   
            
def is_gray():
    dataset = gdal.Open('pictuers/4.jpg')
    band1 = dataset.GetRasterBand(1).ReadAsArray()
    band2 = dataset.GetRasterBand(2).ReadAsArray()
    band3 = dataset.GetRasterBand(3).ReadAsArray()
    arr=[]
    arrindex=[]
    count=0
    positioninline=0
    line=0
    for index in range(len(band1)):
        for i in range(len(band1[index])):
            if(band1[index][i]==band2[index][i]==band3[index][i]):
                band1[index][i]=1
                arrindex.append(i)
            else:
                band1[index][i]=0
        maxindex=maxlong(arrindex)
        arrindex=[] 
        if(count < maxindex):
            count = maxindex  
            line = index
            positioninline=i
            arr.append([count,line,positioninline])
    for i in range(positioninline+count):
        band1[line][i]=2
    open_file_tiff(dataset,band1)




    

    
   
