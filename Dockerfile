# Use official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first


COPY requirements.txt .

# Install yfinance separately in case of issues
RUN pip install yfinance

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project (including bot folder)
COPY . .

# Set the entry point to run the bot
CMD ["python", "bot/financial_bot.py"]
