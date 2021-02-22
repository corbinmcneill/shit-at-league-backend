# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error import Error  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_player(self):
        """Test case for get_player

        Get the shit summary for a particular player
        """
        query_string = [('summoner_name', 'summoner_name_example'),
                        ('region', 'region_example')]
        response = self.client.open(
            '/player',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root(self):
        """Test case for root

        Simple endpoint ping
        """
        response = self.client.open(
            '/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
