import redis

def create_redis_record(key, value):
    r = redis.Redis(host='redis', port=6379, db=0)
    try:
        r.set(key, value)
        return "Register Success"
    except:
        return "Error. Try again."
