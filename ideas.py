from qgis.core import (QgsRasterLayer, QgsPoint, QgsRaster)
import numpy as np

def color_value_for_point(raster, point):
  results = raster.dataProvider().identify(point, QgsRaster.IdentifyFormatValue).results()
  return list(results.values())

def color_values_for_raster(raster):
  width, height = raster.width(), raster.height()
  nested_list = [color_value_for_point(raster, QgsPoint(x, y)) for x in width for y in height]
  return np.array(nested_list)

raster = QgsRasterLayer("satimage.tif", "satimage")
color_values = color_values_for_raster(raster)
