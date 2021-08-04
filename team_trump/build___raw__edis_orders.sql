CREATE EXTENSION IF NOT EXISTS aws_commons CASCADE;

CREATE SCHEMA IF NOT EXISTS raw___ad;

DROP TABLE IF EXISTS raw___ad.itc_orders;

CREATE TABLE IF NOT EXISTS raw___ad.itc_orders (
    order_date text
    , continued_date text
    , itc_case_number text
    , doc_case_number text
    , ad_cvd text
    , review_sequence_group_number text
    , product_group text
    , product text
    , country text
    , column2 text
    , column3 text
    , fed_reg text
    , pub_date text
    , link text
    , column1 text
    , column12 text
);

WITH s3_info AS (
    SELECT
        aws_commons.create_s3_uri ('wt-gc-m'
            , 'edis_orders_itc.csv'
            , 'ap-northeast-2') AS uri
        , aws_commons.create_aws_credentials ('AKIATHBCLRR3ZK5O6TGW'
            , 'f3icJzObixzX+04VHpakrlG+DZ7f8yTC1e92Atag'
            , NULL) AS cred
)
SELECT
    aws_s3.table_import_from_s3 ('raw___ad.itc_orders' , '' , '(format csv, header)' , uri , cred)
FROM
    s3_info;

SELECT
    *
FROM
    raw___ad.itc_orders;

