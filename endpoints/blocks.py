from var import GETBLOCK_API_KEY
from web3 import Web3
from main import app 


@app.get("/blocks/{block_number}")
async def get_blocks(block_number: int):
    eth_url = f'https://eth.getblock.io/{GETBLOCK_API_KEY}/mainnet/'
    w3 = Web3(Web3.HTTPProvider(eth_url))
    response = w3.eth.get_block(block_number)
    block_data = {"gasLimit": response['gasLimit'],
            "gasUsed": response['gasUsed'],
            "number": response['number'],
            "difficulty": response['difficulty'],
            "totalDifficulty": response['totalDifficulty']}
    return block_data