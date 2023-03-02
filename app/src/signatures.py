from var import SIGNATURES_URL_PROVIDER
from fastapi import HTTPException
from pydantic import BaseModel
from main import app
import requests

class SignatureData(BaseModel):
    data: list
    page_size: int
    is_last_page: bool

@app.get("/signatures/{hex_signature}", response_model=SignatureData)
async def get_signatures(hex_signature: str, page_number: int = 1, page_size: int = 10):
    r = requests.get(f'https://{SIGNATURES_URL_PROVIDER}/signatures?hex_signature={hex_signature}') 
    r_json = r.json()['results']
    list_function = []
    for i in range(len(r_json)):
        list_function.append({"name":r_json[i]['text_signature'].split('(', 1)[0]})
    
    start = (page_number - 1) * page_size
    end = start + page_size

    if end >= len(list_function):
        last_page = True
    else:
        last_page = False

    return {
        "data": list_function[start:end],
        "page_size": len(list_function[start:end]),
        "is_last_page": last_page
    }