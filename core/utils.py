import shortuuid


def short_url():
    return shortuuid.ShortUUID().random(length=8)

def create_uuid():
    return shortuuid.uuid()