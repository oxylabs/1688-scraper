# 1688 Scraper API

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

Oxylabs' [1688 Scraper](https://oxylabs.io/products/scraper-api/ecommerce/1688?utm_source=github&utm_medium=repositories&utm_campaign=product) is a data gathering solution allowing you to extract real-time information from an 1688 website effortlessly. This brief guide showcases how 1688 Scraper works, along with code examples to help you better understand how to use it hassle-free.

### How it works

You can get 1688 results by providing your own URLs to our service. We can return the HTML for any page you like.

#### Python code example

The example below illustrates how you can get HTML of 1688 page.

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'universal',
    'url': 'https://fuzhuang.1688.com/nanzhuang?spm=a260k.dacugeneral.home2019category.2.663335e4bwa222'
}

# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with the result.
pprint(response.json())
```
Find code examples for other programming languages [**here**](https://github.com/oxylabs/1688-scraper/tree/main/code%20examples)

#### Output Example
```json
{
  "results": [
    {
      "content": "\r\n<!DOCTYPE html>\n<html>\n\n<head>\n  <link rel=\"dns-prefetch\" href=\"//polyfill.alicdn.com\">\n  <link re ... </html>",
      "created_at": "2024-02-20 12:15:04",
      "updated_at": "2024-02-20 12:15:08",
      "page": 1,
      "url": "https://fuzhuang.1688.com/nanzhuang?spm=a260k.dacugeneral.home2019category.2.663335e4bwa222",
      "job_id": "7165680254252520449",
      "status_code": 200
    }
  ]
}
```
Using our 1688 Scraper, you can easily harvest public data from any 1688 web page. Gather essential mobile phone data, such as price, reviews, or specific features, to monitor the market and outperform your competitors. If you require any assistance, connect with our support team through our live chat or email us at hello@oxylabs.io.
