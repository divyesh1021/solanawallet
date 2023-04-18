from solana.rpc.api import Client
# from solana.publickey import PublicKey
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.rpc.types import TxOpts
from solana.transaction import Transaction
from solders.keypair import Keypair
from solders.pubkey import Pubkey
# from solana

# Connect to the devnet
solana_client = Client("https://api.devnet.solana.com")

keypair = Keypair()
print("Private_key------>>>>>>>>:",keypair)
pub = keypair.pubkey()
print("PUBLIC)_KEY----->>>>>>>:",pub)

symbol = "MYTOKEN"
name = "My Token"
decimals = 2
initial_supply = 1000000

# Create the token account
# token_account, _ = solana_client.get_new_account()
# token_mint:Token.create_mint(
#     solana_client,  # Solana client
#     pub,  # Mint authority
#     decimals,  # Decimals
#     symbol,  # Symbol
#     name,  # Name
# )

# Mint the initial supply
# mint_authority = solana_client.get_account_info(token_mint.mint_authority)["key"]
# token_mint.mint_to(
#     mint_authority,  # Mint authority
#     pub,  # Destination account
#     initial_supply,  # Amount
# )


# pub_key:6PDKvywAUpJV8HiqtoBidJQoXn2qgDkJNACg1BTqjSdb