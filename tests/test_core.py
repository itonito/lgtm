import unittest
class LgtmTest(unittest.TestCase): 
    @unittest.skip('Work in progress')
    def test_lgtm(self):
        from lgtm.core import lgtm 
        self.assertIsNone(lgtm('./python.jpeg', 'LGTM'))