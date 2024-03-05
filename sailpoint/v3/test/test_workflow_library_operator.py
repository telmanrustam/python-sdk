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

from sailpoint.v3.models.workflow_library_operator import WorkflowLibraryOperator

class TestWorkflowLibraryOperator(unittest.TestCase):
    """WorkflowLibraryOperator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowLibraryOperator:
        """Test WorkflowLibraryOperator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowLibraryOperator`
        """
        model = WorkflowLibraryOperator()
        if include_optional:
            return WorkflowLibraryOperator(
                id = 'sp:compare-boolean',
                name = 'Compare Boolean Values',
                type = 'OPERATOR',
                description = 'Compare two boolean values and decide what happens based on the result.',
                form_fields = [{description=Enter the JSONPath to a value from the input to compare to Variable B., helpText=, label=Variable A, name=variableA.$, required=true, type=text}, {helpText=Select an operation., label=Operation, name=operator, options=[{label=Equals, value=BooleanEquals}], required=true, type=select}, {description=Enter the JSONPath to a value from the input to compare to Variable A., helpText=, label=Variable B, name=variableB.$, required=false, type=text}, {description=Enter True or False., helpText=, label=Variable B, name=variableB, required=false, type=text}]
            )
        else:
            return WorkflowLibraryOperator(
        )
        """

    def testWorkflowLibraryOperator(self):
        """Test WorkflowLibraryOperator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()