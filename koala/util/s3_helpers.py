# -*- coding: utf-8 -*-

import boto3


def download_from_s3(bucket, key, filename):
    s3 = boto3.client("s3")
    with open(filename, "wb") as data:
        s3.download_fileobj(bucket, key, data)


def upload_to_s3(bucket, key, filename):
    s3 = boto3.client("s3")
    with open(filename, "rb") as data:
        s3.upload_fileobj(data, bucket, key)
