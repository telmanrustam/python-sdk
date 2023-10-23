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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from beta.models.common_access_item_access import CommonAccessItemAccess
from beta.models.common_access_item_state import CommonAccessItemState


class CommonAccessItemResponse(BaseModel):
    """
    CommonAccessItemResponse
    """
    id: Optional[StrictStr] = Field(None, description="Common Access Item ID")
    access: Optional[CommonAccessItemAccess] = None
    status: Optional[CommonAccessItemState] = None
    last_updated: Optional[StrictStr] = Field(None, alias="lastUpdated")
    reviewed_by_user: Optional[StrictBool] = Field(None,
                                                   alias="reviewedByUser")
    last_reviewed: Optional[StrictStr] = Field(None, alias="lastReviewed")
    created_by_user: Optional[StrictStr] = Field(None, alias="createdByUser")
    __properties = [
        "id", "access", "status", "lastUpdated", "reviewedByUser",
        "lastReviewed", "createdByUser"
    ]

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
    def from_json(cls, json_str: str) -> CommonAccessItemResponse:
        """Create an instance of CommonAccessItemResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of access
        if self.access:
            _dict['access'] = self.access.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CommonAccessItemResponse:
        """Create an instance of CommonAccessItemResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CommonAccessItemResponse.parse_obj(obj)

        _obj = CommonAccessItemResponse.parse_obj({
            "id":
            obj.get("id"),
            "access":
            CommonAccessItemAccess.from_dict(obj.get("access"))
            if obj.get("access") is not None else None,
            "status":
            obj.get("status"),
            "last_updated":
            obj.get("lastUpdated"),
            "reviewed_by_user":
            obj.get("reviewedByUser"),
            "last_reviewed":
            obj.get("lastReviewed"),
            "created_by_user":
            obj.get("createdByUser")
        })
        return _obj
