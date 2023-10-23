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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from beta.models.approval_forward_history import ApprovalForwardHistory
from beta.models.base_reference_dto1 import BaseReferenceDto1
from beta.models.manual_work_item_state import ManualWorkItemState


class ManualWorkItemDetails(BaseModel):
    """
    ManualWorkItemDetails
    """
    forwarded: Optional[StrictBool] = Field(
        None,
        description=
        "True if the request for this item was forwarded from one owner to another."
    )
    original_owner: Optional[BaseReferenceDto1] = Field(None,
                                                        alias="originalOwner")
    current_owner: Optional[BaseReferenceDto1] = Field(None,
                                                       alias="currentOwner")
    modified: Optional[datetime] = Field(
        None, description="Time at which item was modified.")
    status: Optional[ManualWorkItemState] = None
    forward_history: Optional[conlist(ApprovalForwardHistory)] = Field(
        None,
        alias="forwardHistory",
        description="The history of approval forward action.")
    __properties = [
        "forwarded", "originalOwner", "currentOwner", "modified", "status",
        "forwardHistory"
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
    def from_json(cls, json_str: str) -> ManualWorkItemDetails:
        """Create an instance of ManualWorkItemDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of original_owner
        if self.original_owner:
            _dict['originalOwner'] = self.original_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_owner
        if self.current_owner:
            _dict['currentOwner'] = self.current_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in forward_history (list)
        _items = []
        if self.forward_history:
            for _item in self.forward_history:
                if _item:
                    _items.append(_item.to_dict())
            _dict['forwardHistory'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManualWorkItemDetails:
        """Create an instance of ManualWorkItemDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ManualWorkItemDetails.parse_obj(obj)

        _obj = ManualWorkItemDetails.parse_obj({
            "forwarded":
            obj.get("forwarded"),
            "original_owner":
            BaseReferenceDto1.from_dict(obj.get("originalOwner"))
            if obj.get("originalOwner") is not None else None,
            "current_owner":
            BaseReferenceDto1.from_dict(obj.get("currentOwner"))
            if obj.get("currentOwner") is not None else None,
            "modified":
            obj.get("modified"),
            "status":
            obj.get("status"),
            "forward_history": [
                ApprovalForwardHistory.from_dict(_item)
                for _item in obj.get("forwardHistory")
            ] if obj.get("forwardHistory") is not None else None
        })
        return _obj
