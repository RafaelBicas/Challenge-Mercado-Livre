import unittest
import json

from flask import jsonify
from API_VirusTotal import app

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_accessHomePage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'VirusTotal API: Keep searching!', response.data)

    def test_accessHashSearcherMainPage(self):
        response = self.app.get('/hash_search')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Use the following syntax to search on API hashsearch/valid_hash', response.data)

    def test_hashSearch(self):
        valid_data = {
            "IoCs": {
                "Alerts context": [
                    {
                        "hostname": "billred229102.duckdns.org",
                        "src_ip": "37.48.118.12",
                        "src_port": 26546,
                        "url": "http://billred229102.duckdns.org/"
                    },
                    {
                        "hostname": "billred229102.duckdns.org",
                        "src_ip": "37.48.118.12",
                        "src_port": 26546,
                        "url": "http://billred229102.duckdns.org/"
                    },
                    {
                        "src_ip": "37.48.118.12",
                        "src_port": 26546
                    },
                    {
                        "dest_ip": "37.48.118.12",
                        "dest_port": 26546
                    },
                    {
                        "dest_ip": "37.48.118.12",
                        "dest_port": 26546
                    },
                    {
                        "dest_ip": "8.8.8.8",
                        "dest_port": 53
                    },
                    {
                        "dest_ip": "37.48.118.12",
                        "dest_port": 26546,
                        "hostname": "billred229102.duckdns.org",
                        "url": "http://billred229102.duckdns.org/"
                    },
                    {
                        "dest_ip": "8.8.8.8",
                        "dest_port": 53
                    },
                    {
                        "dest_ip": "37.48.118.12",
                        "dest_port": 26546,
                        "hostname": "billred229102.duckdns.org",
                        "url": "http://billred229102.duckdns.org/"
                    }
                ]
            },
            "Malware informations": {
                "Popular threat classification": {
                    "popular_threat_category": [
                        {
                            "count": 35,
                            "value": "trojan"
                        }
                    ],
                    "popular_threat_name": [
                        {
                            "count": 17,
                            "value": "msil"
                        },
                        {
                            "count": 8,
                            "value": "remcos"
                        },
                        {
                            "count": 4,
                            "value": "redline"
                        }
                    ],
                    "suggested_threat_label": "trojan.msil/remcos"
                }
            },
            "Names": {
                "Name variations": [
                    "vgPR.exe",
                    "ced3557310b98b8a1ede8c1c24c4997a2eb2e05e561dd0b6ca36627f0d987d14.exe",
                    "Paymentslip.exe",
                    "mueIOWjsOyku.exe",
                    "Payment slip.exe"
                ],
                "Original name": "vgPR.exe"
            },
            "Votes": {
                "harmless_votes": 0,
                "malicious_votes": 59,
                "suspicious_votes": 0
            },
            "hash": {
                "md5": "c4b108f45b87751371fb6e78597772ae",
                "sha1": "e60ae2b84d36714099a929b5af304e9a40857ba6",
                "sha256": "ced3557310b98b8a1ede8c1c24c4997a2eb2e05e561dd0b6ca36627f0d987d14"
            }
        }

        response = self.app.get('/hash_search/ced3557310b98b8a1ede8c1c24c4997a2eb2e05e561dd0b6ca36627f0d987d14')
        data_returned = json.loads(response.data)
        self.assertEqual(response.status_code,200)
        self.assertDictEqual(valid_data, data_returned)

    def test_hash_search_invalid(self):
        response = self.app.get('/hash_search/billred229102')
        invalid_data = {"Erro": "Hash não encontrado"}
        response_json = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 404)
        self.assertDictEqual(invalid_data, response_json)

if __name__ == '__main__':
    unittest.main()
