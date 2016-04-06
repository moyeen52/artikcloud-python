# coding: utf-8

"""
DeviceTypesApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DeviceTypesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_device_types(self, name, **kwargs):
        """
        Get Device Types
        Retrieves Device Types

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_device_types(name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Device Type name (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set
        :param str tags: Elements tagged with the list of tags. (comma separated)
        :return: DeviceTypesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'offset', 'count', 'tags']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_types" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_device_types`")

        resource_path = '/devicetypes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'name' in params:
            query_params['name'] = params['name']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'tags' in params:
            query_params['tags'] = params['tags']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceTypesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_device_type(self, device_type_id, **kwargs):
        """
        Get Device Type
        Retrieves a Device Type

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_device_type(device_type_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_type_id: deviceTypeId (required)
        :return: DeviceTypeEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_type" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'device_type_id' is set
        if ('device_type_id' not in params) or (params['device_type_id'] is None):
            raise ValueError("Missing the required parameter `device_type_id` when calling `get_device_type`")

        resource_path = '/devicetypes/{deviceTypeId}'.replace('{format}', 'json')
        path_params = {}
        if 'device_type_id' in params:
            path_params['deviceTypeId'] = params['device_type_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeviceTypeEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_available_manifest_versions(self, device_type_id, **kwargs):
        """
        Get Available Manifest Versions
        Get a Device Type's available manifest versions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_available_manifest_versions(device_type_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_type_id: deviceTypeId (required)
        :return: ManifestVersionsEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_manifest_versions" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'device_type_id' is set
        if ('device_type_id' not in params) or (params['device_type_id'] is None):
            raise ValueError("Missing the required parameter `device_type_id` when calling `get_available_manifest_versions`")

        resource_path = '/devicetypes/{deviceTypeId}/availablemanifestversions'.replace('{format}', 'json')
        path_params = {}
        if 'device_type_id' in params:
            path_params['deviceTypeId'] = params['device_type_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ManifestVersionsEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_latest_manifest_properties(self, device_type_id, **kwargs):
        """
        Get Latest Manifest Properties
        Get a Device Type's manifest properties for the latest version.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_latest_manifest_properties(device_type_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_type_id: Device Type ID. (required)
        :return: ManifestPropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_latest_manifest_properties" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'device_type_id' is set
        if ('device_type_id' not in params) or (params['device_type_id'] is None):
            raise ValueError("Missing the required parameter `device_type_id` when calling `get_latest_manifest_properties`")

        resource_path = '/devicetypes/{deviceTypeId}/manifests/latest/properties'.replace('{format}', 'json')
        path_params = {}
        if 'device_type_id' in params:
            path_params['deviceTypeId'] = params['device_type_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ManifestPropertiesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_manifest_properties(self, device_type_id, version, **kwargs):
        """
        Get manifest properties
        Get a Device Type's manifest properties for a specific version.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_manifest_properties(device_type_id, version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_type_id: Device Type ID. (required)
        :param str version: Manifest Version. (required)
        :return: ManifestPropertiesEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_type_id', 'version']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_manifest_properties" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'device_type_id' is set
        if ('device_type_id' not in params) or (params['device_type_id'] is None):
            raise ValueError("Missing the required parameter `device_type_id` when calling `get_manifest_properties`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_manifest_properties`")

        resource_path = '/devicetypes/{deviceTypeId}/manifests/{version}/properties'.replace('{format}', 'json')
        path_params = {}
        if 'device_type_id' in params:
            path_params['deviceTypeId'] = params['device_type_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ManifestPropertiesEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
