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

from beta.models.role_mining_session_parameters_dto import RoleMiningSessionParametersDto  # noqa: E501


class TestRoleMiningSessionParametersDto(unittest.TestCase):
    """RoleMiningSessionParametersDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> RoleMiningSessionParametersDto:
        """Test RoleMiningSessionParametersDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleMiningSessionParametersDto`
        """
        model = RoleMiningSessionParametersDto()  # noqa: E501
        if include_optional:
            return RoleMiningSessionParametersDto(
                min_num_identities_in_potential_role = 20,
                name = 'Saved RM Session - 07/10',
                prune_threshold = 5,
                saved = True,
                scope = beta.models.role_mining_session_scope.RoleMiningSessionScope(
                    identity_ids = [2c918090761a5aac0176215c46a62d58, 2c918090761a5aac01722015c46a62d42], 
                    criteria = 'source.name:DataScienceDataset', 
                    attribute_filter_criteria = {displayName={untranslated=Location: Miami}, ariaLabel={untranslated=Location: Miami}, data={displayName={translateKey=IDN.IDENTITY_ATTRIBUTES.LOCATION}, name=location, operator=EQUALS, values=[Miami]}}, ),
                type = 'SPECIALIZED',
                state = beta.models.role_mining_session_status.RoleMiningSessionStatus(),
                scoping_method = beta.models.role_mining_session_scoping_method.RoleMiningSessionScopingMethod(
                    state = 'MANUAL', )
            )
        else:
            return RoleMiningSessionParametersDto(
        )
        """

    def testRoleMiningSessionParametersDto(self):
        """Test RoleMiningSessionParametersDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
