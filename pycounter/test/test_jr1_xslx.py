from pycounter import pycounter
import unittest
import os

class ParseExample(unittest.TestCase):
    def setUp(self):
        self.report = pycounter.parse(os.path.join(os.path.dirname(__file__),
                                                             'data/JR1.xlsx'))

    def test_reportname(self):
        self.assertEqual(self.report.report_type, u'JR1')
        self.assertEqual(self.report.report_version, 4)

    def test_year(self):
        self.assertEqual(self.report.year, 2013)

    def test_platform(self):
        for publication in self.report:
            self.assertEqual(publication.publisher, u"American Medical Association")
            self.assertEqual(publication.platform, u"Silverchair")

    def test_stats(self):
        publication = self.report.pubs[0]
        self.assertEqual(publication.monthdata, [4, 14, 13, 30, 19, 7, 31, 6, 16, 12, 8, 12])
        publication = self.report.pubs[1]
        self.assertEqual(publication.monthdata, [5414, 5459, 4936, 5172, 4064, 3904, 4054, 4090, 5010, 6680, 5961, 3742])
