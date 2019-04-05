import re


def numUniqueEmails(emails: [str]) -> int:
    def parse(email):
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        return f"{local}@{domain}"
    return len(set(map(parse, emails)))

mail = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print(numUniqueEmails(mail))
