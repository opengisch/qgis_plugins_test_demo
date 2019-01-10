from qgis.testing import unittest, start_app
from qgis.core import (
    QgsProject, QgsVectorLayer, QgsPointXY, QgsGeometry, QgsFeature)

start_app()


class TestGeometries(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_create_geometries(self):

        layer = QgsVectorLayer(
            'Polygon?crs=epsg:2056&field=value:double(1,0)',
            'polygons', "memory")

        QgsProject.instance().addMapLayers([layer])

        pos_x = 2600000
        pos_y = 1200000
        for value in range(10):
            points = []
            points.append(QgsPointXY(pos_x, pos_y))
            points.append(QgsPointXY(pos_x + 200, pos_y))
            points.append(QgsPointXY(pos_x + 200, pos_y + 10))
            points.append(QgsPointXY(pos_x, pos_y + 10))
            points.append(QgsPointXY(pos_x, pos_y))
            geometry = QgsGeometry.fromPolygonXY([points])

            feature = QgsFeature(layer.fields())
            feature.setFields(layer.fields())
            feature.setGeometry(geometry)
            layer.dataProvider().addFeatures([feature])
            pos_y += 20

        self.assertEqual(10, layer.featureCount())
