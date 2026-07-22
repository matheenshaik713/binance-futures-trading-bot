# 📈 Binance Futures Testnet Trading Bot

A modular Python-based trading bot for the **Binance USDT-M Futures Testnet** that allows users to place **Market** and **Limit** orders through both a **Command-Line Interface (CLI)** and a **Streamlit Web UI**.

This project was developed as part of the **Primetrade.ai Python Developer Application Task** and demonstrates clean software architecture, input validation, logging, and robust exception handling.

---

# 🚀 Features

- ✅ Place **Market Orders**
- ✅ Place **Limit Orders**
- ✅ Support for **BUY** and **SELL** orders
- ✅ Binance **USDT-M Futures Testnet**
- ✅ Command-Line Interface (Typer)
- ✅ Streamlit Web Interface (Bonus)
- ✅ Input Validation
- ✅ Structured Logging
- ✅ Exception Handling
- ✅ Modular Project Structure
- ✅ Environment Variable Support (.env)

---

# 📂 Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── exceptions.py
│
├── logs/
│   ├── trading.log
│   ├── market_order.log
│   └── limit_order.log
│
├── cli.py
├── ui.py
├── config.py
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Prerequisites

- Python 3.10+
- Binance Futures Testnet Account
- Binance Futures Testnet API Key
- Binance Futures Testnet Secret Key

---

# 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/binance-futures-trading-bot.git

cd binance-futures-trading-bot
```

Create a virtual environment:

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_SECRET_KEY=YOUR_SECRET_KEY
```

You can obtain your API credentials from the **Binance Futures Testnet**.

---

# ▶️ Running the CLI

### Market BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

### Market SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type MARKET --quantity 0.001
```

### Limit BUY

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 50000
```

### Limit SELL

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 120000
```

---

# 🌐 Running the Streamlit UI

Start the web application:

```bash
streamlit run ui.py
```

The application will open automatically in your browser.

---

# 📝 Logging

All API requests, responses, and errors are automatically recorded in:

```text
logs/trading.log
```

Additional sample logs:

- `logs/market_order.log`
- `logs/limit_order.log`

---

# 🛡 Validation

The application validates:

- Trading Symbol
- BUY / SELL Side
- MARKET / LIMIT Order Type
- Quantity
- Price (required for LIMIT orders)

Invalid inputs are handled gracefully with clear error messages.

---

# ⚠ Error Handling

The application includes robust exception handling for:

- Invalid user input
- Binance API errors
- Network failures
- Authentication issues
- Unexpected runtime exceptions

---

# 🛠 Technologies Used

- Python 3
- python-binance
- Typer
- Streamlit
- Rich
- python-dotenv
- Logging

---

# 📸 Screenshots

You can add screenshots here before submitting:

### CLI

```
(Add CLI Screenshot Here)
```

### Streamlit UI

```
(Add Streamlit UI Screenshot Here)
```

---

# 📋 Assumptions

- Binance Futures Testnet account is active.
- API credentials are correctly configured.
- Testnet account has sufficient virtual funds.
- Internet connection is available.

---

# 👨‍💻 Author

**Shaik Mateen**

B.Tech – Computer Science and Engineering

---

# 📄 License

This project is released under the **MIT License**.
