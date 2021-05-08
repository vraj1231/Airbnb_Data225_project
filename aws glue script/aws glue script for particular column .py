#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "airbnb_db225", table_name = "listings_la_csv", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "airbnb_db225", table_name = "listings_la_csv", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("id", "long", "id", "long"), ("name", "string", "name", "string"), ("host_id", "long", "host_id", "long"), ("host_name", "string", "host_name", "string"), ("neighbourhood", "string", "neighbourhood", "string"), ("latitude", "double", "latitude", "double"), ("longitude", "double", "longitude", "double"), ("room_type", "string", "room_type", "string"), ("price", "long", "price", "long"), ("minimum_nights", "long", "minimum_nights", "long"), ("number_of_reviews", "long", "number_of_reviews", "long"), ("last_review", "string", "last_review", "string"), ("reviews_per_month", "double", "reviews_per_month", "double"), ("calculated_host_listings_count", "long", "calculated_host_listings_count", "long"), ("availability_365", "long", "availability_365", "long")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("id", "long", "id", "long"), ("name", "string", "name", "string"), ("host_id", "long", "host_id", "long"), ("host_name", "string", "host_name", "string"), ("neighbourhood", "string", "neighbourhood", "string"), ("latitude", "double", "latitude", "double"), ("longitude", "double", "longitude", "double"), ("room_type", "string", "room_type", "string"), ("price", "long", "price", "long"), ("minimum_nights", "long", "minimum_nights", "long"), ("number_of_reviews", "long", "number_of_reviews", "long"), ("last_review", "string", "last_review", "string"), ("reviews_per_month", "double", "reviews_per_month", "double"), ("calculated_host_listings_count", "long", "calculated_host_listings_count", "long"), ("availability_365", "long", "availability_365", "long")], transformation_ctx = "applymapping1")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice2"]
## @return: resolvechoice2
## @inputs: [frame = applymapping1]
resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_cols", transformation_ctx = "resolvechoice2")
## @type: DropNullFields
## @args: [transformation_ctx = "dropnullfields3"]
## @return: dropnullfields3
## @inputs: [frame = resolvechoice2]
dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")

#dropping null values from the dataframe
df = dropnullfields3.toDF()
df = df.na.drop('any')

df.show()
#dropping duplicates from the dataframe
df_dropped_duplicates = df.distinct()

df_dropped_duplicates.show()
#all lowercase value from host_name column
from pyspark.sql.functions import lower, col

df_dropped_duplicates_lowered = df_dropped_duplicates.select(lower(df_dropped_duplicates.host_name))

#formatting date in column last_review
from pyspark.sql.functions import to_date
df_formatted = df_dropped_dulpicates_lowered.select(to_date(df_dropped_dulpicates_lowered.last_review, 'mm-dd-yyyy'))

df_formatted.show()
#converting back to glue standard frame
df2 = DynamicFrame.fromDF(df_formatted, glueContext, 'df2')

## @type: DataSink
## @args: [catalog_connection = "redshift_conn", connection_options = {"dbtable": "listings_la_csv", "database": "dev"}, redshift_tmp_dir = TempDir, transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]
#datasink4 = glueContext.write_dynamic_frame.from_jdbc_conf(frame = df2, catalog_connection = "redshift_conn", connection_options = {"dbtable": "listings_la_csv", "database": "dev"}, redshift_tmp_dir = args["TempDir"], transformation_ctx = "datasink4")
job.commit()

