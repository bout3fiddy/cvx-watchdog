import time
from typing import Any

from src.utils.contract_utils import init_contract
from brownie import network

from src.utils.network_utils import QUICKNODE

w3 = QUICKNODE["wss"]


def tx_resource_smart_contract_history():

    contract_addr: Any = "0x4e3FBD56CD56c3e72c1403e103b45Db9da5B9D2B"

    network.connect('mainnet')
    brownie_contract = init_contract(contract_addr)
    abi: Any = brownie_contract.abi
    contract = w3.eth.contract(
        address=contract_addr,
        abi=abi
    )
    event_filter = contract.events.Transfer.createFilter(
        fromBlock='pending'
    )

    while True:
        print(event_filter.get_new_entries())
        time.sleep(2)

    return


tx_resource_smart_contract_history()

