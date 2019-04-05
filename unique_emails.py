import re


def numUniqueEmails(emails: [str]) -> int:    
    return len(set(map(parse, emails)))


def parse(email):
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        return f"{local}@{domain}"

mail = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"]

print(numUniqueEmails(mail))
