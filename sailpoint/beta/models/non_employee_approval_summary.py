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

from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt


class NonEmployeeApprovalSummary(BaseModel):
    """
    NonEmployeeApprovalSummary
    """
    approved: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        description="The number of approved non-employee approval requests.")
    pending: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        description="The number of pending non-employee approval requests.")
    rejected: Optional[Union[StrictFloat, StrictInt]] = Field(
        None,
        description="The number of rejected non-employee approval requests.")
    __properties = ["approved", "pending", "rejected"]

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
    def from_json(cls, json_str: str) -> NonEmployeeApprovalSummary:
        """Create an instance of NonEmployeeApprovalSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeApprovalSummary:
        """Create an instance of NonEmployeeApprovalSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeApprovalSummary.parse_obj(obj)

        _obj = NonEmployeeApprovalSummary.parse_obj({
            "approved":
            obj.get("approved"),
            "pending":
            obj.get("pending"),
            "rejected":
            obj.get("rejected")
        })
        return _obj
