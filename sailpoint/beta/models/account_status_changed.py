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

from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from beta.models.account_status_changed_account import AccountStatusChangedAccount
from beta.models.account_status_changed_status_change import AccountStatusChangedStatusChange


class AccountStatusChanged(BaseModel):
    """
    AccountStatusChanged
    """
    event_type: Optional[StrictStr] = Field(None,
                                            alias="eventType",
                                            description="the event type")
    identity_id: Optional[StrictStr] = Field(None,
                                             alias="identityId",
                                             description="the identity id")
    dt: Optional[StrictStr] = Field(None, description="the date of event")
    account: Optional[AccountStatusChangedAccount] = None
    status_change: Optional[AccountStatusChangedStatusChange] = Field(
        None, alias="statusChange")
    __properties = ["eventType", "identityId", "dt", "account", "statusChange"]

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
    def from_json(cls, json_str: str) -> AccountStatusChanged:
        """Create an instance of AccountStatusChanged from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_change
        if self.status_change:
            _dict['statusChange'] = self.status_change.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountStatusChanged:
        """Create an instance of AccountStatusChanged from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountStatusChanged.parse_obj(obj)

        _obj = AccountStatusChanged.parse_obj({
            "event_type":
            obj.get("eventType"),
            "identity_id":
            obj.get("identityId"),
            "dt":
            obj.get("dt"),
            "account":
            AccountStatusChangedAccount.from_dict(obj.get("account"))
            if obj.get("account") is not None else None,
            "status_change":
            AccountStatusChangedStatusChange.from_dict(obj.get("statusChange"))
            if obj.get("statusChange") is not None else None
        })
        return _obj
