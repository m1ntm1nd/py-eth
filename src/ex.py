import os
import sys
import json 
from dotenv import dotenv_values
from web3 import Web3

from solc import compile_standard, install_solc



def compile_source_file(file_path):
    spec = {
        "language": "Solidity",
        "sources": {
            "file": {
                "urls": [
                    file_path
                ]
            }
        },
        "settings": {
            "optimizer": {
               "enabled": True
            },
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata", "evm.bytecode", "abi"
                    ]
                }
            }
        }
    }

    out = compile_standard(spec, allow_paths=".")

    return out


def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address


CURR_PATH = os.path.dirname(__file__)
env = dotenv_values(os.path.join(CURR_PATH, '../.env'))

node_provider = env['RPC_NODE_URL_LOCAL']

w3 = Web3(Web3.HTTPProvider(node_provider))    

contract_source_path = os.path.join(CURR_PATH, '../contracts/StoreVar.sol')
compiled_sol = compile_source_file(contract_source_path)

print(compiled_sol)