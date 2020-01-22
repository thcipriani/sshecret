# -*- coding: utf8 -*-
"""
Tests for sshecret
"""
import unittest

sshecret = __import__('sshecret')


class TestGetHost(unittest.TestCase):
    """
    Test hostname extraction from args
    """
    def test_ssh_prefix(self):
        host = sshecret.get_host('ssh://example.com')
        assert host == 'example.com'

        host = sshecret.get_host('ssh://example.com:2222')
        assert host == 'example.com'

        host = sshecret.get_host('ssh://test@example.com')
        assert host == 'example.com'

        host = sshecret.get_host('ssh://test@example.com:2222')
        assert host == 'example.com'

    def test_with_at(self):
        host = sshecret.get_host('test@example.com')
        assert host == 'example.com'

        host = sshecret.get_host('test@example.com:2222')
        assert host == 'example.com'

    def test_without_domain(self):
        host = sshecret.get_host('test@example:2222')
        assert host == 'example'


class TestArgParse(unittest.TestCase):
    """
    Test argument parsing
    """
    def test_parse_known_args(self):
        args, extra = sshecret.parse_known_args(['-v', 'foo@example.com:2222'])
        assert args.verbose > 0
        assert args.hostname == 'foo@example.com:2222'
        assert not extra

    def test_socket_arg(self):
        args, extra = sshecret.parse_known_args(['--socket', 'foo@example.com:2222'])
        assert args.hostname == 'foo@example.com:2222'
        assert not extra
        assert args.sshecret_print_socket is True


if __name__ == '__main__':
    unittest.main()
