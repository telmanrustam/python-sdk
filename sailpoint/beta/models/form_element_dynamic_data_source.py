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
from pydantic import BaseModel, Field, StrictStr, validator
from beta.models.form_element_dynamic_data_source_config import FormElementDynamicDataSourceConfig


class FormElementDynamicDataSource(BaseModel):
    """
    FormElementDynamicDataSource
    """
    config: Optional[FormElementDynamicDataSourceConfig] = None
    data_source_type: Optional[StrictStr] = Field(
        None,
        alias="dataSourceType",
        description=
        "DataSourceType is a FormElementDataSourceType value STATIC FormElementDataSourceTypeStatic INTERNAL FormElementDataSourceTypeInternal SEARCH FormElementDataSourceTypeSearch"
    )
    __properties = ["config", "dataSourceType"]

    @validator('data_source_type')
    def data_source_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('STATIC', 'INTERNAL', 'SEARCH'):
            raise ValueError(
                "must be one of enum values ('STATIC', 'INTERNAL', 'SEARCH')")
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
    def from_json(cls, json_str: str) -> FormElementDynamicDataSource:
        """Create an instance of FormElementDynamicDataSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FormElementDynamicDataSource:
        """Create an instance of FormElementDynamicDataSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FormElementDynamicDataSource.parse_obj(obj)

        _obj = FormElementDynamicDataSource.parse_obj({
            "config":
            FormElementDynamicDataSourceConfig.from_dict(obj.get("config"))
            if obj.get("config") is not None else None,
            "data_source_type":
            obj.get("dataSourceType")
        })
        return _obj
