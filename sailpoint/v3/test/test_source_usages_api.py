# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from v3.api.source_usages_api import SourceUsagesApi  # noqa: E501


class TestSourceUsagesApi(unittest.TestCase):
    """SourceUsagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SourceUsagesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_status_by_source_id(self) -> None:
        """Test case for get_status_by_source_id

        Finds status of source usage  # noqa: E501
        """
        pass

    def test_get_usages_by_source_id(self) -> None:
        """Test case for get_usages_by_source_id

        Returns source usage insights  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
