# Bybit Trades and OHLC Redis Saver
Saves OHLC data (klines) and trades from Bybit websockets to the Redis

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Requirements

<code>pip install pybit</code>

## how to run

First you have to turn your Redis database on with that command:

<code>docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest</code>

then wait for a while and go to http://localhost:8001/redis-stack/browser to ensure that you Redis database in running.
Next run the script with a command

<code>python3 saver.py</code>
and it will start to save klines data and last trades data to your Redis database. Please ensure that it will save only 50-100x coins. If you want to save more just adjust coins filtering in the code on line 34

![image](https://user-images.githubusercontent.com/81808867/218305036-76dc63e9-57ce-48bf-8fbc-83f92bff910f.png)

If you want to get data from your Redis database there are example script named get_data.py. Run it and it will show you the data like this:

![image](https://user-images.githubusercontent.com/81808867/218305079-52ccc91f-5250-44cc-8cc6-2609828afb5a.png)



## Disclaimer
<hr>
<small>This project is for informational purposes only. You should not construe this information or any other material as legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you intend to use real money, use it at your own risk.

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.</small>
<hr>

## Contacts
Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch
