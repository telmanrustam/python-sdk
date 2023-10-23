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

from typing import Any, Dict
from pydantic import BaseModel, Field, StrictStr


class SpConfigMessage(BaseModel):
    """
    Message model for Config Import/Export.  # noqa: E501
    """
    key: StrictStr = Field(..., description="Message key.")
    text: StrictStr = Field(..., description="Message text.")
    details: Dict[str, Dict[str, Any]] = Field(
        ..., description="Message details if any, in key:value pairs.")
    __properties = ["key", "text", "details"]

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
    def from_json(cls, json_str: str) -> SpConfigMessage:
        """Create an instance of SpConfigMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpConfigMessage:
        """Create an instance of SpConfigMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpConfigMessage.parse_obj(obj)

        _obj = SpConfigMessage.parse_obj({
            "key": obj.get("key"),
            "text": obj.get("text"),
            "details": obj.get("details")
        })
        return _obj
