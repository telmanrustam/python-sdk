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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class MailFromAttributes(BaseModel):
    """
    MAIL FROM attributes for a domain / identity
    """

  # noqa: E501
    identity: Optional[StrictStr] = Field(default=None,
                                          description="The email identity")
    mail_from_domain: Optional[StrictStr] = Field(
        default=None,
        description=
        "The name of a domain that an email identity uses as a custom MAIL FROM domain",
        alias="mailFromDomain")
    mx_record: Optional[StrictStr] = Field(
        default=None,
        description=
        "MX record that is required in customer's DNS to allow the domain to receive bounce and complaint notifications that email providers send you",
        alias="mxRecord")
    txt_record: Optional[StrictStr] = Field(
        default=None,
        description=
        "TXT record that is required in customer's DNS in order to prove that Amazon SES is authorized to send email from your domain",
        alias="txtRecord")
    mail_from_domain_status: Optional[StrictStr] = Field(
        default=None,
        description="The current status of the MAIL FROM verification",
        alias="mailFromDomainStatus")
    __properties: ClassVar[List[str]] = [
        "identity", "mailFromDomain", "mxRecord", "txtRecord",
        "mailFromDomainStatus"
    ]

    @field_validator('mail_from_domain_status')
    def mail_from_domain_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PENDING', 'SUCCESS', 'FAILED'):
            raise ValueError(
                "must be one of enum values ('PENDING', 'SUCCESS', 'FAILED')")
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
        """Create an instance of MailFromAttributes from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MailFromAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identity":
            obj.get("identity"),
            "mailFromDomain":
            obj.get("mailFromDomain"),
            "mxRecord":
            obj.get("mxRecord"),
            "txtRecord":
            obj.get("txtRecord"),
            "mailFromDomainStatus":
            obj.get("mailFromDomainStatus")
        })
        return _obj
