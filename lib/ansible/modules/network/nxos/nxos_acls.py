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
The module file for nxos_acls
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
module: nxos_acls
version_added: '2.10'
short_description: Manage named IP ACLs on the Cisco NX-OS platform
description: Manage named IP ACLs on the Cisco NX-OS platform
author: Adharsh Srivats Rangarajan (@adharshsrivatsr)
notes:
  - Tested against NX-OS 7.3.(0)D1(1) on VIRL
  - As NX-OS allows configuring a rule again with different sequence numbers,
    the user is expected to provide sequence numbers for the access control entries to preserve idempotency.
    If no sequence number is given, the rule will be added as a new rule by the device.
  - To parse configuration text, provide the output of show running-config | section access-list or a mocked up config
options:
  running_config:
    description:
      - Parse given commands into structured format. Required if I(state=parsed).
    type: str
  config:
    description: A dictionary of ACL options.
    type: list
    elements: dict
    suboptions:
      afi:
        description: The Address Family Indicator (AFI) for the ACL.
        type: str
        required: true
        choices: ['ipv4', 'ipv6']
      acls:
        description: A list of the ACLs.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the ACL.
            type: str
            required: true
          aces:
            description: The entries within the ACL.
            type: list
            elements: dict
            suboptions:
              grant:
                description: Action to be applied on the rule.
                type: str
                choices: ['permit', 'deny']
              destination:
                description: Specify the packet destination.
                type: dict
                suboptions:
                  address:
                    description: Destination network address.
                    type: str
                  any:
                    description: Any destination address.
                    type: bool
                  host:
                    description: Host IP address.
                    type: str
                  port_protocol:
                    description: Specify the destination port or protocol (only for TCP and UDP).
                    type: dict
                    suboptions:
                      eq:
                        description: Match only packets on a given port number.
                        type: str
                      gt:
                        description: Match only packets with a greater port number.
                        type: str
                      lt:
                        description: Match only packets with a lower port number.
                        type: str
                      neq:
                        description: Match only packets not on a given port number.
                        type: str
                      range:
                        description: Match only packets in the range of port numbers.
                        type: dict
                        suboptions:
                          start:
                            description: Specify the start of the port range.
                            type: str
                          end:
                            description: Specify the end of the port range.
                            type: str
                  prefix:
                    description: Destination network prefix. Only for prefixes of value less than 31 for ipv4 and 127 for ipv6.
                                 Prefixes of 32 (ipv4) and 128 (ipv6) should be given in the 'host' key.
                    type: str
                  wildcard_bits:
                    description: Destination wildcard bits.
                    type: str

              dscp:
                description: Match packets with given DSCP value.
                type: str

              fragments:
                description: Check non-initial fragments.
                type: bool

              remark:
                description: Access list entry comment.
                type: str

              sequence:
                description: Sequence number.
                type: int

              source:
                description: Specify the packet source.
                type: dict
                suboptions:
                  address:
                    description: Source network address.
                    type: str
                  any:
                    description: Any source address.
                    type: bool
                  host:
                    description: Host IP address.
                    type: str
                  port_protocol:
                    description: Specify the destination port or protocol (only for TCP and UDP).
                    type: dict
                    suboptions:
                      eq:
                        description: Match only packets on a given port number.
                        type: str
                      gt:
                        description: Match only packets with a greater port number.
                        type: str
                      lt:
                        description: Match only packets with a lower port number.
                        type: str
                      neq:
                        description: Match only packets not on a given port number.
                        type: str
                      range:
                        description: Match only packets in the range of port numbers.
                        type: dict
                        suboptions:
                          start:
                            description: Specify the start of the port range.
                            type: str
                          end:
                            description: Specify the end of the port range.
                            type: str
                  prefix:
                    description: Source network prefix. Only for prefixes of mask value less than 31 for ipv4 and 127 for ipv6.
                                 Prefixes of mask 32 (ipv4) and 128 (ipv6) should be given in the 'host' key.
                    type: str
                  wildcard_bits:
                    description: Source wildcard bits.
                    type: str

              log:
                description: Log matches against this entry.
                type: bool

              precedence:
                description: Match packets with given precedence value.
                type: str

              protocol:
                description: Specify the protocol.
                type: str

              protocol_options:
                description: All possible suboptions for the protocol chosen.
                type: dict
                suboptions:
                  icmp:
                    description: ICMP protocol options.
                    type: dict
                    suboptions:
                      administratively_prohibited:
                        description: Administratively prohibited
                        type: bool
                      alternate_address:
                        description: Alternate address
                        type: bool
                      conversion_error:
                        description: Datagram conversion
                        type: bool
                      dod_host_prohibited:
                        description: Host prohibited
                        type: bool
                      dod_net_prohibited:
                        description: Net prohibited
                        type: bool
                      echo:
                        description: Echo (ping)
                        type: bool
                      echo_reply:
                        description: Echo reply
                        type: bool
                      general_parameter_problem:
                        description: Parameter problem
                        type: bool
                      host_isolated:
                        description: Host isolated
                        type: bool
                      host_precedence_unreachable:
                        description: Host unreachable for precedence
                        type: bool
                      host_redirect:
                        description: Host redirect
                        type: bool
                      host_tos_redirect:
                        description: Host redirect for TOS
                        type: bool
                      host_tos_unreachable:
                        description: Host unreachable for TOS
                        type: bool
                      host_unknown:
                        description: Host unknown
                        type: bool
                      host_unreachable:
                        description: Host unreachable
                        type: bool
                      information_reply:
                        description: Information replies
                        type: bool
                      information_request:
                        description: Information requests
                        type: bool
                      mask_reply:
                        description: Mask replies
                        type: bool
                      mask_request:
                        description: Mask requests
                        type: bool
                      message_code:
                        description: ICMP message code
                        type: int
                      message_type:
                        description: ICMP message type
                        type: int
                      mobile_redirect:
                        description: Mobile host redirect
                        type: bool
                      net_redirect:
                        description: Network redirect
                        type: bool
                      net_tos_redirect:
                        description: Net redirect for TOS
                        type: bool
                      net_tos_unreachable:
                        description: Network unreachable for TOS
                        type: bool
                      net_unreachable:
                        description: Net unreachable
                        type: bool
                      network_unknown:
                        description: Network unknown
                        type: bool
                      no_room_for_option:
                        description: Parameter required but no room
                        type: bool
                      option_missing:
                        description: Parameter required but not present
                        type: bool
                      packet_too_big:
                        description: Fragmentation needed and DF set
                        type: bool
                      parameter_problem:
                        description: All parameter problems
                        type: bool
                      port_unreachable:
                        description: Port unreachable
                        type: bool
                      precedence_unreachable:
                        description: Precedence cutoff
                        type: bool
                      protocol_unreachable:
                        description: Protocol unreachable
                        type: bool
                      reassembly_timeout:
                        description: Reassembly timeout
                        type: bool
                      redirect:
                        description: All redirects
                        type: bool
                      router_advertisement:
                        description: Router discovery advertisements
                        type: bool
                      router_solicitation:
                        description: Router discovery solicitations
                        type: bool
                      source_quench:
                        description: Source quenches
                        type: bool
                      source_route_failed:
                        description: Source route failed
                        type: bool
                      time_exceeded:
                        description: All time exceeded.
                        type: bool
                      timestamp_reply:
                        description: Timestamp replies
                        type: bool
                      timestamp_request:
                        description: Timestamp requests
                        type: bool
                      traceroute:
                        description: Traceroute
                        type: bool
                      ttl_exceeded:
                        description: TTL exceeded
                        type: bool
                      unreachable:
                        description: All unreachables
                        type: bool
                  tcp:
                    description: TCP flags.
                    type: dict
                    suboptions:
                      ack:
                        description: Match on the ACK bit
                        type: bool
                      established:
                        description: Match established connections
                        type: bool
                      fin:
                        description: Match on the FIN bit
                        type: bool
                      psh:
                        description: Match on the PSH bit
                        type: bool
                      rst:
                        description: Match on the RST bit
                        type: bool
                      syn:
                        description: Match on the SYN bit
                        type: bool
                      urg:
                        description: Match on the URG bit
                        type: bool
                  igmp:
                    description: IGMP protocol options.
                    type: dict
                    suboptions:
                      dvmrp:
                        description: Distance Vector Multicast Routing Protocol
                        type: bool
                      host_query:
                        description: Host Query
                        type: bool
                      host_report:
                        description: Host Report
                        type: bool

  state:
    description:
      - The state the configuration should be left in
    type: str
    choices:
      - deleted
      - gathered
      - merged
      - overridden
      - rendered
      - replaced
      - parsed
    default: merged
