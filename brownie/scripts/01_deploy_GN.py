import os
from dotenv import dotenv_values
from brownie import Wei, accounts, Guess_number

CURR_PATH = os.path.dirname(__file__)
env = dotenv_values(os.path.join(CURR_PATH, '../../.env'))

def main():
    deployer = accounts.add(env['PRIVATE_KEY'])
    transaction_details = {
        'from' : deployer,
        'value' : Wei('10 ether')
    }

    Contract_GN = Guess_number.deploy(999, transaction_details)

    return Contract_GN