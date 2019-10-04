# 1108 defanging an ip address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAdd = address.replace(".", "[.]", 3)
        return newAdd
        
