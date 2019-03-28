# -*- coding: utf-8 -*-

import os
from datetime import datetime

from pyathena import connect
from pyathena.pandas_cursor import PandasCursor

from ..util.s3_helpers import upload_to_s3


def query_appraiser(bucket, date):
    cursor = connect(
        s3_staging_dir="s3://aws-athena-query-results-230106788096-us-west-2",
        region_name="us-west-2",
        cursor_class=PandasCursor,
    ).cursor()

    date = datetime.strptime(date, "%Y-%m-%d")
    year = datetime.strftime(date, "%Y")
    month = datetime.strftime(date, "%m")
    day = datetime.strftime(date, "%d")

    data = cursor.execute(
        """
    SELECT vin, 
           dealer_id, 
           price,
           miles,
           year_is AS year,
           make,
           model,
           trim,
           state,
           city,
           zip,
           latitude,
           longitude
    FROM marketcheck.used_parquet
    WHERE year = %(year)s
      AND month = %(month)s
      AND day = %(day)s
      AND PRICE IS NOT NULL
      AND miles IS NOT NULL
      AND year_is IS NOT NULL
    """,
        {"year": year, "month": month, "day": day},
    ).as_pandas()
    data.to_csv("data.csv", index=False)
    prefix = f"appraiser/{year}-{month}-{day}/raw.csv"
    upload_to_s3(bucket, prefix, "data.csv")
    os.remove("data.csv")
    return f"{bucket}/{prefix}"
