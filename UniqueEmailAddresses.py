class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        actualEmail = set()
        for email in  emails:
            res1 = email.split("@")
            domain = res1[1]
            res2 = res1[0].split("+")
            local = res2[0].replace(".", "")
            res1 = local + "@" + domain
            actualEmail.add(res1)
        return len(actualEmail)            