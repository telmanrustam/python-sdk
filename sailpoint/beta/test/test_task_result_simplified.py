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

from beta.models.task_result_simplified import TaskResultSimplified  # noqa: E501


class TestTaskResultSimplified(unittest.TestCase):
    """TaskResultSimplified unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskResultSimplified:
        """Test TaskResultSimplified
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskResultSimplified`
        """
        model = TaskResultSimplified()  # noqa: E501
        if include_optional:
            return TaskResultSimplified(
                id = 'ff8081814d977c21014da056804a0af3',
                name = 'Background Object Terminator c8f030f2-b1a6-4e33-99e8-6935bc18735d',
                description = 'Generic task for terminating data in the overlay, used by the TerminationService.',
                launcher = 'support',
                completed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                launched = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                completion_status = 'Success'
            )
        else:
            return TaskResultSimplified(
        )
        """

    def testTaskResultSimplified(self):
        """Test TaskResultSimplified"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
