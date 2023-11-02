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
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from v3.models.owner_dto import OwnerDto

class CancelledRequestDetails(BaseModel):
    """
    Provides additional details for a request that has been cancelled.  # noqa: E501
    """
    comment: Optional[StrictStr] = Field(None, description="Comment made by the owner when cancelling the associated request.")
    owner: Optional[OwnerDto] = None
    modified: Optional[datetime] = Field(None, description="Date comment was added by the owner when cancelling the associated request.")
    __properties = ["comment", "owner", "modified"]

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
    def from_json(cls, json_str: str) -> CancelledRequestDetails:
        """Create an instance of CancelledRequestDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CancelledRequestDetails:
        """Create an instance of CancelledRequestDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CancelledRequestDetails.parse_obj(obj)

        _obj = CancelledRequestDetails.parse_obj({
            "comment": obj.get("comment"),
            "owner": OwnerDto.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "modified": obj.get("modified")
        })
        return _obj


