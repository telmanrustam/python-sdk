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

from v3.models.object_import_result import ObjectImportResult  # noqa: E501


class TestObjectImportResult(unittest.TestCase):
    """ObjectImportResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectImportResult:
        """Test ObjectImportResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectImportResult`
        """
        model = ObjectImportResult()  # noqa: E501
        if include_optional:
            return ObjectImportResult(
                infos = [
                    v3.models.config_import/export_message.Config Import/Export Message(
                        key = 'UNKNOWN_REFERENCE_RESOLVER', 
                        text = 'Unable to resolve reference for object [type: IDENTITY, id: 2c91808c746e9c9601747d6507332ecz, name: random identity]', 
                        details = {details=message details}, )
                    ],
                warnings = [
                    v3.models.config_import/export_message.Config Import/Export Message(
                        key = 'UNKNOWN_REFERENCE_RESOLVER', 
                        text = 'Unable to resolve reference for object [type: IDENTITY, id: 2c91808c746e9c9601747d6507332ecz, name: random identity]', 
                        details = {details=message details}, )
                    ],
                errors = [
                    v3.models.config_import/export_message.Config Import/Export Message(
                        key = 'UNKNOWN_REFERENCE_RESOLVER', 
                        text = 'Unable to resolve reference for object [type: IDENTITY, id: 2c91808c746e9c9601747d6507332ecz, name: random identity]', 
                        details = {details=message details}, )
                    ],
                imported_objects = [
                    v3.models.base_reference_dto.BaseReferenceDto(
                        type = 'IDENTITY', 
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'William Wilson', )
                    ]
            )
        else:
            return ObjectImportResult(
                infos = [
                    v3.models.config_import/export_message.Config Import/Export Message(
                        key = 'UNKNOWN_REFERENCE_RESOLVER', 
                        text = 'Unable to resolve reference for object [type: IDENTITY, id: 2c91808c746e9c9601747d6507332ecz, name: random identity]', 
                        details = {details=message details}, )
                    ],
                warnings = [
                    v3.models.config_import/export_message.Config Import/Export Message(
                        key = 'UNKNOWN_REFERENCE_RESOLVER', 
                        text = 'Unable to resolve reference for object [type: IDENTITY, id: 2c91808c746e9c9601747d6507332ecz, name: random identity]', 
                        details = {details=message details}, )
                    ],
                errors = [
                    v3.models.config_import/export_message.Config Import/Export Message(
                        key = 'UNKNOWN_REFERENCE_RESOLVER', 
                        text = 'Unable to resolve reference for object [type: IDENTITY, id: 2c91808c746e9c9601747d6507332ecz, name: random identity]', 
                        details = {details=message details}, )
                    ],
                imported_objects = [
                    v3.models.base_reference_dto.BaseReferenceDto(
                        type = 'IDENTITY', 
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'William Wilson', )
                    ],
        )
        """

    def testObjectImportResult(self):
        """Test ObjectImportResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
