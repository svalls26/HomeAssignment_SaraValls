from var import GETBLOCK_API_KEY
from fastapi import HTTPException
from pydantic import BaseModel
from web3 import Web3
from main import app 

class BlockData(BaseModel):
    gasLimit: int
    gasUsed: int
    number: int
    difficulty: int
    totalDifficulty: int

@app.get("/blocks/{block_number}", response_model=BlockData)
async def get_blocks(block_number: int):
    eth_url = f'https://eth.getblock.io/{GETBLOCK_API_KEY}/mainnet/'
    w3 = Web3(Web3.HTTPProvider(eth_url))
    try:
        response = w3.eth.get_block(block_number)
    except:
        raise HTTPException(
            status_code=404,
            detail="Block number not found"
        )
    block_data = {"gasLimit": response['gasLimit'],
            "gasUsed": response['gasUsed'],
            "number": response['number'],
            "difficulty": response['difficulty'],
            "totalDifficulty": response['totalDifficulty']}
    return block_data