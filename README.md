### **🚀 TrackETH - Ethereum Wallet Transaction Analyzer**
**TrackETH** is a **powerful and easy-to-use Ethereum wallet tracker** that fetches and visualizes **ETH inflow, outflow, and transaction flow graphs** using the **Alchemy API** and **Python Telegram Bot**.

---

## **📌 Features**
✅ **Real-time ETH transaction analysis** (inflow, outflow, and balance)  
✅ **Transaction flow diagram** to visualize wallet interactions  
✅ **Supports both received & sent ETH transactions**  
✅ **Secure API key handling using environment variables**  
✅ **Easy integration with Telegram for instant wallet analysis**  

---

## **🔧 Installation**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/NandakishoreN09/TrackETH.git
cd TrackETH
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file in the root directory and add your API keys:
```
ALCHEMY_API_KEY=your-alchemy-api-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

---

## **🛠️ Usage**
### **Start the Telegram Bot**
```bash
python bot.py
```

### **Interact with the Bot**
1. Open Telegram and search for your bot (configured in BotFather).
2. Send `/start` to initialize.
3. Send `/analyze` followed by an Ethereum wallet address.
4. The bot will return:
   - ETH inflow, outflow, and balance
   - A transaction flow diagram

---

## **🌟 Example Output**
```
📊 ETH Wallet Analysis for 0x0625...4624

💰 ETH Inflow: 3.410632 ETH
💴 ETH Outflow: 1.563210 ETH
🔹 ETH Balance: 1.847422 ETH
```

---

## **🔧 Tech Stack**
- **Python** (3.9+)
- **Telegram Bot API**
- **Alchemy API** (Ethereum blockchain data)
- **NetworkX & Matplotlib** (for transaction flow visualization)

---

## **✨ Contributing**
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.

---

## **🛠️ Troubleshooting**
- Ensure that `.env` is set up correctly.
- If you encounter `Invalid Token` errors, check your Telegram bot token.
- For missing libraries, run:
  ```bash
  pip install -r requirements.txt
  ```

---


## **👨‍💻 Author**
Developed by **Nandakishore N**. Feel free to connect!

