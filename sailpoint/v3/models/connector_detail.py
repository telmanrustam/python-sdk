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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConnectorDetail(BaseModel):
    """
    ConnectorDetail
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The connector name")
    type: Optional[StrictStr] = Field(default=None, description="The connector type")
    class_name: Optional[StrictStr] = Field(default=None, description="The connector class name", alias="className")
    script_name: Optional[StrictStr] = Field(default=None, description="The connector script name", alias="scriptName")
    application_xml: Optional[StrictStr] = Field(default=None, description="The connector application xml", alias="applicationXml")
    correlation_config_xml: Optional[StrictStr] = Field(default=None, description="The connector correlation config xml", alias="correlationConfigXml")
    source_config_xml: Optional[StrictStr] = Field(default=None, description="The connector source config xml", alias="sourceConfigXml")
    source_config: Optional[StrictStr] = Field(default=None, description="The connector source config", alias="sourceConfig")
    source_config_from: Optional[StrictStr] = Field(default=None, description="The connector source config origin", alias="sourceConfigFrom")
    s3_location: Optional[StrictStr] = Field(default=None, description="storage path key for this connector", alias="s3Location")
    uploaded_files: Optional[List[StrictStr]] = Field(default=None, description="The list of uploaded files supported by the connector. If there was any executable files uploaded to thee connector. Typically this be empty as the executable be uploaded at source creation.", alias="uploadedFiles")
    file_upload: Optional[StrictBool] = Field(default=False, description="true if the source is file upload", alias="fileUpload")
    direct_connect: Optional[StrictBool] = Field(default=False, description="true if the source is a direct connect source", alias="directConnect")
    translation_properties: Optional[Dict[str, Any]] = Field(default=None, description="A map containing translation attributes by loacale key", alias="translationProperties")
    connector_metadata: Optional[Dict[str, Any]] = Field(default=None, description="A map containing metadata pertinent to the UI to be used", alias="connectorMetadata")
    status: Optional[StrictStr] = Field(default=None, description="The connector status")
    __properties: ClassVar[List[str]] = ["name", "type", "className", "scriptName", "applicationXml", "correlationConfigXml", "sourceConfigXml", "sourceConfig", "sourceConfigFrom", "s3Location", "uploadedFiles", "fileUpload", "directConnect", "translationProperties", "connectorMetadata", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DEPRECATED', 'DEVELOPMENT', 'DEMO', 'RELEASED'):
            raise ValueError("must be one of enum values ('DEPRECATED', 'DEVELOPMENT', 'DEMO', 'RELEASED')")
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
        """Create an instance of ConnectorDetail from a JSON string"""
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
            exclude={
            },
            exclude_none=True,
        )
        # set to None if uploaded_files (nullable) is None
        # and model_fields_set contains the field
        if self.uploaded_files is None and "uploaded_files" in self.model_fields_set:
            _dict['uploadedFiles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConnectorDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "className": obj.get("className"),
            "scriptName": obj.get("scriptName"),
            "applicationXml": obj.get("applicationXml"),
            "correlationConfigXml": obj.get("correlationConfigXml"),
            "sourceConfigXml": obj.get("sourceConfigXml"),
            "sourceConfig": obj.get("sourceConfig"),
            "sourceConfigFrom": obj.get("sourceConfigFrom"),
            "s3Location": obj.get("s3Location"),
            "uploadedFiles": obj.get("uploadedFiles"),
            "fileUpload": obj.get("fileUpload") if obj.get("fileUpload") is not None else False,
            "directConnect": obj.get("directConnect") if obj.get("directConnect") is not None else False,
            "translationProperties": obj.get("translationProperties"),
            "connectorMetadata": obj.get("connectorMetadata"),
            "status": obj.get("status")
        })
        return _obj

