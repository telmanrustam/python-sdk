# coding: utf-8

"""
    SailPoint SaaS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from v2.models.modify_workgroup_members_request import ModifyWorkgroupMembersRequest  # noqa: E501


class TestModifyWorkgroupMembersRequest(unittest.TestCase):
    """ModifyWorkgroupMembersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ModifyWorkgroupMembersRequest:
        """Test ModifyWorkgroupMembersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ModifyWorkgroupMembersRequest`
        """
        model = ModifyWorkgroupMembersRequest()  # noqa: E501
        if include_optional:
            return ModifyWorkgroupMembersRequest(
                add = [
                    '2c9180867624cbd7017642d8c8c81f67'
                    ],
                remove = [
                    '2c9180867624cbd7017642d8c8c81f67'
                    ]
            )
        else:
            return ModifyWorkgroupMembersRequest(
        )
        """

    def testModifyWorkgroupMembersRequest(self):
        """Test ModifyWorkgroupMembersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
