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

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist


class PermissionDto(BaseModel):
    """
    Simplified DTO for the Permission objects stored in SailPoint's database. The data is aggregated from customer systems and is free-form, so its appearance can vary largely between different clients/customers.  # noqa: E501
    """
    rights: Optional[conlist(StrictStr)] = Field(
        None,
        description=
        "All the rights (e.g. actions) that this permission allows on the target"
    )
    target: Optional[StrictStr] = Field(
        None, description="The target the permission would grants rights on.")
    __properties = ["rights", "target"]

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
    def from_json(cls, json_str: str) -> PermissionDto:
        """Create an instance of PermissionDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "rights",
                              "target",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PermissionDto:
        """Create an instance of PermissionDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PermissionDto.parse_obj(obj)

        _obj = PermissionDto.parse_obj({
            "rights": obj.get("rights"),
            "target": obj.get("target")
        })
        return _obj
