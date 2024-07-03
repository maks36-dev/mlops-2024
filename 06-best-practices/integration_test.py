import os
import pandas as pd
from datetime import datetime


def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


def create_test_data(year, month):

    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = ['PULocationID', 'DOLocationID',
               'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df_input = pd.DataFrame(data, columns=columns)

    input_file = os.getenv('INPUT_FILE_PATTERN').format(year=year, month=month)
    options = {
        'client_kwargs': {
            'endpoint_url': os.getenv('S3_ENDPOINT_URL')
        }
    }

    df_input.to_parquet(
        input_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )


def run_batch_script():
    os.system('python batch.py 2023 1')


def verify_output(year, month):
    output_file = os.getenv('OUTPUT_FILE_PATTERN').format(year=year, month=month)
    options = {
        'client_kwargs': {
            'endpoint_url': os.getenv('S3_ENDPOINT_URL')
        }
    }

    df_result = pd.read_parquet(output_file, storage_options=options)
    print("Sum of predicted durations:", df_result['predicted_duration'].sum())


if __name__ == "__main__":
    create_test_data(2023, 1)
    run_batch_script()
    verify_output(2023, 1)
