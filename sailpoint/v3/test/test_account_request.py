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

from v3.models.account_request import AccountRequest  # noqa: E501


class TestAccountRequest(unittest.TestCase):
    """AccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountRequest:
        """Test AccountRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountRequest`
        """
        model = AccountRequest()  # noqa: E501
        if include_optional:
            return AccountRequest(
                account_id = 'John.Doe',
                attribute_requests = [
                    v3.models.attribute_request.AttributeRequest(
                        name = 'groups', 
                        op = 'Add', 
                        value = '3203537556531076', )
                    ],
                op = 'Modify',
                provisioning_target = None,
                result = v3.models.account_request_result.AccountRequest_result(
                    errors = [
                        '[ConnectorError] [
  {
    "code": "unrecognized_keys",
    "keys": [
      "groups"
    ],
    "path": [],
    "message": "Unrecognized key(s) in object: 'groups'"
  }
] (requestId: 5e9d6df5-9b1b-47d9-9bf1-dc3a2893299e)'
                        ], 
                    status = 'failed', 
                    ticket_id = '', ),
                source = None
            )
        else:
            return AccountRequest(
        )
        """

    def testAccountRequest(self):
        """Test AccountRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
