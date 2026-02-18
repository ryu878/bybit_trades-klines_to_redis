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



***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, liquidations, volume, delta, liquidity, spread behavior, funding)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL, ClickHouse
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***
