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
from beta.models.schedule1 import Schedule1
from beta.models.sod_recipient import SodRecipient

class SodPolicySchedule(BaseModel):
    """
    SodPolicySchedule
    """
    name: Optional[StrictStr] = Field(None, description="SOD Policy schedule name")
    created: Optional[datetime] = Field(None, description="The time when this SOD policy schedule is created.")
    modified: Optional[datetime] = Field(None, description="The time when this SOD policy schedule is modified.")
    description: Optional[StrictStr] = Field(None, description="SOD Policy schedule description")
    schedule: Optional[Schedule1] = None
    recipients: Optional[conlist(SodRecipient)] = None
    email_empty_results: Optional[StrictBool] = Field(None, alias="emailEmptyResults", description="Indicates if empty results need to be emailed")
    creator_id: Optional[StrictStr] = Field(None, alias="creatorId", description="Policy's creator ID")
    modifier_id: Optional[StrictStr] = Field(None, alias="modifierId", description="Policy's modifier ID")
    __properties = ["name", "created", "modified", "description", "schedule", "recipients", "emailEmptyResults", "creatorId", "modifierId"]

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
    def from_json(cls, json_str: str) -> SodPolicySchedule:
        """Create an instance of SodPolicySchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SodPolicySchedule:
        """Create an instance of SodPolicySchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SodPolicySchedule.parse_obj(obj)

        _obj = SodPolicySchedule.parse_obj({
            "name": obj.get("name"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "description": obj.get("description"),
            "schedule": Schedule1.from_dict(obj.get("schedule")) if obj.get("schedule") is not None else None,
            "recipients": [SodRecipient.from_dict(_item) for _item in obj.get("recipients")] if obj.get("recipients") is not None else None,
            "email_empty_results": obj.get("emailEmptyResults"),
            "creator_id": obj.get("creatorId"),
            "modifier_id": obj.get("modifierId")
        })
        return _obj


