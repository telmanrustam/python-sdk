# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from beta.api.iai_access_request_recommendations_api import IAIAccessRequestRecommendationsApi  # noqa: E501


class TestIAIAccessRequestRecommendationsApi(unittest.TestCase):
    """IAIAccessRequestRecommendationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IAIAccessRequestRecommendationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_access_request_recommendations_ignored_item(self) -> None:
        """Test case for add_access_request_recommendations_ignored_item

        Notification of Ignored Access Request Recommendations  # noqa: E501
        """
        pass

    def test_add_access_request_recommendations_requested_item(self) -> None:
        """Test case for add_access_request_recommendations_requested_item

        Notification of Requested Access Request Recommendations  # noqa: E501
        """
        pass

    def test_add_access_request_recommendations_viewed_item(self) -> None:
        """Test case for add_access_request_recommendations_viewed_item

        Notification of Viewed Access Request Recommendations  # noqa: E501
        """
        pass

    def test_add_access_request_recommendations_viewed_items(self) -> None:
        """Test case for add_access_request_recommendations_viewed_items

        Notification of Viewed Access Request Recommendations in Bulk  # noqa: E501
        """
        pass

    def test_get_access_request_recommendations(self) -> None:
        """Test case for get_access_request_recommendations

        Identity Access Request Recommendations  # noqa: E501
        """
        pass

    def test_get_access_request_recommendations_ignored_items(self) -> None:
        """Test case for get_access_request_recommendations_ignored_items

        List of Ignored Access Request Recommendations  # noqa: E501
        """
        pass

    def test_get_access_request_recommendations_requested_items(self) -> None:
        """Test case for get_access_request_recommendations_requested_items

        List of Requested Access Request Recommendations  # noqa: E501
        """
        pass

    def test_get_access_request_recommendations_viewed_items(self) -> None:
        """Test case for get_access_request_recommendations_viewed_items

        List of Viewed Access Request Recommendations  # noqa: E501
        """
        pass

    def test_get_message_catalogs(self) -> None:
        """Test case for get_message_catalogs

        Get Message catalogs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
