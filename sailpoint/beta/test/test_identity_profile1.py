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

from beta.models.identity_profile1 import IdentityProfile1  # noqa: E501


class TestIdentityProfile1(unittest.TestCase):
    """IdentityProfile1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityProfile1:
        """Test IdentityProfile1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityProfile1`
        """
        model = IdentityProfile1()  # noqa: E501
        if include_optional:
            return IdentityProfile1(
                id = 'id12345',
                name = 'aName',
                created = '2015-05-28T14:07:17Z',
                modified = '2015-05-28T14:07:17Z',
                description = 'My custom flat file profile',
                owner = beta.models.identity_profile_all_of_owner.IdentityProfile_allOf_owner(
                    type = 'IDENTITY', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'William Wilson', ),
                priority = 10,
                authoritative_source = beta.models.identity_profile_1_all_of_authoritative_source.IdentityProfile_1_allOf_authoritativeSource(
                    type = 'SOURCE', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'HR Active Directory', ),
                identity_refresh_required = True,
                identity_count = 8,
                identity_attribute_config = beta.models.identity_attribute_config_1.IdentityAttributeConfig_1(
                    enabled = True, 
                    attribute_transforms = [
                        beta.models.identity_attribute_transform_1.IdentityAttributeTransform_1(
                            identity_attribute_name = 'email', 
                            transform_definition = beta.models.transform_definition_1.TransformDefinition_1(
                                type = 'accountAttribute', 
                                attributes = {attributeName=e-mail, sourceName=MySource, sourceId=2c9180877a826e68017a8c0b03da1a53}, ), )
                        ], ),
                identity_exception_report_reference = beta.models.identity_exception_report_reference_1.IdentityExceptionReportReference_1(
                    task_result_id = '2b838de9-db9b-abcf-e646-d4f274ad4238', 
                    report_name = 'My annual report', ),
                has_time_based_attr = True
            )
        else:
            return IdentityProfile1(
                name = 'aName',
                authoritative_source = beta.models.identity_profile_1_all_of_authoritative_source.IdentityProfile_1_allOf_authoritativeSource(
                    type = 'SOURCE', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'HR Active Directory', ),
        )
        """

    def testIdentityProfile1(self):
        """Test IdentityProfile1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
