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

from v3.models.selector import Selector  # noqa: E501


class TestSelector(unittest.TestCase):
    """Selector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Selector:
        """Test Selector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Selector`
        """
        model = Selector()  # noqa: E501
        if include_optional:
            return Selector(
                type = 'LIST',
                values = [MON, WED],
                interval = 3
            )
        else:
            return Selector(
                type = 'LIST',
                values = [MON, WED],
        )
        """

    def testSelector(self):
        """Test Selector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
