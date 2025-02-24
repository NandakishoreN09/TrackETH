from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from config import TOKEN
from alchemy_api import get_eth_transactions, get_eth_balance  # ✅ Import get_eth_balance
from analysis import analyze_eth_wallet
from graph_generator import generate_graph


# Function to handle /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Welcome to **TrackETH**! 🚀\n\n"
        "Send me an **Ethereum wallet address**, and I'll analyze its **ETH inflow, outflow, and balance**, "
        "along with a **clean transaction flow diagram**."
    )

# Function to request Ethereum wallet address from user
async def ask_for_wallet(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("📩 Please send me an **Ethereum wallet address** to analyze.")

# Function to analyze ETH wallet transactions
async def analyze(update: Update, context: CallbackContext) -> None:
    wallet = update.message.text.strip()

    if not (wallet.startswith("0x") and len(wallet) == 42):
        await update.message.reply_text("❌ Invalid Ethereum address! Please enter a valid Ethereum wallet address.")
        return

    await update.message.reply_text(f"🔄 Fetching ETH transactions for `{wallet}` ... Please wait ⏳", parse_mode="Markdown")

    # Fetch ETH transactions
    df_eth = get_eth_transactions(wallet)

    if df_eth.empty:
        await update.message.reply_text("🚫 No ETH transactions found for this address.")
        return

    # Fetch ETH balance from Alchemy
    eth_balance = get_eth_balance(wallet)

    # Analyze ETH inflows and outflows
    eth_inflow, eth_outflow = analyze_eth_wallet(df_eth, wallet)

    # Construct response message
    message = (
        f"📊 **ETH Wallet Analysis for `{wallet[:6]}...{wallet[-4:]}`**\n\n"
        f"💰 **ETH Inflow:** {eth_inflow:.6f} ETH\n"
        f"📤 **ETH Outflow:** {eth_outflow:.6f} ETH\n"
        f"🔹 **ETH Balance:** {eth_balance:.6f} ETH"
    )

    await update.message.reply_text(message, parse_mode="Markdown")

    # Generate transaction flow graph
    img_path = generate_graph(df_eth, wallet)

    # Send the ETH transaction flow diagram
    with open(img_path, "rb") as photo:
        await update.message.reply_photo(photo=photo)



# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyze", ask_for_wallet))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze))

    # Start bot polling
    print("🤖 TrackETH Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
