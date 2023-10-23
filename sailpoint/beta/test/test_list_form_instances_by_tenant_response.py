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

from beta.models.list_form_instances_by_tenant_response import ListFormInstancesByTenantResponse  # noqa: E501


class TestListFormInstancesByTenantResponse(unittest.TestCase):
    """ListFormInstancesByTenantResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> ListFormInstancesByTenantResponse:
        """Test ListFormInstancesByTenantResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListFormInstancesByTenantResponse`
        """
        model = ListFormInstancesByTenantResponse()  # noqa: E501
        if include_optional:
            return ListFormInstancesByTenantResponse(
                count = 1,
                results = [
                    beta.models.form_instance_response.FormInstanceResponse(
                        created = '2023-07-12T20:14:57.744860Z', 
                        created_by = beta.models.form_instance_created_by.FormInstanceCreatedBy(
                            id = '00000000-0000-0000-0000-000000000000', 
                            type = 'WORKFLOW_EXECUTION', ), 
                        expire = '2023-08-12T20:14:57.74486Z', 
                        form_conditions = [
                            beta.models.form_condition.FormCondition(
                                effects = [
                                    beta.models.condition_effect.ConditionEffect(
                                        config = {}, 
                                        effect_type = 'HIDE', )
                                    ], 
                                rule_operator = 'AND', 
                                rules = [
                                    beta.models.condition_rule.ConditionRule(
                                        operator = 'EQ', 
                                        source = 'department', 
                                        source_type = 'ELEMENT', 
                                        value = Engineering, 
                                        value_type = 'STRING', )
                                    ], )
                            ], 
                        form_data = {department=Engineering}, 
                        form_definition_id = '00000000-0000-0000-0000-000000000000', 
                        form_elements = [
                            beta.models.form_element.FormElement(
                                config = {label=Department}, 
                                element_type = 'TEXT', 
                                id = '00000000-0000-0000-0000-000000000000', 
                                key = 'department', 
                                validations = [{validationType=REQUIRED}], )
                            ], 
                        form_errors = [
                            beta.models.form_error.FormError(
                                key = 'department', 
                                messages = [
                                    beta.models.error_message_is_the_standard_api_error_response_message_type/.ErrorMessage is the standard API error response message type.(
                                        locale = 'en-US', 
                                        locale_origin = 'DEFAULT', 
                                        text = 'This is an error', )
                                    ], 
                                value = Engineering, )
                            ], 
                        form_input = {input1=Sales}, 
                        id = '00000000-0000-0000-0000-000000000000', 
                        modified = '2023-07-12T20:14:57.744860Z', 
                        recipients = [
                            beta.models.form_instance_recipient.FormInstanceRecipient(
                                id = '00000000-0000-0000-0000-000000000000', 
                                type = 'IDENTITY', )
                            ], 
                        stand_alone_form = False, 
                        stand_alone_form_url = 'https://my-org.identitynow.com/ui/d/forms/00000000-0000-0000-0000-000000000000', 
                        state = 'ASSIGNED', )
                    ]
            )
        else:
            return ListFormInstancesByTenantResponse(
        )
        """

    def testListFormInstancesByTenantResponse(self):
        """Test ListFormInstancesByTenantResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
