# coding: utf-8

"""
ExportApi.py
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


class ExportApi(object):
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

    def export_request(self, export_request_info, **kwargs):
        """
        Create Export Request
        Export normalized messages. The following input combinations are supported:<br/><table><tr><th>Combination</th><th>Parameters</th><th>Description</th></tr><tr><td>Get by users</td><td>uids</td><td>Search by a list of User IDs. For each user in the list, the current authenticated user must have read access over the specified user.</td></tr><tr><td>Get by devices</td><td>sdids</td><td>Search by Source Device IDs.</td></tr><tr><td>Get by device types</td><td>uids,sdtids</td><td>Search by list of Source Device Type IDs for the given list of users.</td></tr><tr><td>Get by trial</td><td>trialId</td><td>Search by Trial ID.</td></tr><tr><td>Get by combination of parameters</td><td>uids,sdids,sdtids</td><td>Search by list of Source Device IDs. Each Device ID must belong to a Source Device Type ID and a User ID.</td></tr><tr><td>Common</td><td>startDate,endDate,order,format,url,csvHeaders</td><td>Parameters that can be used with the above combinations.</td></tr></table>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export_request(export_request_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ExportRequestInfo export_request_info: ExportRequest object that is passed in the body (required)
        :return: ExportRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['export_request_info']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export_request" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'export_request_info' is set
        if ('export_request_info' not in params) or (params['export_request_info'] is None):
            raise ValueError("Missing the required parameter `export_request_info` when calling `export_request`")

        resource_path = '/messages/export'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'export_request_info' in params:
            body_params = params['export_request_info']

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

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ExportRequestResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_export_history(self, **kwargs):
        """
        Get Export History
        Get the history of export requests.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_export_history(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str trial_id: Filter by trialId.
        :param int count: Pagination count.
        :param int offset: Pagination offset.
        :return: ExportHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trial_id', 'count', 'offset']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_history" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/messages/export/history'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'trial_id' in params:
            query_params['trialId'] = params['trial_id']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'offset' in params:
            query_params['offset'] = params['offset']

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
                                            response_type='ExportHistoryResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_export_result(self, export_id, **kwargs):
        """
        Get Export Result
        Retrieve result of the export query in tgz format. The tar file may contain one or more files with the results.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_export_result(export_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str export_id: Export ID of the export query. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['export_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_result" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'export_id' is set
        if ('export_id' not in params) or (params['export_id'] is None):
            raise ValueError("Missing the required parameter `export_id` when calling `get_export_result`")

        resource_path = '/messages/export/{exportId}/result'.replace('{format}', 'json')
        path_params = {}
        if 'export_id' in params:
            path_params['exportId'] = params['export_id']

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
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_export_status(self, export_id, **kwargs):
        """
        Check Export Status
        Check status of the export query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_export_status(export_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str export_id: Export ID of the export query. (required)
        :return: ExportStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['export_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_export_status" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'export_id' is set
        if ('export_id' not in params) or (params['export_id'] is None):
            raise ValueError("Missing the required parameter `export_id` when calling `get_export_status`")

        resource_path = '/messages/export/{exportId}/status'.replace('{format}', 'json')
        path_params = {}
        if 'export_id' in params:
            path_params['exportId'] = params['export_id']

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
                                            response_type='ExportStatusResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
