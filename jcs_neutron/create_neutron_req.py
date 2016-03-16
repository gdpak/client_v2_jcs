#!/usr/bin/env python

# Copyright 2016, Reliance Industries Ltd, all rights reserved.
# Author: Deepak Agrawal

import os
import sys
import datetime
from jcs_iam_client import generate_iam_token_from_key
import httplib
params, headers = {}, {}
method = 'GET'
path, port, auth_path = '', '', ''
body, host, protocol = '', '', ''

def add_params(string):
    length = len(string)
    parts = string.split('&')
    for p in parts:
        (key, val) = p.split('=')
        params[key] = val

def requestify(request):
    [initial, rest] = request.split('?')
    parts = initial.split('/')
    protocol, host_port = parts[0][ : -1], parts[2]
    path = '/' + parts[3] + '/' + parts[4] + '/'
    auth_path = path
    host = host_port
    add_params(rest)
    headers['User-Agent'] = 'curl/7.35.0'
    headers['Content-Type'] = 'application/json'
    reqObj = auth_handler.HTTPRequest(method, protocol, host, path, auth_path,
                         params, headers, body)
    authHandlerObj = auth_handler.V2Handler(host)
    reqObj = authHandlerObj.add_auth(reqObj)
    request_string = 'curl -k -X ' + reqObj.method
    request_string += ' -H \"Accept-Encoding: identity\"'
    request_string += ' -H \"User-Agent: ' + headers['User-Agent'] + '\"'
    request_string += ' -H \"Content-Type: ' + headers['Content-Type'] + '\"'
    request_string += ' \"' + initial + '?'
    for keys in reqObj.params:
        request_string += keys + '=' + reqObj.params[keys] + '&'
    request_string = request_string[ : -1]
    request_string += '\"'
    return request_string

def main():
    #req = sys.argv[1]
    iam_token_response = generate_iam_token_from_key()
    print iam_token_response
    print iam_token_response['token_id']
    #os.system(chngd_req)

main()
