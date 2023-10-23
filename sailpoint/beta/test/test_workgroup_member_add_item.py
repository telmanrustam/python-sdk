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

from beta.models.workgroup_member_add_item import WorkgroupMemberAddItem  # noqa: E501


class TestWorkgroupMemberAddItem(unittest.TestCase):
    """WorkgroupMemberAddItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkgroupMemberAddItem:
        """Test WorkgroupMemberAddItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkgroupMemberAddItem`
        """
        model = WorkgroupMemberAddItem()  # noqa: E501
        if include_optional:
            return WorkgroupMemberAddItem(
                id = '464ae7bf791e49fdb74606a2e4a89635',
                status = '201',
                description = '
> Identity is added into Governance Group members list.

> Unable to set Membership of Identity "3244d5f2d04447498520f54c6789ae33" to Governance Group "f80bba83-98c4-4ec2-81c8-373c00e9663b"; the relationship already exists.
'
            )
        else:
            return WorkgroupMemberAddItem(
                id = '464ae7bf791e49fdb74606a2e4a89635',
                status = '201',
        )
        """

    def testWorkgroupMemberAddItem(self):
        """Test WorkgroupMemberAddItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
