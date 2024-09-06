⛔    BYBIT Exchange Affiliate Program SCAM ALERT ⛔ 


I have received a letter from Bybit Exchange:

* "After a thorough internal investigation conducted by our risk team, your account was being flagged out from receiving Referral commissions due to a violation of our Terms of Service and Bonus...                                                            Let it be clear that this decision is final and we will not accommodate any further appeals regarding the matter."   

I must admit that this is totally scam behaviour from the exchange. I have a lot of referees and as I know a lot of them have passed KYC. Sometimes I help traders with trades on their accounts but I neved registered another account for myself to receive comission. But Bybit say that "According to our statistics, we found out that most users who have successfully registered using your referral link created their accounts using the same IP address." This is total lie. I can't register account for users.

Also I sent email to them regargind my ref id P11NJW. But there is no answer as well.

So then let it be CLEAR, that since 
* Bybit violate their own rules
* Bybit scam users
* I'll not receive a Referral commission anymore
* They don't reply and there is no support

this project is closed and there will be no more updates. I'll move all my code to Binance, OKX etc soon.

By their actions they undermine my authority and I can no longer recommend trading on this platform.

⛔    BYBIT Exchange Affiliate Program SCAM ALERT ⛔ 



`

`

`

`

`

`

`

`

# Bybit Trades and OHLC Redis Saver
Saves OHLC data (klines) and trades from Bybit websockets to the Redis

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://aadresearch.xyz)

## Requirements

<code>pip install pybit==2.4.1</code>

<code>pip install pandas</code>

## How to run

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

This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial or other advice. Nothing contained here is a recommendation, endorsement or offer by me to buy or sell any securities or other financial instruments. If you intend to use real money, use it at your own risk. Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.


## Contacts
I develop trading bots of any complexity, dashboards and indicators for crypto exchanges, forex and stocks.
To contact me:

Discord: https://discord.gg/zSw58e9Uvf

Telegram: https://t.me/aadresearch


## VPS for bots and scripts
I prefer using DigitalOcean. 
To get $200 in credit over 60 days use my ref link: https://m.do.co/c/3d7f6e57bc04
