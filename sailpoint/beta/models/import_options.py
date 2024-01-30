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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.object_export_import_options import ObjectExportImportOptions
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ImportOptions(BaseModel):
    """
    ImportOptions
    """

  # noqa: E501
    exclude_types: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "Object type names to be excluded from an sp-config export command.",
        alias="excludeTypes")
    include_types: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "Object type names to be included in an sp-config export command. IncludeTypes takes precedence over excludeTypes.",
        alias="includeTypes")
    object_options: Optional[Dict[str, ObjectExportImportOptions]] = Field(
        default=None,
        description=
        "Additional options targeting specific objects related to each item in the includeTypes field",
        alias="objectOptions")
    default_references: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "List of object types that can be used to resolve references on import.",
        alias="defaultReferences")
    exclude_backup: Optional[StrictBool] = Field(
        default=False,
        description=
        "By default, every import will first export all existing objects supported by sp-config as a backup before the import is attempted. If excludeBackup is true, the backup will not be performed.",
        alias="excludeBackup")
    __properties: ClassVar[List[str]] = [
        "excludeTypes", "includeTypes", "objectOptions", "defaultReferences",
        "excludeBackup"
    ]

    @field_validator('exclude_types')
    def exclude_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'RULE',
                         'SOURCE', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION'):
                raise ValueError(
                    "each list item must be one of ('IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'RULE', 'SOURCE', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION')"
                )
        return value

    @field_validator('include_types')
    def include_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'RULE',
                         'SOURCE', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION'):
                raise ValueError(
                    "each list item must be one of ('IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'RULE', 'SOURCE', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION')"
                )
        return value

    @field_validator('default_references')
    def default_references_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'RULE',
                         'SOURCE', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION'):
                raise ValueError(
                    "each list item must be one of ('IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'RULE', 'SOURCE', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION')"
                )
        return value

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
        """Create an instance of ImportOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in object_options (dict)
        _field_dict = {}
        if self.object_options:
            for _key in self.object_options:
                if self.object_options[_key]:
                    _field_dict[_key] = self.object_options[_key].to_dict()
            _dict['objectOptions'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ImportOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeTypes":
            obj.get("excludeTypes"),
            "includeTypes":
            obj.get("includeTypes"),
            "objectOptions":
            dict((_k, ObjectExportImportOptions.from_dict(_v))
                 for _k, _v in obj.get("objectOptions").items())
            if obj.get("objectOptions") is not None else None,
            "defaultReferences":
            obj.get("defaultReferences"),
            "excludeBackup":
            obj.get("excludeBackup")
            if obj.get("excludeBackup") is not None else False
        })
        return _obj
