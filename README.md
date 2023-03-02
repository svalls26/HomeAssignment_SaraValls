## Home Assignment - Sara Valls


This project is made to satisfy the requirements of the Homework assignment. The project is composed by different parts with the porpouse of develop a small service that exposes the following two endpoints:

* blocks/{blocks_number: integer}[GET]
* signatures/{signature: string}[GET]

The first endpoint communicates with a sample free node from <href>https://account.getblock.io</href>, and retrieve information about the given node.

The second endpoint connects with <href>https://www.4byte.directory</href> and provides the functions name associated by the given signature.

The framework used for the development is <a href="https://fastapi.tiangolo.com" target="_top">FastAPI</a>.

## How it works

First step is making avaiable the libraries used in the development in our environment by: 

```
pip install -r requirements.txt
```

(Notice that sometimes the version of pip requires pip3 instead of pip)

The next step is running the following command inside app folder:
```
python -m uvicorn main:app
```

Once the last step is done, the API will be working and the endpoints will be ready to use.
To see the documentation: 
```
/docs
```
