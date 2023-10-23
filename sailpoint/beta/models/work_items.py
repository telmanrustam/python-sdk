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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from beta.models.approval_item_details import ApprovalItemDetails
from beta.models.remediation_item_details import RemediationItemDetails
from beta.models.work_item_state import WorkItemState
from beta.models.work_item_type import WorkItemType


class WorkItems(BaseModel):
    """
    WorkItems
    """
    id: Optional[StrictStr] = Field(None, description="ID of the work item")
    requester_id: Optional[StrictStr] = Field(
        None, alias="requesterId", description="ID of the requester")
    requester_display_name: Optional[StrictStr] = Field(
        None,
        alias="requesterDisplayName",
        description="The displayname of the requester")
    owner_id: Optional[StrictStr] = Field(None,
                                          alias="ownerId",
                                          description="The ID of the owner")
    owner_name: Optional[StrictStr] = Field(
        None, alias="ownerName", description="The name of the owner")
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
    description: Optional[StrictStr] = Field(
        None, description="The description of the work item")
    state: Optional[WorkItemState] = None
    type: Optional[WorkItemType] = None
    remediation_items: Optional[RemediationItemDetails] = Field(
        None, alias="remediationItems")
    approval_items: Optional[ApprovalItemDetails] = Field(
        None, alias="approvalItems")
    name: Optional[StrictStr] = Field(None, description="The work item name")
    completed: Optional[datetime] = None
    num_items: Optional[StrictInt] = Field(
        None,
        alias="numItems",
        description="The number of items in the work item")
    errors: Optional[conlist(StrictStr)] = None
    __properties = [
        "id", "requesterId", "requesterDisplayName", "ownerId", "ownerName",
        "created", "modified", "description", "state", "type",
        "remediationItems", "approvalItems", "name", "completed", "numItems",
        "errors"
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
    def from_json(cls, json_str: str) -> WorkItems:
        """Create an instance of WorkItems from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of remediation_items
        if self.remediation_items:
            _dict['remediationItems'] = self.remediation_items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of approval_items
        if self.approval_items:
            _dict['approvalItems'] = self.approval_items.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkItems:
        """Create an instance of WorkItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkItems.parse_obj(obj)

        _obj = WorkItems.parse_obj({
            "id":
            obj.get("id"),
            "requester_id":
            obj.get("requesterId"),
            "requester_display_name":
            obj.get("requesterDisplayName"),
            "owner_id":
            obj.get("ownerId"),
            "owner_name":
            obj.get("ownerName"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "description":
            obj.get("description"),
            "state":
            obj.get("state"),
            "type":
            obj.get("type"),
            "remediation_items":
            RemediationItemDetails.from_dict(obj.get("remediationItems"))
            if obj.get("remediationItems") is not None else None,
            "approval_items":
            ApprovalItemDetails.from_dict(obj.get("approvalItems"))
            if obj.get("approvalItems") is not None else None,
            "name":
            obj.get("name"),
            "completed":
            obj.get("completed"),
            "num_items":
            obj.get("numItems"),
            "errors":
            obj.get("errors")
        })
        return _obj
