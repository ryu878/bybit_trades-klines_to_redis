# Ryuryu's Get Bybit Trades and OHLC from Redis
# Redis Edition (Production Mode #6973)
# ---------------------------------------------
# (c) 2023 Ryan Hayabusa 
# GitGub: https://github.com/ryu878
# Web: https://aadresearch.xyz
# Discord: https://discord.gg/zSw58e9Uvf
# Telegram: https://t.me/aadresearch
# ---------------------------------------------
# Instructions:
# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# Redis instance: http://localhost:8001
# Release the port if used:
# sudo fuser -k 6379/tcp

import time
import redis
import pandas as pd
from config import redis_host, redis_port, redis_db



r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

symbol = 'DOGEUSDT'


while True:

    keys = r.keys(f'{symbol}-*')
    # print(keys)

    data_list = []

    for key in keys:
        data = r.hgetall(key)
        # print(key, data)
        data_dict = {k.decode(): v.decode() for k, v in data.items()}
        # data_list.append({"key": key.decode(), "data": data_dict})
        data_list.append(data_dict)

    # data_json = json.dumps(data_list, ensure_ascii=False)
    # print(data_json)

    df = pd.DataFrame(data_list)
    df = df.sort_values(by='open_time')
    df['sma6low'] = df['low'].rolling(6).mean()
    df['sma6hgh'] = df['high'].rolling(6).mean()
    df['sma33'] = df['close'].rolling(33).mean()
    df['sma60'] = df['close'].rolling(60).mean()
    df['sma120'] = df['close'].rolling(120).mean()
    df['sma240'] = df['close'].rolling(240).mean()
    df['240low'] = df['close'].rolling(240).min()
    df['240hgh'] = df['close'].rolling(240).max()
    
    print(df.tail(7))

    price = float(r.hgetall(symbol).get(b'price'))
    side = str((r.hgetall(symbol).get(b'side')).decode())
    size = float(r.hgetall(symbol).get(b'size'))

    print('Price:',price,'Side:',side,'Size:',size)

    time.sleep(0.1)
