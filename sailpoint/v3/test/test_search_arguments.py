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

from v3.models.search_arguments import SearchArguments  # noqa: E501


class TestSearchArguments(unittest.TestCase):
    """SearchArguments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchArguments:
        """Test SearchArguments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchArguments`
        """
        model = SearchArguments()  # noqa: E501
        if include_optional:
            return SearchArguments(
                schedule_id = '7a724640-0c17-4ce9-a8c3-4a89738459c8',
                owner = v3.models.typed_reference.TypedReference(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', ),
                recipients = [
                    v3.models.typed_reference.TypedReference(
                        type = 'IDENTITY', 
                        id = '2c91808568c529c60168cca6f90c1313', )
                    ]
            )
        else:
            return SearchArguments(
        )
        """

    def testSearchArguments(self):
        """Test SearchArguments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
