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
from pydantic import BaseModel, Field
from beta.models.localized_message import LocalizedMessage


class CompleteInvocationInput(BaseModel):
    """
    CompleteInvocationInput
    """
    localized_error: Optional[LocalizedMessage] = Field(None,
                                                        alias="localizedError")
    output: Optional[Dict[str, Any]] = Field(
        None,
        description=
        "Trigger output that completed the invocation. Its schema is defined in the trigger definition."
    )
    __properties = ["localizedError", "output"]

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
    def from_json(cls, json_str: str) -> CompleteInvocationInput:
        """Create an instance of CompleteInvocationInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of localized_error
        if self.localized_error:
            _dict['localizedError'] = self.localized_error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CompleteInvocationInput:
        """Create an instance of CompleteInvocationInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CompleteInvocationInput.parse_obj(obj)

        _obj = CompleteInvocationInput.parse_obj({
            "localized_error":
            LocalizedMessage.from_dict(obj.get("localizedError"))
            if obj.get("localizedError") is not None else None,
            "output":
            obj.get("output")
        })
        return _obj
