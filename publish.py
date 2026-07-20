from redis.asyncio import Redis

def publish(updated_data):
  try:
    redis_update_admin = Redis.from_url("", decode_responses = True)
    await redis_update_admin.publish("update_admin", json.dumps(updated_data))
  except Exception as e:
    print(f"Failed to update: {e}")


  
