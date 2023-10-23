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
from pydantic import BaseModel, Field, StrictStr, conlist, validator


class AccountAction(BaseModel):
    """
    Object for specifying Actions to be performed on a specified list of sources' account.  # noqa: E501
    """
    action: Optional[StrictStr] = Field(
        None, description="Describes if action will be enabled or disabled")
    source_ids: Optional[conlist(StrictStr, unique_items=True)] = Field(
        None,
        alias="sourceIds",
        description=
        "List of unique source IDs. The sources must have the ENABLE feature or flat file source. See \"/sources\" endpoint for source features."
    )
    __properties = ["action", "sourceIds"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ENABLE', 'DISABLE'):
            raise ValueError(
                "must be one of enum values ('ENABLE', 'DISABLE')")
        return value

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
    def from_json(cls, json_str: str) -> AccountAction:
        """Create an instance of AccountAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountAction:
        """Create an instance of AccountAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountAction.parse_obj(obj)

        _obj = AccountAction.parse_obj({
            "action": obj.get("action"),
            "source_ids": obj.get("sourceIds")
        })
        return _obj
