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

from beta.models.provisioning_completed import ProvisioningCompleted  # noqa: E501

class TestProvisioningCompleted(unittest.TestCase):
    """ProvisioningCompleted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProvisioningCompleted:
        """Test ProvisioningCompleted
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProvisioningCompleted`
        """
        model = ProvisioningCompleted()  # noqa: E501
        if include_optional:
            return ProvisioningCompleted(
                tracking_number = '4b4d982dddff4267ab12f0f1e72b5a6d',
                sources = 'Corp AD, Corp LDAP, Corp Salesforce',
                action = 'IdentityRefresh',
                errors = [
                    'Connector AD Failed'
                    ],
                warnings = [
                    'Notification Skipped due to invalid email'
                    ],
                recipient = beta.models.provisioning_completed_recipient.ProvisioningCompleted_recipient(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                requester = beta.models.provisioning_completed_requester.ProvisioningCompleted_requester(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                account_requests = [
                    beta.models.provisioning_completed_account_requests_inner.ProvisioningCompleted_accountRequests_inner(
                        source = beta.models.provisioning_completed_account_requests_inner_source.ProvisioningCompleted_accountRequests_inner_source(
                            id = '4e4d982dddff4267ab12f0f1e72b5a6d', 
                            type = 'SOURCE', 
                            name = 'Corporate Active Directory', ), 
                        account_id = 'CN=Chewy.Bacca,ou=hardcorefigter,ou=wookies,dc=starwars,dc=com', 
                        account_operation = 'Modify', 
                        provisioning_result = SUCCESS, 
                        provisioning_target = 'Corp AD', 
                        ticket_id = '72619262', 
                        attribute_requests = [
                            beta.models.provisioning_completed_account_requests_inner_attribute_requests_inner.ProvisioningCompleted_accountRequests_inner_attributeRequests_inner(
                                attribute_name = 'memberOf', 
                                attribute_value = 'CN=jedi,DC=starwars,DC=com', 
                                operation = Add, )
                            ], )
                    ]
            )
        else:
            return ProvisioningCompleted(
                tracking_number = '4b4d982dddff4267ab12f0f1e72b5a6d',
                sources = 'Corp AD, Corp LDAP, Corp Salesforce',
                recipient = beta.models.provisioning_completed_recipient.ProvisioningCompleted_recipient(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                account_requests = [
                    beta.models.provisioning_completed_account_requests_inner.ProvisioningCompleted_accountRequests_inner(
                        source = beta.models.provisioning_completed_account_requests_inner_source.ProvisioningCompleted_accountRequests_inner_source(
                            id = '4e4d982dddff4267ab12f0f1e72b5a6d', 
                            type = 'SOURCE', 
                            name = 'Corporate Active Directory', ), 
                        account_id = 'CN=Chewy.Bacca,ou=hardcorefigter,ou=wookies,dc=starwars,dc=com', 
                        account_operation = 'Modify', 
                        provisioning_result = SUCCESS, 
                        provisioning_target = 'Corp AD', 
                        ticket_id = '72619262', 
                        attribute_requests = [
                            beta.models.provisioning_completed_account_requests_inner_attribute_requests_inner.ProvisioningCompleted_accountRequests_inner_attributeRequests_inner(
                                attribute_name = 'memberOf', 
                                attribute_value = 'CN=jedi,DC=starwars,DC=com', 
                                operation = Add, )
                            ], )
                    ],
        )
        """

    def testProvisioningCompleted(self):
        """Test ProvisioningCompleted"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
