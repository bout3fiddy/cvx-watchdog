from brownie import network
from brownie.network.contract import Contract
from brownie.network.contract import ContractNotFound

from web3.exceptions import InvalidAddress

from src.utils.exceptions import NetworkNotConnected


def init_contract(address: str):

    if not network.is_connected():
        raise NetworkNotConnected

    if not address_is_contract(address):
        raise ContractNotFound

    try:
        contract = Contract(address_or_alias=address)
    except InvalidAddress:
        raise
    except Exception as e:
        print(e)
        contract = Contract.from_explorer(address=address)

    return contract


def address_is_contract(address: str) -> bool:
    return w3_infura.eth.getCode(address) > HexBytes(0)