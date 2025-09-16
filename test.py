import json
import unittest
import urllib3
import vcr


class TestUrllib3Cassette(unittest.TestCase):
    def test_cassette(self):
        pool_mgr = urllib3.PoolManager()

        with vcr.use_cassette("cassette.yaml"):
            response = pool_mgr.request("GET", "http://httpbin.org/gzip")

        json.loads(response.data)


if __name__ == "__main__":
    unittest.main()
