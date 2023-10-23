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

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr


class VAClusterStatusChangeEventApplication(BaseModel):
    """
    Details about the `CLUSTER` or `SOURCE` that initiated this event.  # noqa: E501
    """
    id: StrictStr = Field(..., description="The GUID of the application")
    name: StrictStr = Field(..., description="The name of the application")
    attributes: Optional[Dict[str, Any]] = Field(
        ...,
        description=
        "Custom map of attributes for a source.  This will only be populated if type is `SOURCE` and the source has a proxy."
    )
    __properties = ["id", "name", "attributes"]

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
    def from_json(cls, json_str: str) -> VAClusterStatusChangeEventApplication:
        """Create an instance of VAClusterStatusChangeEventApplication from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.attributes is None and "attributes" in self.__fields_set__:
            _dict['attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VAClusterStatusChangeEventApplication:
        """Create an instance of VAClusterStatusChangeEventApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VAClusterStatusChangeEventApplication.parse_obj(obj)

        _obj = VAClusterStatusChangeEventApplication.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "attributes":
            obj.get("attributes")
        })
        return _obj
