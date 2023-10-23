# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from v3.models.reassign_reference import ReassignReference


class ReviewReassign(BaseModel):
    """
    ReviewReassign
    """
    reassign: conlist(ReassignReference) = Field(...)
    reassign_to: StrictStr = Field(
        ...,
        alias="reassignTo",
        description=
        "The ID of the identity to which the certification is reassigned")
    reason: StrictStr = Field(
        ..., description="The reason comment for why the reassign was made")
    __properties = ["reassign", "reassignTo", "reason"]

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
    def from_json(cls, json_str: str) -> ReviewReassign:
        """Create an instance of ReviewReassign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in reassign (list)
        _items = []
        if self.reassign:
            for _item in self.reassign:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reassign'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReviewReassign:
        """Create an instance of ReviewReassign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReviewReassign.parse_obj(obj)

        _obj = ReviewReassign.parse_obj({
            "reassign": [
                ReassignReference.from_dict(_item)
                for _item in obj.get("reassign")
            ] if obj.get("reassign") is not None else None,
            "reassign_to":
            obj.get("reassignTo"),
            "reason":
            obj.get("reason")
        })
        return _obj
