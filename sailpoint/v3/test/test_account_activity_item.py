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

from v3.models.account_activity_item import AccountActivityItem  # noqa: E501


class TestAccountActivityItem(unittest.TestCase):
    """AccountActivityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountActivityItem:
        """Test AccountActivityItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountActivityItem`
        """
        model = AccountActivityItem()  # noqa: E501
        if include_optional:
            return AccountActivityItem(
                id = '48c545831b264409a81befcabb0e3c5a',
                name = '48c545831b264409a81befcabb0e3c5a',
                requested = '2017-07-11T18:45:37.098Z',
                approval_status = 'FINISHED',
                provisioning_status = 'PENDING',
                requester_comment = v3.models.comment.Comment(
                    commenter_id = '2c918084660f45d6016617daa9210584', 
                    commenter_name = 'Adam Kennedy', 
                    body = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat.', 
                    date = '2017-07-11T18:45:37.098Z', ),
                reviewer_identity_summary = v3.models.identity_summary.IdentitySummary(
                    id = 'ff80818155fe8c080155fe8d925b0316', 
                    name = 'SailPoint Services', 
                    identity_id = 'c15b9f5cca5a4e9599eaa0e64fa921bd', 
                    completed = True, ),
                reviewer_comment = v3.models.comment.Comment(
                    commenter_id = '2c918084660f45d6016617daa9210584', 
                    commenter_name = 'Adam Kennedy', 
                    body = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat.', 
                    date = '2017-07-11T18:45:37.098Z', ),
                operation = 'ADD',
                attribute = 'detectedRoles',
                value = 'Treasury Analyst [AccessProfile-1529010191212]',
                native_identity = 'Sandie.Camero',
                source_id = '2c91808363ef85290164000587130c0c',
                account_request_info = v3.models.account_request_info.AccountRequestInfo(
                    requested_object_id = '2c91808563ef85690164001c31140c0c', 
                    requested_object_name = 'Treasury Analyst', 
                    requested_object_type = 'ACCESS_PROFILE', ),
                client_metadata = {customKey1=custom value 1, customKey2=custom value 2},
                remove_date = '2020-07-11T00:00Z'
            )
        else:
            return AccountActivityItem(
        )
        """

    def testAccountActivityItem(self):
        """Test AccountActivityItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
