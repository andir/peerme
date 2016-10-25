#!/usr/bin/env python3

import unittest

from ..config import PeermeConfig

class PeermeBaseTests(unittest.TestCase):

    SAMPLE_CONF='tests/peerme.conf'

    def test_loading_conf(self):
        expected_conf_file = 'tests/sample.conf'
        pmc = PeermeConfig(self.SAMPLE_CONF)
        self.assertEquals(
            expected_conf_file,
            pmc.conf_file,
            'Somehow conf files do not match',
        )

if __name__ == '__main__':
    unittest.main()
