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

from v2.models.get_org_settings200_response_system_notification_config_notifications_inner_thresholds import GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds  # noqa: E501


class TestGetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds(
        unittest.TestCase):
    """GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds:
        """Test GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds`
        """
        model = GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds()  # noqa: E501
        if include_optional:
            return GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds(
                healthy = '',
                unhealthy = ''
            )
        else:
            return GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds(
        )
        """

    def testGetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds(
            self):
        """Test GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
