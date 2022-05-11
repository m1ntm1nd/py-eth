import os
import json 
from dotenv import dotenv_values
from web3 import Web3

CURR_PATH = os.path.dirname(__file__)
env = dotenv_values(os.path.join(CURR_PATH, '.env'))

node_provider = env['RPC_NODE_URL_LOCAL']

w3 = Web3(Web3.HTTPProvider(node_provider))    


def main():
    block = w3.eth.get_block('latest')

    acc0 = w3.eth.accounts[0]
    bal = w3.eth.get_balance(acc0)
    print(bal)
    return None
    

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