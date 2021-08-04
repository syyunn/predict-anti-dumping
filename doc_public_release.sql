CREATE EXTENSION IF NOT EXISTS aws_commons CASCADE;

CREATE SCHEMA IF NOT EXISTS raw___doc;

DROP TABLE IF EXISTS raw___doc.public_release;

CREATE TABLE IF NOT EXISTS raw___doc.public_release (
    date text
    , headline text
);

WITH s3_info AS (
    SELECT
        aws_commons.create_s3_uri ('wt-gc-m'
            , 'doc_public_release_headlines.csv'
            , 'ap-northeast-2') AS uri
        , aws_commons.create_aws_credentials ('AKIATHBCLRR3ZK5O6TGW'
            , 'f3icJzObixzX+04VHpakrlG+DZ7f8yTC1e92Atag'
            , NULL) AS cred
)
SELECT
    aws_s3.table_import_from_s3 ('raw___doc.public_release' , '' , '(format csv, header)' , uri , cred)
FROM
    s3_info;

SELECT
    *
FROM
   raw___doc.public_release;

