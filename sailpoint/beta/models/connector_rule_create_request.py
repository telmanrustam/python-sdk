# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from beta.models.connector_rule_create_request_signature import ConnectorRuleCreateRequestSignature
from beta.models.source_code import SourceCode


class ConnectorRuleCreateRequest(BaseModel):
    """
    ConnectorRuleCreateRequest  # noqa: E501
    """
    name: constr(strict=True, max_length=128,
                 min_length=1) = Field(..., description="the name of the rule")
    description: Optional[StrictStr] = Field(
        None, description="a description of the rule's purpose")
    type: StrictStr = Field(..., description="the type of rule")
    signature: Optional[ConnectorRuleCreateRequestSignature] = None
    source_code: SourceCode = Field(..., alias="sourceCode")
    attributes: Optional[Dict[str, Any]] = Field(
        None, description="a map of string to objects")
    __properties = [
        "name", "description", "type", "signature", "sourceCode", "attributes"
    ]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('BuildMap', 'ConnectorAfterCreate',
                         'ConnectorAfterDelete', 'ConnectorAfterModify',
                         'ConnectorBeforeCreate', 'ConnectorBeforeDelete',
                         'ConnectorBeforeModify', 'JDBCBuildMap',
                         'JDBCOperationProvisioning', 'JDBCProvision',
                         'PeopleSoftHRMSBuildMap',
                         'PeopleSoftHRMSOperationProvisioning',
                         'PeopleSoftHRMSProvision',
                         'RACFPermissionCustomization', 'SAPBuildMap',
                         'SapHrManagerRule', 'SapHrOperationProvisioning',
                         'SapHrProvision',
                         'SuccessFactorsOperationProvisioning',
                         'WebServiceAfterOperationRule',
                         'WebServiceBeforeOperationRule'):
            raise ValueError(
                "must be one of enum values ('BuildMap', 'ConnectorAfterCreate', 'ConnectorAfterDelete', 'ConnectorAfterModify', 'ConnectorBeforeCreate', 'ConnectorBeforeDelete', 'ConnectorBeforeModify', 'JDBCBuildMap', 'JDBCOperationProvisioning', 'JDBCProvision', 'PeopleSoftHRMSBuildMap', 'PeopleSoftHRMSOperationProvisioning', 'PeopleSoftHRMSProvision', 'RACFPermissionCustomization', 'SAPBuildMap', 'SapHrManagerRule', 'SapHrOperationProvisioning', 'SapHrProvision', 'SuccessFactorsOperationProvisioning', 'WebServiceAfterOperationRule', 'WebServiceBeforeOperationRule')"
            )
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConnectorRuleCreateRequest:
        """Create an instance of ConnectorRuleCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of signature
        if self.signature:
            _dict['signature'] = self.signature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_code
        if self.source_code:
            _dict['sourceCode'] = self.source_code.to_dict()
        # set to None if attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.attributes is None and "attributes" in self.__fields_set__:
            _dict['attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectorRuleCreateRequest:
        """Create an instance of ConnectorRuleCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectorRuleCreateRequest.parse_obj(obj)

        _obj = ConnectorRuleCreateRequest.parse_obj({
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "type":
            obj.get("type"),
            "signature":
            ConnectorRuleCreateRequestSignature.from_dict(obj.get("signature"))
            if obj.get("signature") is not None else None,
            "source_code":
            SourceCode.from_dict(obj.get("sourceCode"))
            if obj.get("sourceCode") is not None else None,
            "attributes":
            obj.get("attributes")
        })
        return _obj
