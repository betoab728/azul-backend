import os
from web3 import Web3
from app.infrastructure.blockchain.web3_client import get_web3

w3 = get_web3()

contract_address = Web3.to_checksum_address(
    "0xc14f142CC462C73CB165F5A22570b33DF35aF5C0"
)

# ABI (copia desde Remix)
abi = [
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_idOrden",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_hash",
        "type": "string"
      }
    ],
    "name": "guardarRegistro",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "internalType": "string",
        "name": "idOrden",
        "type": "string"
      },
      {
        "indexed": False,
        "internalType": "string",
        "name": "hash",
        "type": "string"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "name": "HashRegistrado",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_idOrden",
        "type": "string"
      }
    ],
    "name": "obtenerRegistros",
    "outputs": [
      {
        "components": [
          {
            "internalType": "string",
            "name": "hash",
            "type": "string"
          },
          {
            "internalType": "uint256",
            "name": "timestamp",
            "type": "uint256"
          }
        ],
        "internalType": "struct Trazabilidad.Registro[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]

contract = w3.eth.contract(address=contract_address, abi=abi)
# Obtener account de forma segura
def get_account():
    private_key = os.getenv("PRIVATE_KEY")

    if not private_key:
        raise ValueError("❌ PRIVATE_KEY no definida en variables de entorno")

    if not private_key.startswith("0x"):
        private_key = "0x" + private_key  # asegurar formato

    return w3.eth.account.from_key(private_key), private_key


def guardar_hash_blockchain(id_orden: str, hash_value: str):

    account, private_key = get_account()

    nonce = w3.eth.get_transaction_count(account.address, 'pending')

    tx = contract.functions.guardarRegistro(
        id_orden,
        hash_value
    ).build_transaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)

    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return {
        "tx_hash": tx_hash.hex(),
        "blockNumber": receipt.blockNumber,
        "status": receipt.status
    }