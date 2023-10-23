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
from pydantic import BaseModel, Field, StrictStr, validator
from beta.models.access_request_post_approval_requested_items_status_inner_approval_info_inner_approver import AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover


class AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner(
        BaseModel):
    """
    AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner
    """
    approval_comment: Optional[StrictStr] = Field(
        None,
        alias="approvalComment",
        description="A comment left by the approver.")
    approval_decision: Dict[str, Any] = Field(
        ...,
        alias="approvalDecision",
        description="The final decision of the approver.")
    approver_name: StrictStr = Field(...,
                                     alias="approverName",
                                     description="The name of the approver")
    approver: AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover = Field(
        ...)
    __properties = [
        "approvalComment", "approvalDecision", "approverName", "approver"
    ]

    @validator('approval_decision')
    def approval_decision_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('APPROVED', 'DENIED'):
            raise ValueError(
                "must be one of enum values ('APPROVED', 'DENIED')")
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
    def from_json(
        cls, json_str: str
    ) -> AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner:
        """Create an instance of AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of approver
        if self.approver:
            _dict['approver'] = self.approver.to_dict()
        # set to None if approval_comment (nullable) is None
        # and __fields_set__ contains the field
        if self.approval_comment is None and "approval_comment" in self.__fields_set__:
            _dict['approvalComment'] = None

        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner:
        """Create an instance of AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner.parse_obj(
                obj)

        _obj = AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInner.parse_obj(
            {
                "approval_comment":
                obj.get("approvalComment"),
                "approval_decision":
                obj.get("approvalDecision"),
                "approver_name":
                obj.get("approverName"),
                "approver":
                AccessRequestPostApprovalRequestedItemsStatusInnerApprovalInfoInnerApprover
                .from_dict(obj.get("approver"))
                if obj.get("approver") is not None else None
            })
        return _obj
