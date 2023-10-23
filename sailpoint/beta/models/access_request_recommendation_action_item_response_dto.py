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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from beta.models.access_request_recommendation_item import AccessRequestRecommendationItem


class AccessRequestRecommendationActionItemResponseDto(BaseModel):
    """
    AccessRequestRecommendationActionItemResponseDto
    """
    identity_id: Optional[StrictStr] = Field(
        None,
        alias="identityId",
        description="The identity ID taking the action.")
    access: Optional[AccessRequestRecommendationItem] = None
    timestamp: Optional[datetime] = None
    __properties = ["identityId", "access", "timestamp"]

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
    def from_json(
            cls,
            json_str: str) -> AccessRequestRecommendationActionItemResponseDto:
        """Create an instance of AccessRequestRecommendationActionItemResponseDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of access
        if self.access:
            _dict['access'] = self.access.to_dict()
        return _dict

    @classmethod
    def from_dict(
            cls,
            obj: dict) -> AccessRequestRecommendationActionItemResponseDto:
        """Create an instance of AccessRequestRecommendationActionItemResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRequestRecommendationActionItemResponseDto.parse_obj(
                obj)

        _obj = AccessRequestRecommendationActionItemResponseDto.parse_obj({
            "identity_id":
            obj.get("identityId"),
            "access":
            AccessRequestRecommendationItem.from_dict(obj.get("access"))
            if obj.get("access") is not None else None,
            "timestamp":
            obj.get("timestamp")
        })
        return _obj
