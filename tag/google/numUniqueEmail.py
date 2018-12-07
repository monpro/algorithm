class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # use hashmap to store address
        # one rule: delete every. and everything after first '+'
        # as key
        email_map = dict()
        for i in emails:
            email_map[self.helper(i)] = 0
        return len(email_map)

    def helper(self,email):
        email = email.split("@")
        after_at = email[1]
        before_at = email[0]
        before_at = before_at.replace('.','')
        before_at = before_at.split("+")
        before_at = before_at[0]
        return before_at + '@' + after_at



