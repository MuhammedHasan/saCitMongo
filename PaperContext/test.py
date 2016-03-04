import unittest
import settings
import paperead


class TestPapeRead(unittest.TestCase):

    def setUp(self):
        self.id = '10.1.1.582.1'
        settings.DATASET_PATH = 'PaperContext/test/'

    def test_id_to_path(self):
        paper_path = paperead.id_to_path(self.id, 'xml')
        self.assertEqual(paper_path, 'PaperContext/test/xml/10/1/1/582/1/')
        paper_path = paperead.id_to_path(self.id, 'text')
        self.assertEqual(paper_path, 'PaperContext/test/text/10/1/1/582/1/')

    def test_get_xml_last_version(self):
        xml_path = paperead.get_xml_last_version(self.id)
        self.assertEqual(xml_path, '10.1.1.582.1v1.xml')

    def test_get_text_paper(self):
        paper_text = paperead.get_text_paper(self.id)
        self.assertEqual(paper_text.strip(), 'Repatriation Taxes')

    def test_get_xml_paper(self):
        paper_xml = paperead.get_xml_paper(self.id)
        self.assertEqual(paper_xml['document']['@id'], self.id)
        self.assertEqual(paper_xml['document']['clusterid'], '9597914')
        self.assertEqual(paper_xml['document']['year']['#text'], '2001')


if __name__ == '__main__':
    unittest.main()
