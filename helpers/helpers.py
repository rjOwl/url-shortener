import random, string

def generateSlug(slugLen=8):
    slug = ''.join(random.choices(string.ascii_letters + string.digits, k=slugLen))
    return slug


def check_content_type(req):
    print("CONTENT:\n\n\n", req)
    if(req and req.startswith('application/json')):
        return True
    return False