"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#

- name: Merge new ACLs configuration
  nxos_acls:
    config:
      - afi: ipv4
        acls:
          - name: ACL1v4
            aces:
              - grant: deny
                destination:
                  address: 192.0.2.64
                  wildcard_bits: 0.0.0.255
                source:
                  any: true
                  port_protocol:
                    lt: 55
                protocol: tcp
                protocol_options:
                  tcp:
                    ack: true
                    fin: true
                sequence: 50

      - afi: ipv6
        acls:
          - name: ACL1v6
            aces:
              - grant: permit
                sequence: 10
                source:
                  any: true
                destination:
                  prefix: 2001:db8:12::/32
                protocol: sctp
    state: merged

# After state:
# ------------
#
# ip access-list ACL1v4
#  50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
# ipv6 access-list ACL1v6
#  10 permit sctp any any

# Using replaced

# Before state:
# ----------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Replace existing ACL configuration with provided configuration
  nxos_acls:
    config:
      - afi: ipv4
      - afi: ipv6
        acls:
          - name: ACL1v6
            aces:
              - sequence: 20
                grant: permit
                source:
                  any: true
                destination:
                  any: true
                protocol: pip

              - remark: Replaced ACE

          - name: ACL2v6
    state: replaced

# After state:
# ---------------
#
# ipv6 access-list ACL1v6
#   20 permit pip any any
#   30 remark Replaced ACE
# ipv6 access-list ACL2v6

# Using overridden

