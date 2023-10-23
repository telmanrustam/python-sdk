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

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from beta.models.subscription_patch_request_inner_value import SubscriptionPatchRequestInnerValue


class SubscriptionPatchRequestInner(BaseModel):
    """
    A JSONPatch Operation as defined by [RFC 6902 - JSON Patch](https://tools.ietf.org/html/rfc6902)  # noqa: E501
    """
    op: StrictStr = Field(..., description="The operation to be performed")
    path: StrictStr = Field(
        ...,
        description=
        "A string JSON Pointer representing the target path to an element to be affected by the operation"
    )
    value: Optional[SubscriptionPatchRequestInnerValue] = None
    __properties = ["op", "path", "value"]

    @validator('op')
    def op_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('add', 'remove', 'replace', 'move', 'copy'):
            raise ValueError(
                "must be one of enum values ('add', 'remove', 'replace', 'move', 'copy')"
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
    def from_json(cls, json_str: str) -> SubscriptionPatchRequestInner:
        """Create an instance of SubscriptionPatchRequestInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionPatchRequestInner:
        """Create an instance of SubscriptionPatchRequestInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionPatchRequestInner.parse_obj(obj)

        _obj = SubscriptionPatchRequestInner.parse_obj({
            "op":
            obj.get("op"),
            "path":
            obj.get("path"),
            "value":
            SubscriptionPatchRequestInnerValue.from_dict(obj.get("value"))
            if obj.get("value") is not None else None
        })
        return _obj
