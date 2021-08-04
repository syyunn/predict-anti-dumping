CREATE EXTENSION IF NOT EXISTS aws_commons CASCADE;

CREATE SCHEMA IF NOT EXISTS raw___ad;

DROP TABLE IF EXISTS raw___ad.us_imposed;

CREATE TABLE IF NOT EXISTS raw___ad.us_imposed (
    hs text
    , hs_ordi smallint
    , initiation_date smallint
    , initiation_month smallint
    , initiation_year smallint
    , measure_description text
    , member_imposing text
    , partner_affected text
    , product_description text
);

WITH s3_info AS (
    SELECT
        aws_commons.create_s3_uri ('wt-gc-m'
            , 'us-imposed-anti-dumpings.csv'
            , 'ap-northeast-2') AS uri
        , aws_commons.create_aws_credentials ('AKIATHBCLRR3ZK5O6TGW'
            , 'f3icJzObixzX+04VHpakrlG+DZ7f8yTC1e92Atag'
            , NULL) AS cred
)
SELECT
    aws_s3.table_import_from_s3 ('raw___ad.us_imposed' , '' , '(format csv, header)' , uri , cred)
FROM
    s3_info;

SELECT
    *
FROM
    raw___ad.us_imposed;

