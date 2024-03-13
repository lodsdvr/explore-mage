## What is it?

This is a demo repository of my first experience with Mage. Based from the official documentation [here](http://docs.mage.ai/guides/load-api-data).

This pulls data from an API, transforms it with Mage, and writes it to a local DuckDB database.

## How can I get started?

First, be sure Docker is installed and running, then run the following command:

Mac/Linux:

```bash
git clone https://github.com/lodsdvr/explore-mage ota-etl-test \
&& cd ota-etl-test \
&& cp dev.env .env && rm dev.env \
&& docker compose up
```

Windows:

```bash
git clone https://github.com/lodsdvr/explore-mage ota-etl-test
cd ota-etl-test
cp dev.env .env
rm dev.env
docker compose up
```
