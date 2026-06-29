import redis


redis_url = "redis://127.0.0.1:6379"
# 定义redis客户端
redis_client = redis.Redis(redis_url)
#ping
print(redis_client.ping())