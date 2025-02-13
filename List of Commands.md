Here’s a detailed README-style documentation that includes each command and example usage:

---

# **Discord Bot - Stock & Crypto Tracker**

This bot allows you to get stock prices, cryptocurrency prices, historical data, set price alerts, track a portfolio, manage a watchlist, and much more.

---

## **Commands**

### **1. !stock**
- **Description**: Fetches the current stock price for a given symbol.
- **Usage**: `!stock SYMBOL`
- **Example**:
  - `!stock AAPL`  
  Fetches the current price of Apple Inc. (AAPL) stock.

---

### **2. !crypto**
- **Description**: Fetches the current price of a cryptocurrency.
- **Usage**: `!crypto COIN`
- **Example**:
  - `!crypto bitcoin`  
  Fetches the current price of Bitcoin (BTC).

---

### **3. !chart**
- **Description**: Generates a stock price chart for a given symbol and period (default is "30d").
- **Usage**: `!chart SYMBOL PERIOD`
- **Example**:
  - `!chart AAPL 30d`  
  Generates a chart for Apple stock (AAPL) showing the past 30 days of stock data.

---

### **4. !set_alert**
- **Description**: Sets a price alert for a given stock or cryptocurrency symbol.
- **Usage**: `!set_alert SYMBOL PRICE`
- **Example**:
  - `!set_alert AAPL 150`  
  Sets an alert for Apple stock (AAPL) when the price reaches $150.

---

### **5. !remove_alert**
- **Description**: Removes a price alert for a given symbol.
- **Usage**: `!remove_alert SYMBOL`
- **Example**:
  - ` `  
  Removes the alert set for Apple stock (AAPL).

---

### **6. !portfolio**
- **Description**: Tracks your stock portfolio and calculates the total value.
- **Usage**: `!portfolio SYMBOL QUANTITY`
- **Example**:
  - `!portfolio AAPL 10 MSFT 5`  
  Shows the value of 10 shares of Apple (AAPL) and 5 shares of Microsoft (MSFT), including the total portfolio value.

---

### **7. !historical**
- **Description**: Fetches historical stock data for a given symbol and period (default is "1y").
- **Usage**: `!historical SYMBOL PERIOD`
- **Example**:
  - `!historical AAPL 1y`  
  Fetches the historical data for Apple stock (AAPL) for the past 1 year.

---

### **8. !watchlist**
- **Description**: Manages a personal watchlist for stocks. You can add or view stocks on the watchlist.
- **Usage**: `!watchlist SYMBOL` or `!watchlist view`
- **Examples**:
  - `!watchlist AAPL`  
    Adds Apple stock (AAPL) to your watchlist.
  - `!watchlist view`  
    Views all the stocks currently on your watchlist.

---

### **9. !remove_watchlist**
- **Description**: Removes a stock from your watchlist.
- **Usage**: `!remove_watchlist SYMBOL`
- **Example**:
  - `!remove_watchlist AAPL`  
    Removes Apple stock (AAPL) from your watchlist.

---

### **10. !news**
- **Description**: Fetches the latest news for a given stock or cryptocurrency symbol.
- **Usage**: `!news SYMBOL`
- **Example**:
  - `!news AAPL`  
  Fetches the latest news for Apple Inc. (AAPL).
  - `!news bitcoin`  
  Fetches the latest news for Bitcoin.

---

### **11. !restricted**
- **Description**: A restricted command that can only be used by authorized users (configured in your environment variables).
- **Usage**: `!restricted`
- **Example**:
  - `!restricted`  
  If you are authorized, you can use this command. Otherwise, the bot will deny access.

---

### **12. !adminonly**
- **Description**: This command is restricted to users with the "Admin" role.
- **Usage**: `!adminonly`
- **Example**:
  - `!adminonly`  
  If you have the "Admin" role, you can use this command. Otherwise, you will be denied.

---

### **13. !botowner**
- **Description**: A command restricted to the bot owner only.
- **Usage**: `!botowner`
- **Example**:
  - `!botowner`  
  Only the bot owner can use this command.

---

### **14. !restart**
- **Description**: Restarts the bot. This command is restricted to the bot owner.
- **Usage**: `!restart`
- **Example**:
  - `!restart`  
  Restarts the bot (only accessible to the bot owner).

---

## **How to Set Up the Bot**

1. **Clone or Download the Code**:  
   Download the bot’s Python script.

2. **Install Dependencies**:  
   Install required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the `.env` File**:  
   Set up the environment variables in the `.env` file with the following keys:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   NEWS_API_KEY=your_news_api_key
   UPDATE_CHANNEL_ID=your_discord_channel_id
   AUTHORIZED_USER_IDS=user_ids_separated_by_commas
   AUTHORIZED_ROLES=role_names_separated_by_commas
   BOT_OWNER_ID=your_discord_id
   ```

4. **Run the Bot**:  
   Run the bot with:
   ```bash
   python bot.py
   ```

---

## **Common Errors & Troubleshooting**

### **Error**: `MissingRequiredArgument: symbol is a required argument that is missing`
- **Cause**: The `!watchlist` command requires a stock symbol or the `view` keyword to view the watchlist.
- **Solution**: Make sure you provide a symbol when adding a stock or use `!watchlist view` to view the list.

### **Error**: `CommandNotFound: Command 'XYZ' is not found`
- **Cause**: The command might not be defined properly or could be missing in the code.
- **Solution**: Ensure that the command is defined with the correct name and is loaded properly by the bot.

---

## **Notes**

- **Environment Variables**: The bot relies on environment variables for security (e.g., API keys, bot token). Ensure these are properly set in the `.env` file.
- **API Limits**: The Alpha Vantage API has a limit on the number of free requests per minute. If you hit this limit, you may need to wait before making more requests or consider upgrading to a paid API plan.
- **Command Permissions**: Some commands are restricted based on roles (e.g., `!adminonly`, `!botowner`, `!restricted`). Ensure your Discord roles and permissions are correctly configured.

---

Let me know if you need more clarification or further improvements!