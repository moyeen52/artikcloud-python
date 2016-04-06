# coding: utf-8

"""
RulesApi.py
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


class RulesApi(object):
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

    def create_rule(self, rule_info, user_id, **kwargs):
        """
        Create Rule
        Create a new Rule

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_rule(rule_info, user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RuleCreationInfo rule_info: Rule object that needs to be added (required)
        :param str user_id: User ID (required)
        :return: RuleEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_info', 'user_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_info' is set
        if ('rule_info' not in params) or (params['rule_info'] is None):
            raise ValueError("Missing the required parameter `rule_info` when calling `create_rule`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `create_rule`")

        resource_path = '/rules'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'user_id' in params:
            query_params['userId'] = params['user_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule_info' in params:
            body_params = params['rule_info']

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
                                            response_type='RuleEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_rule(self, rule_id, **kwargs):
        """
        Get Rule
        Get a rule using the Rule ID

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_rule(rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str rule_id: Rule ID. (required)
        :return: RuleEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params) or (params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `get_rule`")

        resource_path = '/rules/{ruleId}'.replace('{format}', 'json')
        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']

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
                                            response_type='RuleEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_rule(self, rule_id, rule_info, **kwargs):
        """
        Update Rule
        Update an existing Rule

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_rule(rule_id, rule_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str rule_id: Rule ID. (required)
        :param RuleUpdateInfo rule_info: Rule object that needs to be updated (required)
        :return: RuleEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id', 'rule_info']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params) or (params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `update_rule`")
        # verify the required parameter 'rule_info' is set
        if ('rule_info' not in params) or (params['rule_info'] is None):
            raise ValueError("Missing the required parameter `rule_info` when calling `update_rule`")

        resource_path = '/rules/{ruleId}'.replace('{format}', 'json')
        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'rule_info' in params:
            body_params = params['rule_info']

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

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RuleEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_rule(self, rule_id, **kwargs):
        """
        Delete Rule
        Delete a Rule

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_rule(rule_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str rule_id: Rule ID. (required)
        :return: RuleEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['rule_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_rule" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params) or (params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `delete_rule`")

        resource_path = '/rules/{ruleId}'.replace('{format}', 'json')
        path_params = {}
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']

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

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RuleEnvelope',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
