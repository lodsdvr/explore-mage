if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import ydata_profiling as profiler

@custom
def transform_custom(df, *args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        the profiler report as a notebook iframe
    """
    # Using ydata_profiling to do EDA
    profile = profiler.ProfileReport(df).to_notebook_iframe()
    
    return profile