# aip-client

The aip-client provides a implementation of the Copernicus Space Component Long Term Archive Interface in Python. So it's easy to search, download and trigger offline retrieval of products from the Archive Interface delivery Point (AIP). 

The [sentinelsat](https://github.com/sentinelsat/sentinelsat) library offers such a functionality for Copernicus Open Access Hubs. The aip-client therefore uses sentinelsat and extends it for AIP.

## Installation

The aip-client is currently not provided via pip. So you have to clone this repository and install it with the `setup.py`.

```BASH
git clone https://github.com/markus-kunze/aip-client.git
cd aip-client
sudo python setup.py install
```

## Usage

```PYTHON
from aip_client import AIPClient

client = AIPClient('user', 'password', "url")

# Query products
query_result = client.query(query="ContentLength lt 550000")
```

## Examples

Import and instantiate AIPClient (required for further examples)

```PYTHON
from aip_client import AIPClient
client = AIPClient('user', 'password', "url")
```

Set logging level

```PYTHON
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
```

Configure checksum comparison

```PYTHON
client.downloader.verify_md5_dl = True # Calculates the checksum during the download and compares it after completion without re-reading the file.
client.downloader.verify_checksum = True # Calculates the checksum after the download and requires re-reading
```

Query with string

```PYTHON
query = "ContentLength lt 550000"
query_result = client.query(query)
```

Inspect a product by UUID

```PYTHON
inspect_result = client.inspect_product("173c2e04-6e06-30c1-a364-011e68bc4fad")
```

Download of a single product including:

* Trigger retrieval of products if offline
* Wait until product is online available
* Checksum check
* Files are first saved with `.incomplete` until the download is finished
* If the file is already available in the destination directory the download is skipped

```PYTHON
dl_result = client.download("173c2e04-6e06-30c1-a364-011e68bc4fad")
```

Download a list of products

```PYTHON
query_result = client.query("ContentLength lt 550000")
dl_all_result = client.download_all(products=query_result)
```

Manual bulk handling

```PYTHON
# Create bulk
query = "ContentLength lt 550000"
bulk_result = client.bulk_create(query, batch_size_volume=10000000000, batch_size_products=10)
bulk_id = bulk_result["Id"]

# Inspect bulk
# bulk_inspect_result = client.bulk_inspect(bulk_id=bulk_id)

bulk_ls_batches_result = client.bulk_ls_batches(bulk_id=bulk_id)

for batch in bulk_ls_batches_result:
    batch_id = batch["Id"]
    
    # Inspect batch
    # batch_order_inspect_result = api.batch_order_inspect(batch_id=batch_id)
    
    # List products of batch
    # batch_order_ls_products_result = client.batch_order_ls_products(batch_id=batch_id)

    client.batch_order_trigger(batch_id=batch_id)
    client.batch_order_wait_completed(batch_id=batch_id)  
    client.batch_order_products_download(batch_id=batch_id)
```

Automated bulk handling

```PYTHON
client.bulk_auto_download(query="ContentLength lt 550000", batch_size_products=20, batch_size_volume=1000000000)
```

## Credits

* The aip-client is an extension of [sentinelsat](https://github.com/sentinelsat/sentinelsat)