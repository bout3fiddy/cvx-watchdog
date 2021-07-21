import os

import web3


QUICKNODE_KEY = os.environ["QUICKNODE_API_KEY"]
INFURA_KEY = os.environ["WEB3_INFURA_PROJECT_ID"]

INFURA = {
    "https": web3.Web3(
        web3.Web3.HTTPProvider(
            f"https://mainnet.infura.io/v3/{INFURA_KEY}",
        ),
    ),
    "wss": web3.Web3(
        web3.Web3.WebsocketProvider(
            f"wss://mainnet.infura.io/v3/{INFURA_KEY}",
        ),
    ),
}

QUICKNODE = {
    "https": web3.Web3(
        web3.Web3.HTTPProvider(
            f"wss://long-fragrant-violet.quiknode.pro/{QUICKNODE_KEY}"
        )
    ),
    "wss": web3.Web3(
        web3.Web3.WebsocketProvider(
            f"wss://long-fragrant-violet.quiknode.pro/{QUICKNODE_KEY}"
        )
    )
}
