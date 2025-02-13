import unittest
from unittest.mock import patch, AsyncMock, MagicMock
import os
import sys
import requests
import yfinance as yf
import pandas as pd
import io
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Import functions from your bot file
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from financial_bot import (  # Change 'bot' to the new filename
    get_stock_price, get_crypto_price, is_authorized, is_bot_owner,
    bot, watchlist, set_alert, remove_alert, portfolio, stock, crypto
)
class TestBotFunctions(unittest.TestCase):

    @patch("requests.get")
    def test_get_stock_price_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "Global Quote": {
                "05. price": "150.00"
            }
        }
        mock_get.return_value = mock_response

        price = get_stock_price("AAPL")
        self.assertEqual(price, "150.00")

    @patch("requests.get")
    def test_get_stock_price_fail(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException
        price = get_stock_price("AAPL")
        self.assertEqual(price, "⚠️ Error fetching stock price")

    @patch("requests.get")
    def test_get_crypto_price_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"bitcoin": {"usd": 45000}}
        mock_get.return_value = mock_response

        price = get_crypto_price("bitcoin")
        self.assertEqual(price, 45000)

    @patch("requests.get")
    def test_get_crypto_price_fail(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        price = get_crypto_price("bitcoin")
        self.assertEqual(price, "N/A")

    def test_is_authorized_true(self):
        mock_ctx = MagicMock()
        mock_ctx.author.id = 123456789
        authorized_users = [123456789, 987654321]

        with patch("financial_bot.AUTHORIZED_USER_IDS", authorized_users):
            self.assertTrue(is_authorized(mock_ctx))

    def test_is_authorized_false(self):
        mock_ctx = MagicMock()
        mock_ctx.author.id = 111111111
        authorized_users = [123456789, 987654321]

        with patch("financial_bot.AUTHORIZED_USER_IDS", authorized_users):
            self.assertFalse(is_authorized(mock_ctx))

    def test_is_bot_owner_true(self):
        mock_ctx = MagicMock()
        mock_ctx.author.id = "123456789"

        with patch("financial_bot.BOT_OWNER_ID", "123456789"):
            self.assertTrue(is_bot_owner(mock_ctx))

    def test_is_bot_owner_false(self):
        mock_ctx = MagicMock()
        mock_ctx.author.id = "111111111"

        with patch("financial_bot.BOT_OWNER_ID", "123456789"):
            self.assertFalse(is_bot_owner(mock_ctx))

class TestBotCommands(unittest.IsolatedAsyncioTestCase):

    async def test_stock_command(self):
        mock_ctx = MagicMock()
        mock_ctx.send = AsyncMock()

        with patch("bot.get_stock_price", return_value="150.00"):
            await stock(mock_ctx, "AAPL")
            mock_ctx.send.assert_called_once()
        call_args = mock_ctx.send.call_args[0][0]
        assert "AAPL" in call_args and "$150.00" in call_args



async def test_crypto_command(self):
    mock_ctx = MagicMock()
    mock_ctx.send = AsyncMock()

    with patch("bot.get_crypto_price", return_value="45000"):
        await crypto(mock_ctx, "bitcoin")
        mock_ctx.send.assert_called_once()
        call_args = mock_ctx.send.call_args[0][0]
        assert "Bitcoin" in call_args and "$45000 USD" in call_args

    async def test_watchlist_add(self):
        mock_ctx = MagicMock()
        mock_ctx.send = AsyncMock()

        with patch("bot.is_authorized", return_value=True):  # Make user authorized
            await watchlist(mock_ctx, "AAPL")    
            mock_ctx.send.assert_called_with("🔔None AAPL added to your watchlist!")

    async def test_set_alert(self):
        mock_ctx = MagicMock()
        mock_ctx.author.id = 123456789
        mock_ctx.send = AsyncMock()

        with patch("builtins.open", new_callable=unittest.mock.mock_open()), patch("bot.is_authorized", return_value=True):
            await set_alert(mock_ctx, "AAPL", 150.00)
            mock_ctx.send.assert_called_once()
            call_args = mock_ctx.send.call_args[0][0]
        assert "Alert set for AAPL" in call_args and "$150.0" in call_args


    async def test_remove_alert(self):
        mock_ctx = MagicMock()
        mock_ctx.author.id = 123456789
        mock_ctx.send = AsyncMock()

        with patch("builtins.open", new_callable=unittest.mock.mock_open(read_data="AAPL,150.0,123456789\n")), patch("financial_bot.is_authorized", return_value=True):
            await remove_alert(mock_ctx, "AAPL")
            mock_ctx.send.assert_called_with("❌ None Alert removed for AAPL.")

    async def test_portfolio(self):
        mock_ctx = MagicMock()
        mock_ctx.send = AsyncMock()

        with patch("financial_bot.get_stock_price", return_value="150.00"), patch("financial_bot.is_authorized", return_value=True):
            await portfolio(mock_ctx, "AAPL", "2")
            mock_ctx.send.assert_called_with("📊 **Your Portfolio**:\n📈 AAPL: 2 shares, $150.00 each, Total: $300.00\n\n💰 **Total Portfolio Value**: $300.00")

if __name__ == "__main__":
    unittest.main()
