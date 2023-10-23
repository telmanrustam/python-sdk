# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from beta.models.source_account import SourceAccount  # noqa: E501


class TestSourceAccount(unittest.TestCase):
    """SourceAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceAccount:
        """Test SourceAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceAccount`
        """
        model = SourceAccount()  # noqa: E501
        if include_optional:
            return SourceAccount(
                uuid = 'b7264868-7201-415f-9118-b581d431c688',
                id = 'ee769173319b41d19ccec35ba52f237b',
                native_identifier = 'E009',
                source_id = '2c918082814e693601816e09471b29b6',
                source_name = 'Active Directory',
                identity_id = 'ee769173319b41d19ccec6c235423237b',
                identity_name = 'john.doe',
                attributes = {firstname=John, lastname=Doe, email=john.doe@gmail.com, department=Sales, displayName=John Doe, created=2020-04-27T16:48:33.597Z, employeeNumber=E009, uid=E009, inactive=true, phone=null, identificationNumber=E009}
            )
        else:
            return SourceAccount(
                id = 'ee769173319b41d19ccec35ba52f237b',
                native_identifier = 'E009',
                source_id = '2c918082814e693601816e09471b29b6',
                source_name = 'Active Directory',
                identity_id = 'ee769173319b41d19ccec6c235423237b',
                identity_name = 'john.doe',
                attributes = {firstname=John, lastname=Doe, email=john.doe@gmail.com, department=Sales, displayName=John Doe, created=2020-04-27T16:48:33.597Z, employeeNumber=E009, uid=E009, inactive=true, phone=null, identificationNumber=E009},
        )
        """

    def testSourceAccount(self):
        """Test SourceAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
