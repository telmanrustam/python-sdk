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

from v3.models.forward_approval_dto import ForwardApprovalDto  # noqa: E501


class TestForwardApprovalDto(unittest.TestCase):
    """ForwardApprovalDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ForwardApprovalDto:
        """Test ForwardApprovalDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ForwardApprovalDto`
        """
        model = ForwardApprovalDto()  # noqa: E501
        if include_optional:
            return ForwardApprovalDto(
                new_owner_id = '2c91808568c529c60168cca6f90c1314',
                comment = '2c91808568c529c60168cca6f90c1313'
            )
        else:
            return ForwardApprovalDto(
                new_owner_id = '2c91808568c529c60168cca6f90c1314',
                comment = '2c91808568c529c60168cca6f90c1313',
        )
        """

    def testForwardApprovalDto(self):
        """Test ForwardApprovalDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
