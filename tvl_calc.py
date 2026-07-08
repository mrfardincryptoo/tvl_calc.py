# Aggregate Total Value Locked (TVL) across multiple protocol pools
def calculate_total_tvl(protocol_pools):
    total_tvl = sum(pool["balance"] * pool["token_price"] for pool in protocol_pools)
    return total_tvl

active_pools = [
    {"name": "ETH-USDC", "balance": 150, "token_price": 3400},
    {"name": "WBTC-USDT", "balance": 12, "token_price": 62000},
    {"name": "LINK-POOL", "balance": 5000, "token_price": 15}
]

current_tvl = calculate_total_tvl(active_pools)
print(f"Protocol Total Value Locked (TVL): ${current_tvl:,.2f} USD")