# Before state:
# ----------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Override existing configuration with provided configuration
  nxos_acls:
    config:
      - afi: ipv4
        acls:
          - name: NewACL
            aces:
              - grant: deny
                source:
                  address: 192.0.2.0
                  wildcard_bits: 0.0.255.255
                destination:
                  any: true
                protocol: eigrp
              - remark: Example for overridden state
    state: overridden

# After state:
# ------------
#
# ip access-list NewACL
#   10 deny eigrp 192.0.2.0 0.0.255.255 any
#   20 remark Example for overridden state

# Using deleted:
#
# Before state:
# -------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Delete all ACLs
  nxos_acls:
    config:
    state: deleted

# After state:
# -----------
#


# Before state:
# -------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Delete all ACLs in given AFI
  nxos_acls:
    config:
      - afi: ipv4
    state: deleted

# After state:
# ------------
#
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128



# Before state:
# -------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACL1v6
#   10 permit sctp any any
#   20 remark IPv6 ACL
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

- name: Delete specific ACLs
  nxos_acls:
    config:
      - afi: ipv6
        acls:
          - name: ACL1v6
            aces:
              - grant: permit
                sequence: 10
                source:
                  any: true
                destination:
                  any: true
                protocol: sctp

              - sequence: 20
    state: deleted

# After state:
# ------------
#
# ip access-list ACL1v4
#   10 permit ip any any
#   20 deny udp any any
# ip access-list ACL2v4
#   10 permit ahp 192.0.2.0 0.0.0.255 any
# ip access-list ACl1v6
# ip access-list ACL2v6
#  10 deny ipv6 any 2001:db8:3000::/36
#  20 permit tcp 2001:db8:2000:2::2/128 2001:db8:2000:ab::2/128

# Using parsed
#
# Before state:
# ------------
#

- name: Parse given config to structured data
  nxos_acls:
    running_config: |
      ip access-list ACL1v4
        50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
      ipv6 access-list ACL1v6
        10 permit sctp any any
    state: parsed

# After state:
# -----------
#

# returns:
# parsed:
# - afi: ipv4
#   acls:
#     - name: ACL1v4
#       aces:
#         - grant: deny
#           destination:
#             address: 192.0.2.64
#             wildcard_bits: 0.0.0.255
#           source:
#             any: true
#             port_protocol:
#               lt: 55
#           protocol: tcp
#           protocol_options:
#             tcp:
#               ack: true
#               fin: true
#           sequence: 50
#
# - afi: ipv6
#   acls:
#     - name: ACL1v6
#       aces:
#         - grant: permit
#           sequence: 10
#           source:
#             any: true
#           destination:
#             prefix: 2001:db8:12::/32
#           protocol: sctp

# Using gathered:

# Before state:
# ------------
#
# ip access-list ACL1v4
#  50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
# ipv6 access-list ACL1v6
#  10 permit sctp any any

- name: Gather existing configuration
  nxos_acls:
    state: gathered

# After state:
# ------------
#
# ip access-list ACL1v4
#  50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
# ipv6 access-list ACL1v6
#  10 permit sctp any any

# returns:
# nxos_acls:
#   config:
#     - afi: ipv4
#       acls:
#         - name: ACL1v4
#           aces:
#             - grant: deny
#               destination:
#                 address: 192.0.2.64
#                 wildcard_bits: 0.0.0.255
#               source:
#                 any: true
#                 port_protocol:
#                   lt: 55
#               protocol: tcp
#               protocol_options:
#                 tcp:
#                   ack: true
#                   fin: true
#               sequence: 50

#     - afi: ipv6
#       acls:
#         - name: ACL1v6
#           aces:
#             - grant: permit
#               sequence: 10
#               source:
#                 any: true
#               destination:
#                 prefix: 2001:db8:12::/32
#               protocol: sctp

# Using rendered

# Before state:
# ------------
#
- name: Render required configuration to be pushed to the device
  nxos_acls:
    config:
      - afi: ipv4
        acls:
          - name: ACL1v4
            aces:
              - grant: deny
                destination:
                  address: 192.0.2.64
                  wildcard_bits: 0.0.0.255
                source:
                  any: true
                  port_protocol:
                    lt: 55
                protocol: tcp
                protocol_options:
                  tcp:
                    ack: true
                    fin: true
                sequence: 50

      - afi: ipv6
        acls:
          - name: ACL1v6
            aces:
              - grant: permit
                sequence: 10
                source:
                  any: true
                destination:
                  prefix: 2001:db8:12::/32
                protocol: sctp
    state: rendered
# After state:
# -----------
#

# returns:
# rendered:
#  ip access-list ACL1v4
#   50 deny tcp any lt 55 192.0.2.64 0.0.0.255 ack fin
#  ipv6 access-list ACL1v6
#   10 permit sctp any any
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['ip access-list ACL1v4', '10 permit ip any any precedence critical log', '20 deny tcp any lt smtp host 192.0.2.64 ack fin']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.nxos.argspec.acls.acls import AclsArgs
from ansible.module_utils.network.nxos.config.acls.acls import Acls


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=AclsArgs.argument_spec,
                           supports_check_mode=True)

    result = Acls(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
