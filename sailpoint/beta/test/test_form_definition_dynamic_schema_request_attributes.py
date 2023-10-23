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

from beta.models.form_definition_dynamic_schema_request_attributes import FormDefinitionDynamicSchemaRequestAttributes  # noqa: E501


class TestFormDefinitionDynamicSchemaRequestAttributes(unittest.TestCase):
    """FormDefinitionDynamicSchemaRequestAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self,
            include_optional) -> FormDefinitionDynamicSchemaRequestAttributes:
        """Test FormDefinitionDynamicSchemaRequestAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormDefinitionDynamicSchemaRequestAttributes`
        """
        model = FormDefinitionDynamicSchemaRequestAttributes()  # noqa: E501
        if include_optional:
            return FormDefinitionDynamicSchemaRequestAttributes(
                form_definition_id = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return FormDefinitionDynamicSchemaRequestAttributes(
        )
        """

    def testFormDefinitionDynamicSchemaRequestAttributes(self):
        """Test FormDefinitionDynamicSchemaRequestAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
