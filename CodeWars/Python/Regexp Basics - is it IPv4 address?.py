"""
Implement `ipv4_address`, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading `0`s, spaces etc.
"""

def ipv4_address(address):
    ip_range = [str(x) for x in range(0, 256)]
    if not address or len(address.split('.')) != 4:
        return False

    for i in address.split('.'):
        if not i in ip_range:
            return False

    return True
