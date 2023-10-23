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

from v3.models.non_employee_source_with_cloud_external_id import NonEmployeeSourceWithCloudExternalId  # noqa: E501


class TestNonEmployeeSourceWithCloudExternalId(unittest.TestCase):
    """NonEmployeeSourceWithCloudExternalId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self, include_optional) -> NonEmployeeSourceWithCloudExternalId:
        """Test NonEmployeeSourceWithCloudExternalId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeSourceWithCloudExternalId`
        """
        model = NonEmployeeSourceWithCloudExternalId()  # noqa: E501
        if include_optional:
            return NonEmployeeSourceWithCloudExternalId(
                id = 'a0303682-5e4a-44f7-bdc2-6ce6112549c1',
                source_id = '2c91808568c529c60168cca6f90c1313',
                name = 'Retail',
                description = 'Source description',
                approvers = [
                    v3.models.non_employee_identity_reference_with_id.NonEmployeeIdentityReferenceWithId(
                        type = 'IDENTITY', 
                        id = '5168015d32f890ca15812c9180835d2e', )
                    ],
                account_managers = [
                    v3.models.non_employee_identity_reference_with_id.NonEmployeeIdentityReferenceWithId(
                        type = 'IDENTITY', 
                        id = '5168015d32f890ca15812c9180835d2e', )
                    ],
                modified = '2019-08-23T18:52:59.162Z',
                created = '2019-08-23T18:40:35.772Z',
                cloud_external_id = '99999'
            )
        else:
            return NonEmployeeSourceWithCloudExternalId(
        )
        """

    def testNonEmployeeSourceWithCloudExternalId(self):
        """Test NonEmployeeSourceWithCloudExternalId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
