# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from beta.api.search_attribute_configuration_api import SearchAttributeConfigurationApi  # noqa: E501


class TestSearchAttributeConfigurationApi(unittest.TestCase):
    """SearchAttributeConfigurationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SearchAttributeConfigurationApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_search_attribute_config(self) -> None:
        """Test case for create_search_attribute_config

        Configure/create extended search attributes in IdentityNow.  # noqa: E501
        """
        pass

    def test_delete_search_attribute_config(self) -> None:
        """Test case for delete_search_attribute_config

        Delete an extended search attribute in IdentityNow.  # noqa: E501
        """
        pass

    def test_get_search_attribute_config(self) -> None:
        """Test case for get_search_attribute_config

        Retrieve a list of extended search attributes in IdentityNow.  # noqa: E501
        """
        pass

    def test_get_single_search_attribute_config(self) -> None:
        """Test case for get_single_search_attribute_config

        Get the details of a specific extended search attribute in IdentityNow.  # noqa: E501
        """
        pass

    def test_patch_search_attribute_config(self) -> None:
        """Test case for patch_search_attribute_config

        Update the details of a specific extended search attribute in IdentityNow.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
