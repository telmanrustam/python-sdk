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
from beta.models.access_profile_usage_used_by_inner import AccessProfileUsageUsedByInner

class AccessProfileUsage(BaseModel):
    """
    AccessProfileUsage
    """
    access_profile_id: Optional[StrictStr] = Field(None, alias="accessProfileId", description="ID of the Access Profile that is in use")
    used_by: Optional[conlist(AccessProfileUsageUsedByInner)] = Field(None, alias="usedBy", description="List of references to objects which are using the indicated Access Profile")
    __properties = ["accessProfileId", "usedBy"]

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
    def from_json(cls, json_str: str) -> AccessProfileUsage:
        """Create an instance of AccessProfileUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in used_by (list)
        _items = []
        if self.used_by:
            for _item in self.used_by:
                if _item:
                    _items.append(_item.to_dict())
            _dict['usedBy'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessProfileUsage:
        """Create an instance of AccessProfileUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessProfileUsage.parse_obj(obj)

        _obj = AccessProfileUsage.parse_obj({
            "access_profile_id": obj.get("accessProfileId"),
            "used_by": [AccessProfileUsageUsedByInner.from_dict(_item) for _item in obj.get("usedBy")] if obj.get("usedBy") is not None else None
        })
        return _obj


