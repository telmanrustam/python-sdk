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

from v3.models.account_attributes_create import AccountAttributesCreate  # noqa: E501


class TestAccountAttributesCreate(unittest.TestCase):
    """AccountAttributesCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountAttributesCreate:
        """Test AccountAttributesCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountAttributesCreate`
        """
        model = AccountAttributesCreate()  # noqa: E501
        if include_optional:
            return AccountAttributesCreate(
                attributes = {sourceId=34bfcbe116c9407464af37acbaf7a4dc, city=Austin, displayName=John Doe, userName=jdoe, sAMAccountName=jDoe, mail=john.doe@sailpoint.com}
            )
        else:
            return AccountAttributesCreate(
                attributes = {sourceId=34bfcbe116c9407464af37acbaf7a4dc, city=Austin, displayName=John Doe, userName=jdoe, sAMAccountName=jDoe, mail=john.doe@sailpoint.com},
        )
        """

    def testAccountAttributesCreate(self):
        """Test AccountAttributesCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
