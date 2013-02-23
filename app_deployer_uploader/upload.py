#! /usr/bin/env python
# -*- coding: utf-8 -*-
#   Copyright 2013 Jacek Marchwicki <jacek.marchwicki@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys
import requests
import json
import urllib2
import json
import argparse
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

DEFAULT_BASE_URL = "https://app-deployer.appspot.com"

UPLOAD_URL = "/_ah/api/appdeployer/v1/uploads"

  #upload(options.app_guid, options.token, options.version
  #    fileName)
def upload(app_guid, token, version, file_name, base_url):
  register_openers()

  insert_url = base_url + UPLOAD_URL
  data = json.dumps({})
  headers = {'Content-Type': 'application/json'}

  resp = requests.post(insert_url, data=data, headers=headers)
  if resp.status_code != requests.codes.ok:
    sys.stderr.write("Wrong response from server:\n")
    sys.stderr.write("%s\n(%d)\n" % (resp.text, resp.status_code))
    return 1

  json_data = resp.json()
  upload_url = json_data["upload_url"]

  data = {
      'app_guid': str(app_guid),
      'token': str(token),
      'version': str(version),
        }
  files = {
      'file': open(file_name, 'rb')
      }
  resp = requests.post(upload_url, files=files, data=data)
  if resp.status_code != requests.codes.ok:
    sys.stderr.write("Wrong response from server:\n")
    sys.stderr.write("%s\n(%d)\n" % (resp.text, resp.status_code))
    return 1

  print "Uploaded"
  return 0

def main():

  parser = argparse.ArgumentParser(description='Upload file to AppDeploy server.')
  parser.add_argument('guid', metavar='GUID', type=str, 
    help='Application guid')
  parser.add_argument('token', metavar='TOKEN', type=str, 
    help='Application token')
  parser.add_argument('version', metavar='VERSION', type=str, 
    help='Upload application version')
  parser.add_argument('file_name', metavar='FILE', type=str, 
    help='File to upload')
  parser.add_argument('-u', '--base-url', dest="base_url",
      type=str, nargs="?", default=DEFAULT_BASE_URL,
      help="Base url for request")

  args = parser.parse_args()

  app_guid = args.guid
  token = args.token
  version = args.version
  file_name = args.file_name
  base_url = args.base_url

  ret = upload(app_guid, token, version, file_name, base_url)
  sys.exit(ret)
      

if __name__ == "__main__":
  main()

