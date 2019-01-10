import os
import tempfile
import shutil

from qgis.testing import unittest, start_app

from qgis.core import (
    QgsProject, QgsLayoutExporter)

start_app()


class TestPrintLayout(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.outdir = tempfile.mkdtemp()

    def test_print_layout(self):
        export_file = os.path.join(self.outdir, 'export.pdf')

        project = QgsProject.instance()
        project.read(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data/simple_polygons.qgz'))

        layout_manager = project.layoutManager()
        layout = layout_manager.layouts()[0]
        exporter = QgsLayoutExporter(layout)

        exporter.exportToPdf(
            export_file,
            exporter.PdfExportSettings())

        self.assertTrue(os.path.isfile(export_file))
        self.assertTrue(os.path.getsize(export_file) > 0)

    @classmethod
    def tearDownClass(self):
        shutil.rmtree(self.outdir, True)
