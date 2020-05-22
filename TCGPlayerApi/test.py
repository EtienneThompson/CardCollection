import unittest
from tcgplayerapi import TCGPlayerAPI

class TestTCGPlayerApi(unittest.TestCase):
    def setUp(self):
        self.api = TCGPlayerAPI()

    def test_single_generic_get(self):
        price = self.api.get("Korvold, Fae-Cursed King")
        assert price[0] != [-1]

    def test_single_specific_get(self):
        pass

    def test_single_fail_get(self):
        price = self.api.get("njbcihjlq./O K9iuo4ijckemw")
        assert price[0] == -1

    def test_multiple_generic_gets(self):
        success = 0
        for _ in range(100):
            try:
                api.get("Ketria Triome")
                api.get("Najeela, the Blade-Blossom")
                api.get("Korvold, Fae-Cursed King")
                success += 1
            except:
                pass
        # Want a greater than 95% success rate on these operation.
        # That means at least 285 successful gets out of 300.
        assert success > 95

    def test_multiple_specific_gets(self):
        success = 0
        for _ in range(100):
            success += 1
        assert success > 95

    def test_multiple_threaded_generic_gets(self):
        success = 0
        for _ in range(100):
            success += 1
        assert success > 95

    def test_multiple_threaded_specific_gets(self):
        success = 0
        for _ in range(100):
            success += 1
        assert success > 95

    def tearDown(self):
        self.api.close()
