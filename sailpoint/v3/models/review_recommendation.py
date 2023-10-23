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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist


class ReviewRecommendation(BaseModel):
    """
    ReviewRecommendation
    """
    recommendation: Optional[StrictStr] = Field(
        None,
        description=
        "The recommendation from IAI at the time of the decision. This field will be null if no recommendation was made."
    )
    reasons: Optional[conlist(StrictStr)] = Field(
        None, description="A list of reasons for the recommendation.")
    timestamp: Optional[datetime] = Field(
        None, description="The time at which the recommendation was recorded.")
    __properties = ["recommendation", "reasons", "timestamp"]

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
    def from_json(cls, json_str: str) -> ReviewRecommendation:
        """Create an instance of ReviewRecommendation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if recommendation (nullable) is None
        # and __fields_set__ contains the field
        if self.recommendation is None and "recommendation" in self.__fields_set__:
            _dict['recommendation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReviewRecommendation:
        """Create an instance of ReviewRecommendation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReviewRecommendation.parse_obj(obj)

        _obj = ReviewRecommendation.parse_obj({
            "recommendation":
            obj.get("recommendation"),
            "reasons":
            obj.get("reasons"),
            "timestamp":
            obj.get("timestamp")
        })
        return _obj
