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

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from sailpoint.beta.models.import_object import ImportObject
from sailpoint.beta.models.sp_config_message import SpConfigMessage
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ObjectImportResult(BaseModel):
    """
    Response model for import of a single object.
    """

  # noqa: E501
    infos: List[SpConfigMessage] = Field(
        description=
        "Informational messages returned from the target service on import.")
    warnings: List[SpConfigMessage] = Field(
        description=
        "Warning messages returned from the target service on import.")
    errors: List[SpConfigMessage] = Field(
        description="Error messages returned from the target service on import."
    )
    imported_objects: List[ImportObject] = Field(
        description=
        "References to objects that were created or updated by the import.",
        alias="importedObjects")
    __properties: ClassVar[List[str]] = [
        "infos", "warnings", "errors", "importedObjects"
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
        """Create an instance of ObjectImportResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in infos (list)
        _items = []
        if self.infos:
            for _item in self.infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['infos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in imported_objects (list)
        _items = []
        if self.imported_objects:
            for _item in self.imported_objects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['importedObjects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ObjectImportResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "infos":
            [SpConfigMessage.from_dict(_item) for _item in obj.get("infos")]
            if obj.get("infos") is not None else None,
            "warnings": [
                SpConfigMessage.from_dict(_item)
                for _item in obj.get("warnings")
            ] if obj.get("warnings") is not None else None,
            "errors":
            [SpConfigMessage.from_dict(_item) for _item in obj.get("errors")]
            if obj.get("errors") is not None else None,
            "importedObjects": [
                ImportObject.from_dict(_item)
                for _item in obj.get("importedObjects")
            ] if obj.get("importedObjects") is not None else None
        })
        return _obj
