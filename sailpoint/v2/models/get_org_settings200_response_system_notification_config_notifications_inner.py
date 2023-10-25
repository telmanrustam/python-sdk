# coding: utf-8

"""
    SailPoint SaaS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from v2.models.get_org_settings200_response_system_notification_config_notifications_inner_thresholds import GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds


class GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner(
        BaseModel):
    """
    GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner
    """
    type: Optional[StrictStr] = None
    by_email: Optional[StrictBool] = Field(None, alias="byEmail")
    thresholds: Optional[
        GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds] = None
    __properties = ["type", "byEmail", "thresholds"]

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
    ) -> GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner:
        """Create an instance of GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of thresholds
        if self.thresholds:
            _dict['thresholds'] = self.thresholds.to_dict()
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner:
        """Create an instance of GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner.parse_obj(
                obj)

        _obj = GetOrgSettings200ResponseSystemNotificationConfigNotificationsInner.parse_obj(
            {
                "type":
                obj.get("type"),
                "by_email":
                obj.get("byEmail"),
                "thresholds":
                GetOrgSettings200ResponseSystemNotificationConfigNotificationsInnerThresholds
                .from_dict(obj.get("thresholds"))
                if obj.get("thresholds") is not None else None
            })
        return _obj
