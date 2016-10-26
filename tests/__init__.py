import os
from click.testing import CliRunner

from unittest import TestCase

from peerme.main import main, add_internal_modules
from peerme.config import PeermeConfig


#class ConfigTests(TestCase):
#
#    SAMPLE_CONF='tests/peerme.conf'
#
#    def test_loading_conf(self):
#        expected_conf_file = 'tests/sample.conf'
#        pmc = PeermeConfig(self.SAMPLE_CONF)
#        self.assertEqual(
#            expected_conf_file,
#            pmc.conf_file,
#            'Somehow conf files do not match',
#        )


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        add_internal_modules()

    def setUp(self):
        self.runner = CliRunner()
        self.main = main

    def invokeCli(self, *args, **kwargs):
        default_map = {
            'main': {
                'config': os.environ.get('PEERME_CONFIG', 'tests/peerme.conf')
            }
        }
        kwargs['default_map'] = default_map
        result = self.runner.invoke(self.main, *args, **kwargs)
        self.assertIsNone(result.exception, result.exception)
        return result



class ExampleTests(BaseTest):
    def test_pdbsql(self):
        for command in [
            ('-s', 'pdbsql', 'discover', '-d', '32934'),
            ('-s', 'pdbsql', 'generate', '-d', '15169', '-t', 'generic.template'),
        ]:

            result = self.invokeCli(command)
            desc = '{}: {}'.format(command, result.output)
            self.assertEqual(result.exit_code, 0, desc)

    def test_pdbapi(self):
        for command in [
            ('-s', 'pdbapi', 'discover', '-d', '32934'),
            ('-s', 'pdbapi', 'generate', '-d', '15169', '-t', 'ios.template'),
        ]:

            result = self.invokeCli(command)
            desc = '{}: {}'.format(command, result.output)
            self.assertEqual(result.exit_code, 0, desc)

    def test_euroix(self):
        for command in [
            "-s euroix --refresh-data discover -d 32934",
            "-s euroix discover -d 32934",
            "-s euroix discover -i FranceIX-MRS",
            "-s euroix discover -d 8218 -i FranceIX-PAR",
            "-s euroix generate -i FranceIX-PAR -t ios-xr.template",
            "-s euroix generate -d 8218 -i FranceIX-PAR -t ios.template",
            "-s euroix generate -d 15169 -t junos.template",
        ]:
            result = self.invokeCli(command.split(' '))
            desc = '{}: {}'.format(command, result.output)
            self.assertEqual(result.exit_code, 0, desc)

