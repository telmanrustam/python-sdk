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

from v3.models.search_export_report_arguments import SearchExportReportArguments  # noqa: E501

class TestSearchExportReportArguments(unittest.TestCase):
    """SearchExportReportArguments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchExportReportArguments:
        """Test SearchExportReportArguments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchExportReportArguments`
        """
        model = SearchExportReportArguments()  # noqa: E501
        if include_optional:
            return SearchExportReportArguments(
                indices = [entitlements],
                filters = {source.id={type=TERMS, terms=[2c9180897termsId780bd2920576]}, source.name.exact={type=TERMS, terms=[IdentityNow], exclude=true}},
                query = v3.models.query.Query(
                    query = 'name:a*', 
                    fields = [name], 
                    time_zone = 'America/Chicago', 
                    inner_hit = v3.models.inner_hit.InnerHit(
                        query = 'source.name:\"Active Directory\"', 
                        type = 'access', ), ),
                include_nested = True,
                sort = [displayName, +id],
                default_s3_bucket = True,
                s3_bucket = 'the-dev-bucket'
            )
        else:
            return SearchExportReportArguments(
                query = v3.models.query.Query(
                    query = 'name:a*', 
                    fields = [name], 
                    time_zone = 'America/Chicago', 
                    inner_hit = v3.models.inner_hit.InnerHit(
                        query = 'source.name:\"Active Directory\"', 
                        type = 'access', ), ),
                default_s3_bucket = True,
        )
        """

    def testSearchExportReportArguments(self):
        """Test SearchExportReportArguments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
