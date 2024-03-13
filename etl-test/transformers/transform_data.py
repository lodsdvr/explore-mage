def drop_column(df, column_name):
    return df.drop(columns=column_name)


def clean_column(column_name):
    return column_name.lower().replace(' ', '_')


@transformer
def transform(df, *args, **kwargs):

    # Drop columns that are discontinued or not needed
    #  'Recovered' and 'Active' are discontinued since August 2021
    df = drop_column(df, ['Recovered', 'Active'])

    # Clean column names
    df.columns = [clean_column(col) for col in df.columns]

    return df


@test
def test_number_of_columns(df, *args) -> None:
    assert len(df.columns) >= 12, 'There needs to be at least 12 columns.'