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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from v3.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail
from v3.models.requestable_object_request_status import RequestableObjectRequestStatus
from v3.models.requestable_object_type import RequestableObjectType


class RequestableObject(BaseModel):
    """
    RequestableObject
    """
    id: Optional[StrictStr] = Field(
        None, description="Id of the requestable object itself")
    name: Optional[StrictStr] = Field(
        None,
        description="Human-readable display name of the requestable object")
    created: Optional[datetime] = Field(
        None, description="The time when the requestable object was created")
    modified: Optional[datetime] = Field(
        None,
        description="The time when the requestable object was last modified")
    description: Optional[StrictStr] = Field(
        None, description="Description of the requestable object.")
    type: Optional[RequestableObjectType] = None
    request_status: Optional[RequestableObjectRequestStatus] = Field(
        None, alias="requestStatus")
    identity_request_id: Optional[StrictStr] = Field(
        None,
        alias="identityRequestId",
        description=
        "If *requestStatus* is *PENDING*, indicates the id of the associated account activity."
    )
    owner_ref: Optional[IdentityReferenceWithNameAndEmail] = Field(
        None, alias="ownerRef")
    request_comments_required: Optional[StrictBool] = Field(
        None,
        alias="requestCommentsRequired",
        description=
        "Whether the requester must provide comments when requesting the object."
    )
    __properties = [
        "id", "name", "created", "modified", "description", "type",
        "requestStatus", "identityRequestId", "ownerRef",
        "requestCommentsRequired"
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
    def from_json(cls, json_str: str) -> RequestableObject:
        """Create an instance of RequestableObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner_ref
        if self.owner_ref:
            _dict['ownerRef'] = self.owner_ref.to_dict()
        # set to None if modified (nullable) is None
        # and __fields_set__ contains the field
        if self.modified is None and "modified" in self.__fields_set__:
            _dict['modified'] = None

        # set to None if identity_request_id (nullable) is None
        # and __fields_set__ contains the field
        if self.identity_request_id is None and "identity_request_id" in self.__fields_set__:
            _dict['identityRequestId'] = None

        # set to None if owner_ref (nullable) is None
        # and __fields_set__ contains the field
        if self.owner_ref is None and "owner_ref" in self.__fields_set__:
            _dict['ownerRef'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestableObject:
        """Create an instance of RequestableObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestableObject.parse_obj(obj)

        _obj = RequestableObject.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "description":
            obj.get("description"),
            "type":
            obj.get("type"),
            "request_status":
            obj.get("requestStatus"),
            "identity_request_id":
            obj.get("identityRequestId"),
            "owner_ref":
            IdentityReferenceWithNameAndEmail.from_dict(obj.get("ownerRef"))
            if obj.get("ownerRef") is not None else None,
            "request_comments_required":
            obj.get("requestCommentsRequired")
        })
        return _obj
