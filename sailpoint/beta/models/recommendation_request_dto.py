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
from pydantic import BaseModel, Field, StrictBool, conlist
from beta.models.recommendation_request import RecommendationRequest


class RecommendationRequestDto(BaseModel):
    """
    RecommendationRequestDto
    """
    requests: Optional[conlist(RecommendationRequest)] = None
    exclude_interpretations: Optional[StrictBool] = Field(
        False,
        alias="excludeInterpretations",
        description=
        "Exclude interpretations in the response if \"true\". Return interpretations in the response if this attribute is not specified."
    )
    include_translation_messages: Optional[StrictBool] = Field(
        False,
        alias="includeTranslationMessages",
        description=
        "When set to true, the calling system uses the translated messages for the specified language"
    )
    include_debug_information: Optional[StrictBool] = Field(
        False,
        alias="includeDebugInformation",
        description="Returns the recommender calculations if set to true")
    prescribe_mode: Optional[StrictBool] = Field(
        False,
        alias="prescribeMode",
        description=
        "When set to true, uses prescribedRulesRecommenderConfig to get identity attributes and peer group threshold instead of standard config."
    )
    __properties = [
        "requests", "excludeInterpretations", "includeTranslationMessages",
        "includeDebugInformation", "prescribeMode"
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
    def from_json(cls, json_str: str) -> RecommendationRequestDto:
        """Create an instance of RecommendationRequestDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RecommendationRequestDto:
        """Create an instance of RecommendationRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RecommendationRequestDto.parse_obj(obj)

        _obj = RecommendationRequestDto.parse_obj({
            "requests": [
                RecommendationRequest.from_dict(_item)
                for _item in obj.get("requests")
            ] if obj.get("requests") is not None else None,
            "exclude_interpretations":
            obj.get("excludeInterpretations")
            if obj.get("excludeInterpretations") is not None else False,
            "include_translation_messages":
            obj.get("includeTranslationMessages")
            if obj.get("includeTranslationMessages") is not None else False,
            "include_debug_information":
            obj.get("includeDebugInformation")
            if obj.get("includeDebugInformation") is not None else False,
            "prescribe_mode":
            obj.get("prescribeMode")
            if obj.get("prescribeMode") is not None else False
        })
        return _obj
