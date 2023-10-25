# coding: utf-8

"""
    SailPoint SaaS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from v2.api.governance_groups_api import GovernanceGroupsApi  # noqa: E501


class TestGovernanceGroupsApi(unittest.TestCase):
    """GovernanceGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GovernanceGroupsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_work_groups(self) -> None:
        """Test case for bulk_delete_work_groups

        Bulk delete work groups  # noqa: E501
        """
        pass

    def test_create_workgroup(self) -> None:
        """Test case for create_workgroup

        Create Work Group  # noqa: E501
        """
        pass

    def test_delete_workgroup(self) -> None:
        """Test case for delete_workgroup

        Delete Work Group By Id  # noqa: E501
        """
        pass

    def test_get_workgroup(self) -> None:
        """Test case for get_workgroup

        Get Work Group By Id  # noqa: E501
        """
        pass

    def test_list_workgroup_connections(self) -> None:
        """Test case for list_workgroup_connections

        List Work Group Connections  # noqa: E501
        """
        pass

    def test_list_workgroup_members(self) -> None:
        """Test case for list_workgroup_members

        List Work Group Members  # noqa: E501
        """
        pass

    def test_list_workgroups(self) -> None:
        """Test case for list_workgroups

        List Work Groups  # noqa: E501
        """
        pass

    def test_modify_workgroup_members(self) -> None:
        """Test case for modify_workgroup_members

        Modify Work Group Members  # noqa: E501
        """
        pass

    def test_update_workgroup(self) -> None:
        """Test case for update_workgroup

        Update Work Group By Id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
