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

from v3.models.access_profile_source_ref import AccessProfileSourceRef  # noqa: E501


class TestAccessProfileSourceRef(unittest.TestCase):
    """AccessProfileSourceRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessProfileSourceRef:
        """Test AccessProfileSourceRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessProfileSourceRef`
        """
        model = AccessProfileSourceRef()  # noqa: E501
        if include_optional:
            return AccessProfileSourceRef(
                id = '2c91809773dee3610173fdb0b6061ef4',
                type = 'SOURCE',
                name = 'ODS-AD-SOURCE'
            )
        else:
            return AccessProfileSourceRef(
        )
        """

    def testAccessProfileSourceRef(self):
        """Test AccessProfileSourceRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
