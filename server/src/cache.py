import redis
import hashlib

# redis_client.set(key, value, redis_ttl)
# value = redis_client.get(key)

    
class RedisClient(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='redis', port=6379, db=0)
    
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self.get_client()
        return self._client
    
    def get_client(self):
        self._client = redis.Redis(connection_pool = self.pool)




