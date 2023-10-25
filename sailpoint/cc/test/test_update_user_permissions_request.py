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

from cc.models.update_user_permissions_request import UpdateUserPermissionsRequest  # noqa: E501


class TestUpdateUserPermissionsRequest(unittest.TestCase):
    """UpdateUserPermissionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateUserPermissionsRequest:
        """Test UpdateUserPermissionsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateUserPermissionsRequest`
        """
        model = UpdateUserPermissionsRequest()  # noqa: E501
        if include_optional:
            return UpdateUserPermissionsRequest(
                ids = '71624,71625',
                is_admin = '1',
                admin_type = 'ADMIN'
            )
        else:
            return UpdateUserPermissionsRequest(
        )
        """

    def testUpdateUserPermissionsRequest(self):
        """Test UpdateUserPermissionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
