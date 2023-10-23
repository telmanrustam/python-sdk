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

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from beta.models.access_request_item_response import AccessRequestItemResponse


class AccessRequestResponse(BaseModel):
    """
    AccessRequestResponse
    """
    requester_id: Optional[StrictStr] = Field(None,
                                              alias="requesterId",
                                              description="the requester Id")
    requester_name: Optional[StrictStr] = Field(
        None, alias="requesterName", description="the requesterName")
    items: Optional[conlist(AccessRequestItemResponse)] = None
    __properties = ["requesterId", "requesterName", "items"]

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
    def from_json(cls, json_str: str) -> AccessRequestResponse:
        """Create an instance of AccessRequestResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessRequestResponse:
        """Create an instance of AccessRequestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRequestResponse.parse_obj(obj)

        _obj = AccessRequestResponse.parse_obj({
            "requester_id":
            obj.get("requesterId"),
            "requester_name":
            obj.get("requesterName"),
            "items": [
                AccessRequestItemResponse.from_dict(_item)
                for _item in obj.get("items")
            ] if obj.get("items") is not None else None
        })
        return _obj
