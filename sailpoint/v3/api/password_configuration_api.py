# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from v3.models.password_org_config import PasswordOrgConfig

from v3.api_client import ApiClient
from v3.api_response import ApiResponse
from v3.exceptions import (  # noqa: F401
    ApiTypeError, ApiValueError)


class PasswordConfigurationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_password_org_config(
            self, password_org_config: PasswordOrgConfig,
            **kwargs) -> PasswordOrgConfig:  # noqa: E501
        """Create Password Org Config  # noqa: E501

        This API creates the password org config. Unspecified fields will use default value. To be able to use the custom password instructions, you must set the `customInstructionsEnabled` field to \"true\". Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:write'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_password_org_config(password_org_config, async_req=True)
        >>> result = thread.get()

        :param password_org_config: (required)
        :type password_org_config: PasswordOrgConfig
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PasswordOrgConfig
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_password_org_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_password_org_config_with_http_info(
            password_org_config, **kwargs)  # noqa: E501

    @validate_arguments
    def create_password_org_config_with_http_info(
            self, password_org_config: PasswordOrgConfig,
            **kwargs) -> ApiResponse:  # noqa: E501
        """Create Password Org Config  # noqa: E501

        This API creates the password org config. Unspecified fields will use default value. To be able to use the custom password instructions, you must set the `customInstructionsEnabled` field to \"true\". Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:write'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_password_org_config_with_http_info(password_org_config, async_req=True)
        >>> result = thread.get()

        :param password_org_config: (required)
        :type password_org_config: PasswordOrgConfig
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PasswordOrgConfig, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['password_org_config']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method create_password_org_config" %
                                   _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['password_org_config'] is not None:
            _body_params = _params['password_org_config']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            '_content_type',
            self.api_client.select_header_content_type(['application/json']))
        if _content_types_list:
            _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "PasswordOrgConfig",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/password-org-config',
            'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_password_org_config(self,
                                **kwargs) -> PasswordOrgConfig:  # noqa: E501
        """Get Password Org Config  # noqa: E501

        This API returns the password org config . Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:read'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_password_org_config(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PasswordOrgConfig
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_password_org_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_password_org_config_with_http_info(
            **kwargs)  # noqa: E501

    @validate_arguments
    def get_password_org_config_with_http_info(
            self, **kwargs) -> ApiResponse:  # noqa: E501
        """Get Password Org Config  # noqa: E501

        This API returns the password org config . Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:read'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_password_org_config_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PasswordOrgConfig, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = []
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method get_password_org_config" % _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "PasswordOrgConfig",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/password-org-config',
            'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def put_password_org_config(self, password_org_config: PasswordOrgConfig,
                                **kwargs) -> PasswordOrgConfig:  # noqa: E501
        """Update Password Org Config  # noqa: E501

        This API updates the password org config for specified fields. Other fields will keep original value. You must set the `customInstructionsEnabled` field to \"true\" to be able to use custom password instructions.  Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:write'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_password_org_config(password_org_config, async_req=True)
        >>> result = thread.get()

        :param password_org_config: (required)
        :type password_org_config: PasswordOrgConfig
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PasswordOrgConfig
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the put_password_org_config_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.put_password_org_config_with_http_info(
            password_org_config, **kwargs)  # noqa: E501

    @validate_arguments
    def put_password_org_config_with_http_info(
            self, password_org_config: PasswordOrgConfig,
            **kwargs) -> ApiResponse:  # noqa: E501
        """Update Password Org Config  # noqa: E501

        This API updates the password org config for specified fields. Other fields will keep original value. You must set the `customInstructionsEnabled` field to \"true\" to be able to use custom password instructions.  Requires ORG_ADMIN, API role or authorization scope of 'idn:password-org-config:write'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_password_org_config_with_http_info(password_org_config, async_req=True)
        >>> result = thread.get()

        :param password_org_config: (required)
        :type password_org_config: PasswordOrgConfig
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PasswordOrgConfig, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ['password_org_config']
        _all_params.extend([
            'async_req', '_return_http_data_only', '_preload_content',
            '_request_timeout', '_request_auth', '_content_type', '_headers'
        ])

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'"
                                   " to method put_password_org_config" % _key)
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['password_org_config'] is not None:
            _body_params = _params['password_org_config']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            '_content_type',
            self.api_client.select_header_content_type(['application/json']))
        if _content_types_list:
            _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['UserContextAuth', 'UserContextAuth']  # noqa: E501

        _response_types_map = {
            '200': "PasswordOrgConfig",
            '400': "ErrorResponseDto",
            '401': "ListAccessProfiles401Response",
            '403': "ErrorResponseDto",
            '429': "ListAccessProfiles429Response",
            '500': "ErrorResponseDto",
        }

        return self.api_client.call_api(
            '/password-org-config',
            'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
