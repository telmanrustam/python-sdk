# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from v3.models.app_all_of_account import AppAllOfAccount  # noqa: E501


class TestAppAllOfAccount(unittest.TestCase):
    """AppAllOfAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAllOfAccount:
        """Test AppAllOfAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAllOfAccount`
        """
        model = AppAllOfAccount()  # noqa: E501
        if include_optional:
            return AppAllOfAccount(
                id = '2c9180837dfe6949017e21f3d8cd6d49',
                account_id = 'CN=Carol Adams,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=sailpointdemo,DC=com'
            )
        else:
            return AppAllOfAccount(
        )
        """

    def testAppAllOfAccount(self):
        """Test AppAllOfAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
