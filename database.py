from sqlalchemy import create_engine, text

productdb = create_engine(
    "mysql+pymysql://2qFsVSFAe2DfpMX.root:1I8dZWlcgKaXxeJ4@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/perfume_product_db",
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/certs/ca-certificates.crt"
        }
    }
)
