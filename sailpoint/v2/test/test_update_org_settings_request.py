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

from v2.models.update_org_settings_request import UpdateOrgSettingsRequest  # noqa: E501


class TestUpdateOrgSettingsRequest(unittest.TestCase):
    """UpdateOrgSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateOrgSettingsRequest:
        """Test UpdateOrgSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateOrgSettingsRequest`
        """
        model = UpdateOrgSettingsRequest()  # noqa: E501
        if include_optional:
            return UpdateOrgSettingsRequest(
                country_codes = [
                    ''
                    ],
                enable_external_password_change = True,
                enable_automatic_password_replay = True,
                enable_automation_generation = True,
                kba_req_answers = 56,
                kba_req_for_authn = 56,
                lockout_attempt_threshold = 56,
                lockout_time_minutes = 56,
                login_url = '',
                netmasks = [
                    ''
                    ],
                notify_authentication_setting_change = True,
                password_replay_state = 'enabled',
                preferred_identity_invite_template = '',
                redirect_patterns = [
                    ''
                    ],
                sso_partner_source = '',
                system_notification_emails = [
                    ''
                    ],
                track_analytics = True,
                usage_cert_required = True,
                usage_cert_text = '',
                username_empty_text = '',
                username_label = '',
                white_list = True,
                approval_config = v2.models.get_org_settings_200_response_approval_config.getOrgSettings_200_response_approvalConfig(
                    days_till_escalation = 56, 
                    days_between_reminders = 56, 
                    max_reminders = 56, 
                    fallback_approver = '', )
            )
        else:
            return UpdateOrgSettingsRequest(
        )
        """

    def testUpdateOrgSettingsRequest(self):
        """Test UpdateOrgSettingsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
