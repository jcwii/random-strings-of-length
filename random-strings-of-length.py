import random
import string

def rsol(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def rsols(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits + '~`! @#$%^&*()_-+={[}]|\:;"\'<,>.?/'):
    return ''.join(random.choice(chars) for _ in range(size))
