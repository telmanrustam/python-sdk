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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from beta.models.approval_scheme import ApprovalScheme
from beta.models.base_reference_dto1 import BaseReferenceDto1
from beta.models.error_message_dto import ErrorMessageDto
from beta.models.manual_work_item_state import ManualWorkItemState


class ApprovalStatusDto(BaseModel):
    """
    ApprovalStatusDto
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
    reviewed_by: Optional[BaseReferenceDto1] = Field(None, alias="reviewedBy")
    modified: Optional[datetime] = Field(
        None, description="Time at which item was modified.")
    status: Optional[ManualWorkItemState] = None
    scheme: Optional[ApprovalScheme] = None
    error_messages: Optional[conlist(ErrorMessageDto)] = Field(
        None,
        alias="errorMessages",
        description=
        "If the request failed, includes any error messages that were generated."
    )
    comment: Optional[StrictStr] = Field(
        None, description="Comment, if any, provided by the approver.")
    remove_date: Optional[datetime] = Field(
        None,
        alias="removeDate",
        description=
        "The date the role or access profile is no longer assigned to the specified identity."
    )
    __properties = [
        "forwarded", "originalOwner", "currentOwner", "reviewedBy", "modified",
        "status", "scheme", "errorMessages", "comment", "removeDate"
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
    def from_json(cls, json_str: str) -> ApprovalStatusDto:
        """Create an instance of ApprovalStatusDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reviewed_by
        if self.reviewed_by:
            _dict['reviewedBy'] = self.reviewed_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in error_messages (list)
        _items = []
        if self.error_messages:
            for _item in self.error_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errorMessages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApprovalStatusDto:
        """Create an instance of ApprovalStatusDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApprovalStatusDto.parse_obj(obj)

        _obj = ApprovalStatusDto.parse_obj({
            "forwarded":
            obj.get("forwarded"),
            "original_owner":
            BaseReferenceDto1.from_dict(obj.get("originalOwner"))
            if obj.get("originalOwner") is not None else None,
            "current_owner":
            BaseReferenceDto1.from_dict(obj.get("currentOwner"))
            if obj.get("currentOwner") is not None else None,
            "reviewed_by":
            BaseReferenceDto1.from_dict(obj.get("reviewedBy"))
            if obj.get("reviewedBy") is not None else None,
            "modified":
            obj.get("modified"),
            "status":
            obj.get("status"),
            "scheme":
            obj.get("scheme"),
            "error_messages": [
                ErrorMessageDto.from_dict(_item)
                for _item in obj.get("errorMessages")
            ] if obj.get("errorMessages") is not None else None,
            "comment":
            obj.get("comment"),
            "remove_date":
            obj.get("removeDate")
        })
        return _obj
