from solders.keypair import Keypair
# from Solana import LAMPORTS_PER_SOL
# from Solana import Connection
# import * as fs from 'fs';
# from fs import *
import solana.rpc.api as rpc_api
# from solana.keypair import Keypair
# from solana.publickey import PublicKey
from solana.rpc.commitment import Confirmed
from solana.transaction import Transaction
from spl.token.client import Token




# keypair = Keypair()
# print("Private_key------>>>>>>>>:",keypair)
# pub = keypair.pubkey()
# print("PUBLIC)_KEY----->>>>>>>:",pub)

# CjFsh3aHd5hdJ9cKeT8EbonTGsBvKN9393u2yKgX5CTz
# STEP 1 - Connect to Solana Network
# endpoint = 'https://cosmological-thrumming-market.solana-devnet.discover.quiknode.pro/1f9b28827e0c51a0d021a6d801399c4527db696a/'
# solanaConnection = Connection(endpoint)


def main():

    connection = rpc_api.Client("https://cosmological-thrumming-market.solana-devnet.discover.quiknode.pro/1f9b28827e0c51a0d021a6d801399c4527db696a/", commitment=Confirmed)

    keypair = Keypair()

    print('private key=========',keypair)
    private_keypair = keypair.pubkey()
    # public_key = str(private_keypair)    
    print('public key -----',private_keypair)

    from_airdrop_signature = connection.request_airdrop(private_keypair, 1000000000)



    to_wallet = Keypair()
    print('private key=========',to_wallet)
    to_private_keypair = to_wallet.pubkey()
    to_public_key = str(to_private_keypair)    
    print('public key -----',to_public_key)

    connection.confirm_transaction(from_airdrop_signature)


    mint = Token.create_mint(
        connection,
        keypair,
        private_keypair,
        None,
        9,
        Token.TOKEN_PROGRAM_ID
    )

    from_token_account = mint.get_or_create_associated_account_info(private_keypair)


    to_token_account = mint.get_or_create_associated_account_info(to_public_key)


    mint.mint_to(
        from_token_account.address,
        private_keypair,
        [],
        1000000000,
    )

    print("Minting complete!")

    transfer_instruction = Token.create_transfer_instruction(
        Token.TOKEN_PROGRAM_ID,
        from_token_account.address,
        to_token_account.address,
        private_keypair,
        [],
        1,
    )
    transaction = Transaction().add(transfer_instruction)

    # Sign transaction, broadcast, and confirm
    transaction.sign([keypair])
    tx_sig = connection.send_transaction(transaction)
    connection.confirm_transaction(tx_sig)

    print(tx_sig)

main()
    # STEP 2 - Generate a New Solana Wallet

    

# STEP 3 - Airdrop 1 SOL to new wallet

# async def Mint():
#     airdropSignature = solanaConnection.requestAirdrop(p,LAMPORTS_PER_SOL)
#     try:
#         txId = await airdropSignature
#         print('Airdrop Transaction Id:', txId)
#         print(f"https://explorer.solana.com/tx/${txId}?cluster=devnet")
#     except:
#         print('some isuess')


# secret_key=[234,211,171,167,254,51,25,150,65,81,191,94,119,62,233,63,113,6,185,95,57,
#             227,70,63,91,92,227,9,80,191,191,28,79,251,38,97,156,86,175,117,40,57,147,
#             16,6,35,122,243,150,58,230,135,90,93,222,191,202,95,200,106,245,83,0,30]

# keypair = Keypair.from_bytes(secret_key)
# print("Created Keypair with Public Key: {}".format(keypair.pubkey()))


# new_keypair = str(keypair)
# b58_string = new_keypair
# keypair = Keypair.from_base58_string(b58_string)
# print("Created Keypair with Public Key: {}".format(keypair.pubkey()))


# keypair = Keypair()
# while(str(keypair.pubkey())[:5]!="elv1s") :
#     keypair = Keypair()

# print(keypair)

# 5mXvS1nSJExEVLsJv6KejatEguRFJh9oDgpwCBPTU781eBqdb7V4HdkJV8JZQzn4t56W9a2Zf7HGZifobPPZ9dCs


# 6MfM1mY9ChJvmtMB5pA87SaATkPXwN7EXdPCK6QtibTB