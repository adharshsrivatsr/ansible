#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The module file for nxos_lldp_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: nxos_lldp_interfaces
version_added: 2.10
short_description: Manages interfaces' configuration for Link Layer Discovery Protocol (LLDP) on NX-OS platforms.
description: This module manages interfaces' configuration for Link Layer Discovery Protocol (LLDP) on NX-OS platforms.
author: Adharsh Srivats Rangarajan (@adharshsrivatsr)
notes:
  - Tested against NXOS 7.3.(0)D1(1) on VIRL
  - The LLDP feature needs to be enabled before using this module
options:
  config:
    description:
      - A list of link layer discovery configurations for interfaces.
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of the interface
        required: true
        type: str
      receive:
        description:
          - Used to enable or disable the reception of LLDP packets on that interface. By default, this is enabled after LLDP is enabled globally.
        type: bool
      transmit:
        description:
          - Used to enable or disable the transmission of LLDP packets on that interface. By default, this is enabled after LLDP is enabled globally.
        type: bool
      tlv_set:
        description:
          - Used to configure TLV parameters on the interface
        type: dict
        suboptions:
          management_address:
            description:
              - Used to mention the IPv4 or IPv6 management address for the interface
            type: str
          vlan:
            description:
              - Used to mention the VLAN for the interface
            type: int
  state:
    description:
      - The state the configuration should be left in
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
    default: merged
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#

- name : Merge provided configuration with device configuration
  nxos_lldp_interfaces:
    config:
        - name : Ethernet1/4
          receive: false
          transmit: true
          tlv_set:
            management_address: 192.168.122.64
          vlan: 12
    state: merged

# After state:
# -------------
#
# interface Ethernet1/4
#   no lldp receive
#   lldp tlv-set management-address 192.168.122.64
#   lldp tlv-set vlan 12


# Using replaced

# Before state:
# ------------
#
# interface Ethernet1/4
#   no lldp receive
#   lldp tlv-set management-address 192.168.122.64
# interface Ethernet1/5
#   no lldp transmit
#   lldp tlv-set vlan 10

- name: Replace LLDP configuration on interfaces with given configuration
  nxos_lldp_interfaces:
    config:
        - name: Ethernet1/4
          transmit: no
          tlv_set:
            vlan: 2
    state: replaced


# After state:
# -----------
#
# interface Ethernet1/4
#   no lldp transmit
#   lldp tlv_set vlan 2
# interface Ethernet1/5
#   no lldp transmit
#   lldp tlv-set vlan 10


# Using overridden

# Before state:
# ------------
#
# interface Ethernet1/4
#   no lldp receive
#   lldp tlv-set management-address 192.168.122.64
# interface Ethernet1/5
#   no lldp transmit
#   lldp tlv-set vlan 10

- name: Override LLDP configuration on all interfaces with given configuration
  nxos_lldp_interfaces:
    config:
        - name: Ethernet1/7
          receive: no
          tlv_set:
            vlan: 12
    state: overridden


# After state:
# -----------
#
# interface Ethernet1/7
#   no lldp receive
#   lldp tlv_set vlan 12


# Using deleted

# Before state:
# ------------
#
# interface Ethernet1/4
#   lldp tlv-set management vlan 24
#   no lldp transmit
# interface mgmt0
#   no lldp receive

- name: Delete LLDP interfaces configuration
  nxos_lldp_interfaces:
    state: deleted

# After state:
# ------------
#


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Ethernet1/2', 'lldp receive', 'lldp tlv-set vlan 12']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.nxos.argspec.lldp_interfaces.lldp_interfaces import Lldp_interfacesArgs
from ansible.module_utils.network.nxos.config.lldp_interfaces.lldp_interfaces import Lldp_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Lldp_interfacesArgs.argument_spec,
                           supports_check_mode=True)

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
