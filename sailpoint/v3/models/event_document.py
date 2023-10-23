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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from v3.models.document_type import DocumentType
from v3.models.name_type import NameType


class EventDocument(BaseModel):
    """
    Event  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    type: DocumentType = Field(..., alias="_type")
    created: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    synced: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    action: Optional[StrictStr] = Field(
        None, description="The action that was performed")
    type: Optional[StrictStr] = Field(None, description="The type of event")
    actor: Optional[NameType] = None
    target: Optional[NameType] = None
    stack: Optional[StrictStr] = None
    tracking_number: Optional[StrictStr] = Field(None, alias="trackingNumber")
    ip_address: Optional[StrictStr] = Field(None, alias="ipAddress")
    details: Optional[StrictStr] = None
    attributes: Optional[Dict[str, Any]] = None
    objects: Optional[conlist(StrictStr)] = None
    operation: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    technical_name: Optional[StrictStr] = Field(None, alias="technicalName")
    __properties = [
        "id", "name", "_type", "created", "synced", "action", "type", "actor",
        "target", "stack", "trackingNumber", "ipAddress", "details",
        "attributes", "objects", "operation", "status", "technicalName"
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
    def from_json(cls, json_str: str) -> EventDocument:
        """Create an instance of EventDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        # set to None if synced (nullable) is None
        # and __fields_set__ contains the field
        if self.synced is None and "synced" in self.__fields_set__:
            _dict['synced'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventDocument:
        """Create an instance of EventDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventDocument.parse_obj(obj)

        _obj = EventDocument.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "type":
            obj.get("_type"),
            "created":
            obj.get("created"),
            "synced":
            obj.get("synced"),
            "action":
            obj.get("action"),
            "type":
            obj.get("type"),
            "actor":
            NameType.from_dict(obj.get("actor"))
            if obj.get("actor") is not None else None,
            "target":
            NameType.from_dict(obj.get("target"))
            if obj.get("target") is not None else None,
            "stack":
            obj.get("stack"),
            "tracking_number":
            obj.get("trackingNumber"),
            "ip_address":
            obj.get("ipAddress"),
            "details":
            obj.get("details"),
            "attributes":
            obj.get("attributes"),
            "objects":
            obj.get("objects"),
            "operation":
            obj.get("operation"),
            "status":
            obj.get("status"),
            "technical_name":
            obj.get("technicalName")
        })
        return _obj
