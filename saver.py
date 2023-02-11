# Ryuryu's Bybit Trades and OHLC Saver
# Redis Edition (Production Mode #6973)
# -------------------------------------
# (c) 2023 Ryan Hayabusa 
# GitGub: https://github.com/ryu878
# Web: https://aadresearch.xyz
# Discord: https://discord.gg/zSw58e9Uvf
# Telegram: https://t.me/aadresearch
# -------------------------------------
# Instructions:
# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# Redis instance: http://localhost:8001
# Release the port if used:
# sudo fuser -k 6379/tcp

import time
import redis
import datetime
from pybit import usdt_perpetual
from config import interval, redis_host, redis_port, redis_db, redis_trade_ttl, redis_kline_ttl, endpoint, domain



r = redis.Redis(host=redis_host,port=redis_port,db=redis_db)
ws = usdt_perpetual.WebSocket(test=False, domain=domain)
session_unauth = usdt_perpetual.HTTP(endpoint=endpoint)
max_leverage = session_unauth.query_symbol()

assets = []

for leverage in max_leverage['result']:
    symbol = leverage['name']
    leverage = leverage['leverage_filter']['max_leverage']
    if leverage >= 50 and 'USDT' in symbol:
        #print(symbol)
        assets.append(symbol)

# print(assets)

def get_trades(trades):
    # print(trades)
    symbol= trades['data'][0]['symbol']
    price = trades['data'][0]['price']
    side = trades['data'][0]['side']
    size = trades['data'][0]['size']

    r.hset(str(symbol), 'price', price)
    r.hset(str(symbol), 'side', side)
    r.hset(str(symbol), 'size', size)
    r.execute_command('expire',str(symbol), redis_trade_ttl)
    
    print(' Trade:',symbol,price)

for asset in assets:
    # print(asset)
    ws.trade_stream(get_trades, asset)


def get_ohcl(ohcl):
    
    symbol = ohcl['topic'].replace('candle.1.','')
    # print(symbol)
    kline_data = ohcl['data'][0]
    # print(kline_data)
    timestamp_ms = kline_data['start']
    timestamp_ms = datetime.datetime.fromtimestamp(timestamp_ms)
    timestamp_ms = timestamp_ms.strftime('%Y-%m-%d %H:%M:00') 
    
    r.hset(symbol+'-'+timestamp_ms, 'symbol', symbol)
    r.hset(symbol+'-'+timestamp_ms, 'open_time', int(kline_data['start']))
    r.hset(symbol+'-'+timestamp_ms, 'open', kline_data['open'])
    r.hset(symbol+'-'+timestamp_ms, 'high', kline_data['high'])
    r.hset(symbol+'-'+timestamp_ms, 'low', kline_data['low'])
    r.hset(symbol+'-'+timestamp_ms, 'close', kline_data['close'])
    r.hset(symbol+'-'+timestamp_ms, 'volume', kline_data['volume'])
    r.execute_command('expire', str(symbol+'-'+timestamp_ms), redis_kline_ttl)
    
    print(' Kline:',symbol,timestamp_ms)

ws.kline_stream(get_ohcl, assets, interval)

while True:
          
    time.sleep(1)
