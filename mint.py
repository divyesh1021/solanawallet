from solders.keypair import Keypair
# keypair = Keypair()
# print()

secret_key = [234,211,171,167,254,51,25,150,65,81,191,94,119,62,
            233,63,113,6,185,95,57,227,70,63,91,92,227,9,80,191,191,28,79,251,
            38,97,156,86,175,117,40,57,147,16,6,35,122,243,150,58,230,135,90,93,
            222,191,202,95,200,106,245,83,0,30]
keypair = Keypair.from_bytes(secret_key)
print("pub_key:{}".format(keypair.pubkey()))