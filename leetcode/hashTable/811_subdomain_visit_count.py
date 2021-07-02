"""
811. Subdomain Visit Count
- Easy
- Hash Table
- Link: https://leetcode.com/problems/subdomain-visit-count/
"""


# Solution 1: Hash Table, String
# Time: O(N*D), where D is the longest subdomain of each domain | Space: O(N)
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}

        for domain in cpdomains:
            count, address = domain.split(' ')
            subdomain = address.split('.')[::-1]
            curSubDomain = ""
            for sub in subdomain:
                curSubDomain = sub + "." + curSubDomain
                if curSubDomain in d:
                    d[curSubDomain] += int(count)
                else:
                    d[curSubDomain] = int(count)

        return ["{} {}".format(v, k[:-1]) for k, v in d.items()]
