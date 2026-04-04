from web3 import Web3
import os

RPC_URL = os.getenv("WEB3_PROVIDER_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def get_web3():
    return w3