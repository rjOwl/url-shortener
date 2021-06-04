import random, string

def generateSlug(slugLen=8):
    slug = ''.join(random.choices(string.ascii_letters + string.digits, k=slugLen))
    return slug


def check_content_type(reqContent):
    if(reqContent and reqContent.startswith('application/json')):
        return True
    return False
