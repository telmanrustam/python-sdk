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

from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from v3.models.display_reference import DisplayReference
from v3.models.dto_type import DtoType


class AccessProfileRole(BaseModel):
    """
    Role  # noqa: E501
    """
    id: Optional[StrictStr] = Field(
        None, description="The unique ID of the referenced object.")
    name: Optional[StrictStr] = Field(
        None, description="The human readable name of the referenced object.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName")
    type: Optional[DtoType] = None
    description: Optional[StrictStr] = None
    owner: Optional[DisplayReference] = None
    disabled: Optional[StrictBool] = None
    revocable: Optional[StrictBool] = None
    __properties = [
        "id", "name", "displayName", "type", "description", "owner",
        "disabled", "revocable"
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
    def from_json(cls, json_str: str) -> AccessProfileRole:
        """Create an instance of AccessProfileRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessProfileRole:
        """Create an instance of AccessProfileRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessProfileRole.parse_obj(obj)

        _obj = AccessProfileRole.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "display_name":
            obj.get("displayName"),
            "type":
            obj.get("type"),
            "description":
            obj.get("description"),
            "owner":
            DisplayReference.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "disabled":
            obj.get("disabled"),
            "revocable":
            obj.get("revocable")
        })
        return _obj
