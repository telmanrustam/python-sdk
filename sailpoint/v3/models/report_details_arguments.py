# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from v3.models.accounts_export_report_arguments import AccountsExportReportArguments
from v3.models.identities_details_report_arguments import IdentitiesDetailsReportArguments
from v3.models.identities_report_arguments import IdentitiesReportArguments
from v3.models.identity_profile_identity_error_report_arguments import IdentityProfileIdentityErrorReportArguments
from v3.models.orphan_uncorrelated_report_arguments import OrphanUncorrelatedReportArguments
from v3.models.search_export_report_arguments import SearchExportReportArguments
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

REPORTDETAILSARGUMENTS_ONE_OF_SCHEMAS = ["AccountsExportReportArguments", "IdentitiesDetailsReportArguments", "IdentitiesReportArguments", "IdentityProfileIdentityErrorReportArguments", "OrphanUncorrelatedReportArguments", "SearchExportReportArguments"]

class ReportDetailsArguments(BaseModel):
    """
    The string-object map(dictionary) with the arguments needed for report processing.
    """
    # data type: AccountsExportReportArguments
    oneof_schema_1_validator: Optional[AccountsExportReportArguments] = None
    # data type: IdentitiesDetailsReportArguments
    oneof_schema_2_validator: Optional[IdentitiesDetailsReportArguments] = None
    # data type: IdentitiesReportArguments
    oneof_schema_3_validator: Optional[IdentitiesReportArguments] = None
    # data type: IdentityProfileIdentityErrorReportArguments
    oneof_schema_4_validator: Optional[IdentityProfileIdentityErrorReportArguments] = None
    # data type: OrphanUncorrelatedReportArguments
    oneof_schema_5_validator: Optional[OrphanUncorrelatedReportArguments] = None
    # data type: SearchExportReportArguments
    oneof_schema_6_validator: Optional[SearchExportReportArguments] = None
    if TYPE_CHECKING:
        actual_instance: Union[AccountsExportReportArguments, IdentitiesDetailsReportArguments, IdentitiesReportArguments, IdentityProfileIdentityErrorReportArguments, OrphanUncorrelatedReportArguments, SearchExportReportArguments]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(REPORTDETAILSARGUMENTS_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ReportDetailsArguments.construct()
        error_messages = []
        match = 0
        # validate data type: AccountsExportReportArguments
        if not isinstance(v, AccountsExportReportArguments):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountsExportReportArguments`")
        else:
            match += 1
        # validate data type: IdentitiesDetailsReportArguments
        if not isinstance(v, IdentitiesDetailsReportArguments):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentitiesDetailsReportArguments`")
        else:
            match += 1
        # validate data type: IdentitiesReportArguments
        if not isinstance(v, IdentitiesReportArguments):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentitiesReportArguments`")
        else:
            match += 1
        # validate data type: IdentityProfileIdentityErrorReportArguments
        if not isinstance(v, IdentityProfileIdentityErrorReportArguments):
            error_messages.append(f"Error! Input type `{type(v)}` is not `IdentityProfileIdentityErrorReportArguments`")
        else:
            match += 1
        # validate data type: OrphanUncorrelatedReportArguments
        if not isinstance(v, OrphanUncorrelatedReportArguments):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OrphanUncorrelatedReportArguments`")
        else:
            match += 1
        # validate data type: SearchExportReportArguments
        if not isinstance(v, SearchExportReportArguments):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchExportReportArguments`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ReportDetailsArguments with oneOf schemas: AccountsExportReportArguments, IdentitiesDetailsReportArguments, IdentitiesReportArguments, IdentityProfileIdentityErrorReportArguments, OrphanUncorrelatedReportArguments, SearchExportReportArguments. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ReportDetailsArguments with oneOf schemas: AccountsExportReportArguments, IdentitiesDetailsReportArguments, IdentitiesReportArguments, IdentityProfileIdentityErrorReportArguments, OrphanUncorrelatedReportArguments, SearchExportReportArguments. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ReportDetailsArguments:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ReportDetailsArguments:
        """Returns the object represented by the json string"""
        instance = ReportDetailsArguments.construct()
        error_messages = []
        match = 0

        # deserialize data into AccountsExportReportArguments
        try:
            instance.actual_instance = AccountsExportReportArguments.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentitiesDetailsReportArguments
        try:
            instance.actual_instance = IdentitiesDetailsReportArguments.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentitiesReportArguments
        try:
            instance.actual_instance = IdentitiesReportArguments.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into IdentityProfileIdentityErrorReportArguments
        try:
            instance.actual_instance = IdentityProfileIdentityErrorReportArguments.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OrphanUncorrelatedReportArguments
        try:
            instance.actual_instance = OrphanUncorrelatedReportArguments.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchExportReportArguments
        try:
            instance.actual_instance = SearchExportReportArguments.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ReportDetailsArguments with oneOf schemas: AccountsExportReportArguments, IdentitiesDetailsReportArguments, IdentitiesReportArguments, IdentityProfileIdentityErrorReportArguments, OrphanUncorrelatedReportArguments, SearchExportReportArguments. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ReportDetailsArguments with oneOf schemas: AccountsExportReportArguments, IdentitiesDetailsReportArguments, IdentitiesReportArguments, IdentityProfileIdentityErrorReportArguments, OrphanUncorrelatedReportArguments, SearchExportReportArguments. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

