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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
from sailpoint.v3.models.approval_reminder_and_escalation_config import ApprovalReminderAndEscalationConfig
from sailpoint.v3.models.entitlement_request_config import EntitlementRequestConfig
from sailpoint.v3.models.request_on_behalf_of_config import RequestOnBehalfOfConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccessRequestConfig(BaseModel):
    """
    AccessRequestConfig
    """

  # noqa: E501
    approvals_must_be_external: Optional[StrictBool] = Field(
        default=None,
        description=
        "If true, then approvals must be processed by external system.",
        alias="approvalsMustBeExternal")
    auto_approval_enabled: Optional[StrictBool] = Field(
        default=None,
        description=
        "If true and requester and reviewer are the same, then automatically approve the approval.",
        alias="autoApprovalEnabled")
    request_on_behalf_of_config: Optional[RequestOnBehalfOfConfig] = Field(
        default=None, alias="requestOnBehalfOfConfig")
    approval_reminder_and_escalation_config: Optional[
        ApprovalReminderAndEscalationConfig] = Field(
            default=None, alias="approvalReminderAndEscalationConfig")
    entitlement_request_config: Optional[EntitlementRequestConfig] = Field(
        default=None, alias="entitlementRequestConfig")
    __properties: ClassVar[List[str]] = [
        "approvalsMustBeExternal", "autoApprovalEnabled",
        "requestOnBehalfOfConfig", "approvalReminderAndEscalationConfig",
        "entitlementRequestConfig"
    ]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AccessRequestConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of request_on_behalf_of_config
        if self.request_on_behalf_of_config:
            _dict[
                'requestOnBehalfOfConfig'] = self.request_on_behalf_of_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of approval_reminder_and_escalation_config
        if self.approval_reminder_and_escalation_config:
            _dict[
                'approvalReminderAndEscalationConfig'] = self.approval_reminder_and_escalation_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of entitlement_request_config
        if self.entitlement_request_config:
            _dict[
                'entitlementRequestConfig'] = self.entitlement_request_config.to_dict(
                )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccessRequestConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approvalsMustBeExternal":
            obj.get("approvalsMustBeExternal"),
            "autoApprovalEnabled":
            obj.get("autoApprovalEnabled"),
            "requestOnBehalfOfConfig":
            RequestOnBehalfOfConfig.from_dict(
                obj.get("requestOnBehalfOfConfig"))
            if obj.get("requestOnBehalfOfConfig") is not None else None,
            "approvalReminderAndEscalationConfig":
            ApprovalReminderAndEscalationConfig.from_dict(
                obj.get("approvalReminderAndEscalationConfig"))
            if obj.get("approvalReminderAndEscalationConfig") is not None else
            None,
            "entitlementRequestConfig":
            EntitlementRequestConfig.from_dict(
                obj.get("entitlementRequestConfig"))
            if obj.get("entitlementRequestConfig") is not None else None
        })
        return _obj
