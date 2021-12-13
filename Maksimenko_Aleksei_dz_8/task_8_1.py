import re


def email_parse(email_address):
    pattern = re.compile(r"(?P<username>[^@&]+)@(?P<domain>[\w_-][\w_\.-]*\.[\w_-]{2,})$")
    result_match = pattern.match(email_address)
    if not result_match:
        raise ValueError(f"wrong email: {email_address}")
    return result_match.groupdict()


e_adr = input("Enter your email: ")
print(email_parse(e_adr))
