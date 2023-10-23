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
from beta.models.basic_auth_config import BasicAuthConfig
from beta.models.bearer_token_auth_config import BearerTokenAuthConfig
from beta.models.http_authentication_type import HttpAuthenticationType
from beta.models.http_dispatch_mode import HttpDispatchMode


class HttpConfig(BaseModel):
    """
    HttpConfig
    """
    url: StrictStr = Field(
        ..., description="URL of the external/custom integration.")
    http_dispatch_mode: HttpDispatchMode = Field(..., alias="httpDispatchMode")
    http_authentication_type: Optional[HttpAuthenticationType] = Field(
        None, alias="httpAuthenticationType")
    basic_auth_config: Optional[BasicAuthConfig] = Field(
        None, alias="basicAuthConfig")
    bearer_token_auth_config: Optional[BearerTokenAuthConfig] = Field(
        None, alias="bearerTokenAuthConfig")
    __properties = [
        "url", "httpDispatchMode", "httpAuthenticationType", "basicAuthConfig",
        "bearerTokenAuthConfig"
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
    def from_json(cls, json_str: str) -> HttpConfig:
        """Create an instance of HttpConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of basic_auth_config
        if self.basic_auth_config:
            _dict['basicAuthConfig'] = self.basic_auth_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bearer_token_auth_config
        if self.bearer_token_auth_config:
            _dict[
                'bearerTokenAuthConfig'] = self.bearer_token_auth_config.to_dict(
                )
        # set to None if basic_auth_config (nullable) is None
        # and __fields_set__ contains the field
        if self.basic_auth_config is None and "basic_auth_config" in self.__fields_set__:
            _dict['basicAuthConfig'] = None

        # set to None if bearer_token_auth_config (nullable) is None
        # and __fields_set__ contains the field
        if self.bearer_token_auth_config is None and "bearer_token_auth_config" in self.__fields_set__:
            _dict['bearerTokenAuthConfig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HttpConfig:
        """Create an instance of HttpConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HttpConfig.parse_obj(obj)

        _obj = HttpConfig.parse_obj({
            "url":
            obj.get("url"),
            "http_dispatch_mode":
            obj.get("httpDispatchMode"),
            "http_authentication_type":
            obj.get("httpAuthenticationType"),
            "basic_auth_config":
            BasicAuthConfig.from_dict(obj.get("basicAuthConfig"))
            if obj.get("basicAuthConfig") is not None else None,
            "bearer_token_auth_config":
            BearerTokenAuthConfig.from_dict(obj.get("bearerTokenAuthConfig"))
            if obj.get("bearerTokenAuthConfig") is not None else None
        })
        return _obj
