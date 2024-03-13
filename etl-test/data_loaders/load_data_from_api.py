import io
import pandas as pd
import requests


@data_loader
def load_data_from_api(*args, **kwargs):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-09-2023.csv'
    response = requests.get(url)
    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_row_count(df, *args) -> None:
    assert len(df.index) != 0, 'No rows to load.'