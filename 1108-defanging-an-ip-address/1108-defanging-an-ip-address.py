class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address=address.split(".")
        return "[.]".join(address)