✅ Solution: Use a "Trusted" Role Instead of Hardcoding User IDs

Instead of manually updating the bot's code every time, you can use Discord roles to manage permissions dynamically.
🔹 How It Works

    Create a "Trusted" role in Discord (e.g., "Premium" or "Verified").
    Assign this role to users who should have access.
    Modify the bot's code to check for this role instead of checking user IDs manually.
    When a user gains trust, just assign them the role instead of changing the code.

✅ Step-by-Step Implementation
1️⃣ Create a Role in Discord

    Open Server Settings > Roles > Create Role (e.g., "Trusted").
    Give the role no extra permissions (the bot will check for it).

2️⃣ Update Your Code to Use Role-Based Authorization

Replace your existing is_authorized(ctx) function with this version:

def is_authorized(ctx):
    """Check if the user has the 'Trusted' role."""
    trusted_role_name = "Trusted"  # Change this to your actual role name

    # Check if user has the role
    if any(role.name == trusted_role_name for role in ctx.author.roles):
        return True
    
    return False

3️⃣ Apply This Check to Restricted Commands

Now update your restricted commands (!set_alert, !remove_alert, !portfolio, etc.) to use role-based access.

@bot.command(name='set_alert', help='Set a price alert. Restricted to Trusted users.')
async def set_alert(ctx, asset: str, price: float):
    if not is_authorized(ctx):
        await ctx.send("🚫 You need the 'Trusted' role to set alerts.")
        return
    try:
        with open(ALERTS_FILE, "a") as f:
            f.write(f"{asset.upper()},{price},{ctx.author.id}\n")
        await ctx.send(f"🔔 Alert set for {asset.upper()} at **${price}**.")
        logger.info(f"Alert set for {asset.upper()} at ${price}")
    except Exception as e:
        await ctx.send(f"⚠️ Error setting alert for {asset}: {e}")
        logger.error(f"Error setting alert for {asset}: {e}")

Repeat the same authorization check for:

    !remove_alert
    !portfolio
    !watchlist
    !remove_watchlist

🔹 How This Fix Works

✅ No need to edit code every time when adding new trusted users.
✅ Admins can dynamically assign the "Trusted" role to users inside Discord.
✅ Scalable and flexible solution for managing access.
🚀 Next Steps

    Create the "Trusted" role in Discord.
    Update the code with the new is_authorized() function.
    Restart your bot:

    python bot.py

    Assign the "Trusted" role to a test user.
    Test the commands as an authorized and unauthorized user.

✅ Your bot now dynamically handles access based on roles! 🚀 Let me know if you need further refinements. 🔥
