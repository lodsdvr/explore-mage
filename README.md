## What is it?

This is a demo repository of my first experience with Mage. Based from the official documentation [here](http://docs.mage.ai/guides/load-api-data).

This pulls data from an API, transforms it with Mage, and writes it to a local DuckDB database.

**Main Consideration/s:**
  * Since it was specified to use a modern data orchestration tool, I took the liberty and explored mage.ai since I haven't tried any of the mentioned tools in the coding assignment.

## How can I get started?

1. Be sure git and Docker is installed and running, then run the following command:

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
copy dev.env .env
del dev.env
docker compose up
```
2. Ensure the docker container is running either in the Docker Desktop or the terminal where you run the command above.

### ❗⚠️ Had to install a 3rd party dependency manually in the docker container since the requirements file doesn't seem to work ⚠️❗

***Open another command prompt and follow below***

Windows:
```bash
docker exec -it ota-etl-test-magic-1 bash
```
***This will enter command line of the environment***
```bash
cd etl-test
pip install -r requirements.txt
```
***Wait until it finishes installation before proceeding with the next steps below***

3. Open http://localhost:6789 in your local web browser, you will land in the Pipelines screen.
4. Click the api_to_duck_db name link, it will lead you to the Triggers screen.
5. Click the Run@once button, wait for the run to be completed successfully.
6. Hover on the left menu icons, click Edit pipeline (</> icon).
7. It shows all the blocks of the pipeline, click the last block (named as 'data_profiling') on the tree on the right pane.
8. You will be directed to the code block for it and just click the Play button to execute it.
9. Wait and it will output the data profiling report.

## Technologies used
* mage.ai
  * python and sql scripting within
  * orchestration
* duckdb
* docker
* ydata-profiling

## Answers to the questions (all taken from the data profiling report)

a. The top 5 most common values in a particular column and what is their frequency
   * column 'country_region': ![image](https://github.com/lodsdvr/explore-mage/assets/163092895/91d31ee5-013a-4322-8fe9-78cc44e200cd)

b. Particular metric change over time within the dataset **(Still WIP)** Will be using time-series analysis

c. A correlation between two specific columns
   * columns 'confirmed' and 'deaths' are highly correlated: ![image](https://github.com/lodsdvr/explore-mage/assets/163092895/91619310-1684-4175-81b1-f882fcbf82f6)
   * Mainly because deaths counts includes the confirmed counts.

