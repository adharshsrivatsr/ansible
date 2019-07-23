#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_appengine_firewall_rule_facts
description:
- Gather facts for GCP FirewallRule
short_description: Gather facts for GCP FirewallRule
version_added: 2.9
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options: {}
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: " a firewall rule facts"
  gcp_appengine_firewall_rule_facts:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: facts
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    description:
      description:
      - An optional string description of this rule.
      returned: success
      type: str
    sourceRange:
      description:
      - IP address or range, defined using CIDR notation, of requests that this rule
        applies to.
      returned: success
      type: str
    action:
      description:
      - The action to take if this rule matches.
      returned: success
      type: str
    priority:
      description:
      - A positive integer that defines the order of rule evaluation.
      - Rules with the lowest priority are evaluated first.
      - A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic
        when no previous rule matches. Only the action of this rule can be modified
        by the user.
      returned: success
      type: int
'''

################################################################################
# Imports
################################################################################
from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict())

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    items = fetch_list(module, collection(module))
    if items.get('ingressRules'):
        items = items.get('ingressRules')
    else:
        items = []
    return_value = {'resources': items}
    module.exit_json(**return_value)


def collection(module):
    return "https://appengine.googleapis.com/v1/apps/{project}/firewall/ingressRules".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'appengine')
    response = auth.get(link)
    return return_if_object(module, response)


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
