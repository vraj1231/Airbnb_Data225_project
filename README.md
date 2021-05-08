# Airbnb Data Analysis

## DATA225 project

In this project we are using **Amazon Web Service(AWS)** to perform ETL and data visualization.

For the listing files and review files we are uploading it to **Amazon S3 bucket** as csv format, while for the geojson files we will be using **Amazon Dynamodb** to store the data.

Using **AWS Glue** we will be doing Extract Transform load (ETL) process on these files to store the clean data into **Amazon Redshift** data warehouse.

Using copy commands, we will be importing data from Dynamodb to Amazon Redshift.

Finally, Using **AWS Quicksight** tool, will be doing data visualization from amazon redshift by writing sql queries.

![image](https://user-images.githubusercontent.com/60303995/117522064-13e17600-af66-11eb-8fbe-f2010ee6111d.png)

