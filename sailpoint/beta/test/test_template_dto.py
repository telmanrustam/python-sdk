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

from beta.models.template_dto import TemplateDto  # noqa: E501


class TestTemplateDto(unittest.TestCase):
    """TemplateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplateDto:
        """Test TemplateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplateDto`
        """
        model = TemplateDto()  # noqa: E501
        if include_optional:
            return TemplateDto(
                key = 'cloud_manual_work_item_summary',
                name = 'Task Manager Subscription',
                medium = 'EMAIL',
                locale = 'en',
                subject = 'You have $numberOfPendingTasks $taskTasks to complete in ${__global.productName}.',
                header = '',
                body = 'Please go to the task manager',
                footer = '',
                var_from = '$__global.emailFromAddress',
                reply_to = '$__global.emailFromAddress',
                description = 'Daily digest - sent if number of outstanding tasks for task owner > 0',
                id = 'c17bea3a-574d-453c-9e04-4365fbf5af0b',
                created = '2020-01-01T00:00Z',
                modified = '2020-01-01T00:00Z'
            )
        else:
            return TemplateDto(
                key = 'cloud_manual_work_item_summary',
                medium = 'EMAIL',
                locale = 'en',
        )
        """

    def testTemplateDto(self):
        """Test TemplateDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
