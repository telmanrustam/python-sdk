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

from pydantic import BaseModel, Field, StrictBool, StrictStr


class AttrSyncSourceAttributeConfig(BaseModel):
    """
    Specification of source attribute sync mapping configuration for an identity attribute  # noqa: E501
    """
    name: StrictStr = Field(..., description="Name of the identity attribute")
    display_name: StrictStr = Field(
        ...,
        alias="displayName",
        description="Display name of the identity attribute")
    enabled: StrictBool = Field(
        ...,
        description=
        "Determines whether or not the attribute is enabled for synchronization"
    )
    target: StrictStr = Field(
        ...,
        description=
        "Name of the source account attribute to which the identity attribute value will be synchronized if enabled"
    )
    __properties = ["name", "displayName", "enabled", "target"]

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
    def from_json(cls, json_str: str) -> AttrSyncSourceAttributeConfig:
        """Create an instance of AttrSyncSourceAttributeConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AttrSyncSourceAttributeConfig:
        """Create an instance of AttrSyncSourceAttributeConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AttrSyncSourceAttributeConfig.parse_obj(obj)

        _obj = AttrSyncSourceAttributeConfig.parse_obj({
            "name":
            obj.get("name"),
            "display_name":
            obj.get("displayName"),
            "enabled":
            obj.get("enabled"),
            "target":
            obj.get("target")
        })
        return _obj
