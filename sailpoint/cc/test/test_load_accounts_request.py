# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from cc.models.load_accounts_request import LoadAccountsRequest  # noqa: E501


class TestLoadAccountsRequest(unittest.TestCase):
    """LoadAccountsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoadAccountsRequest:
        """Test LoadAccountsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoadAccountsRequest`
        """
        model = LoadAccountsRequest()  # noqa: E501
        if include_optional:
            return LoadAccountsRequest(
                disable_optimization = True,
                file = bytes(b'blah')
            )
        else:
            return LoadAccountsRequest(
        )
        """

    def testLoadAccountsRequest(self):
        """Test LoadAccountsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
