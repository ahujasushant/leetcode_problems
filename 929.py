class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            new_email = local_name + '@' + domain
            unique_emails.add(new_email)
        return len(unique_emails)