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
from pydantic import BaseModel, Field, StrictStr
from v3.models.dto_type import DtoType


class TaggedObjectDto(BaseModel):
    """
    TaggedObjectDto
    """
    type: Optional[DtoType] = None
    id: Optional[StrictStr] = Field(
        None, description="ID of the object to which this reference applies")
    name: Optional[StrictStr] = Field(
        None,
        description=
        "Human-readable display name of the object to which this reference applies"
    )
    __properties = ["type", "id", "name"]

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
    def from_json(cls, json_str: str) -> TaggedObjectDto:
        """Create an instance of TaggedObjectDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaggedObjectDto:
        """Create an instance of TaggedObjectDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaggedObjectDto.parse_obj(obj)

        _obj = TaggedObjectDto.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj
