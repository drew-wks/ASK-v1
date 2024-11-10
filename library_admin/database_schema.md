# Example Qdrant Record Object

- In this version of code, each record receives its structure from `langchain.docstore.document.Document`, which was produced by LangChain's PyPDF Loader. 
```python
[
    Document(
        page_content="",   # Required
        metadata={} # Optional
    ),
]
```
- PDFs are chunked into record (i.e., "points" in Qdrant) using Langchain's text_splitter.split_documents(pages)
- Each chunk is one PDF page
- LangChain text_splitter ( I think) adds the metadata dictionary and the Qdrant vectorstore places it inside the qdrant payload dictionary so a key would be accessed `key = metadata.page`
- Qdrant inserts the id.

Result were generated using Qdrantclient
`result=client.scroll`
`print(results[0])`

## Gen 1

- This particular document has since been removed from the library
```python
[Record(
    id='c83aa737-4348-44fa-9d51-0ca6c71ec814', 
    payload={
        'page_content': 'goes here', 
        'metadata': {
            'source': './raw_pdfs/USCG_Addendum_to_US_NSS_to_IAMSAR-CI_16130_2G-2022-10-01.pdf', 
            'page': 0, 
            }
        }, 
    vector=None, 
    shard_key=None, 
    order_value=0),
]
``` 