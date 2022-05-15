import os
import sys
import json 
from dotenv import dotenv_values
from web3 import Web3

from solc import compile_source

CURR_PATH = os.path.dirname(__file__)
env = dotenv_values(os.path.join(CURR_PATH, '../.env'))

node_provider = env['RPC_NODE_URL_LOCAL']

w3 = Web3(Web3.HTTPProvider(node_provider))    





def main():
    


    return 0



def compile_source(file_path):
    with open(file_path, 'r') as f:
        source = f.read()

    return compile_source(source)

def transferETH(senderAddr, receiverAddr, signature, amountEth):
    transaction_body = {
        'nonce':None,
        'to':receiverAddr,
        'value':None,
        'gas':None,
        'gasPrice':None
    }

    #signed_transaction = w3.eth.account.sign_transaction

def configure():
    os.environ['PYTHONWARNINGS'] = 'default'

def connectionCheck():
    status = w3.isConnected()
    return status


if __name__ == '__main__':
    configure()
    assert connectionCheck() == True, f'Connection is not established'
    status = main()