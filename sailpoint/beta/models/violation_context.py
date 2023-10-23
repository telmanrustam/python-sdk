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
from pydantic import BaseModel, Field
from beta.models.exception_access_criteria import ExceptionAccessCriteria
from beta.models.violation_context_policy import ViolationContextPolicy


class ViolationContext(BaseModel):
    """
    ViolationContext
    """
    policy: Optional[ViolationContextPolicy] = None
    conflicting_access_criteria: Optional[ExceptionAccessCriteria] = Field(
        None, alias="conflictingAccessCriteria")
    __properties = ["policy", "conflictingAccessCriteria"]

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
    def from_json(cls, json_str: str) -> ViolationContext:
        """Create an instance of ViolationContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conflicting_access_criteria
        if self.conflicting_access_criteria:
            _dict[
                'conflictingAccessCriteria'] = self.conflicting_access_criteria.to_dict(
                )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ViolationContext:
        """Create an instance of ViolationContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ViolationContext.parse_obj(obj)

        _obj = ViolationContext.parse_obj({
            "policy":
            ViolationContextPolicy.from_dict(obj.get("policy"))
            if obj.get("policy") is not None else None,
            "conflicting_access_criteria":
            ExceptionAccessCriteria.from_dict(
                obj.get("conflictingAccessCriteria"))
            if obj.get("conflictingAccessCriteria") is not None else None
        })
        return _obj
