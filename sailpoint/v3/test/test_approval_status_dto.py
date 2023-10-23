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

from v3.models.approval_status_dto import ApprovalStatusDto  # noqa: E501


class TestApprovalStatusDto(unittest.TestCase):
    """ApprovalStatusDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApprovalStatusDto:
        """Test ApprovalStatusDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApprovalStatusDto`
        """
        model = ApprovalStatusDto()  # noqa: E501
        if include_optional:
            return ApprovalStatusDto(
                forwarded = False,
                original_owner = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                current_owner = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                reviewed_by = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                modified = '2019-08-23T18:52:57.398Z',
                status = 'PENDING',
                scheme = 'MANAGER',
                error_messages = [
                    v3.models.error_message_dto.ErrorMessageDto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', )
                    ],
                comment = 'I approve this request',
                remove_date = '2020-07-11T00:00Z'
            )
        else:
            return ApprovalStatusDto(
        )
        """

    def testApprovalStatusDto(self):
        """Test ApprovalStatusDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
