#  Califronia Airbnb Data Analysis

## DATA225 project

In this project we are using **Amazon Web Service(AWS)** to perform ETL and data visualization.

For all the files we are uploading it to **Amazon S3 bucket** as s3 is like a data lake.

Using **Lambda** integration from S3 bucket to **Amazon Dynamodb** to store geojson file data.

Using **AWS Glue** we will be doing Extract Transform load (ETL) process on these files to store the clean data into **Amazon Redshift** data warehouse.

Finally, Using **AWS Quicksight** tool, will be doing data visualization from amazon redshift by writing sql queries.

![image](https://user-images.githubusercontent.com/60303995/117523472-5fe3e900-af6d-11eb-87ce-f621c0e844c9.png)


## Motivation

There are over 38300 Airbnb listings in California as of February,2021, which approximates to around 4 houses being rented per square mile. Airbnb has seen an exponential increase in the number of listings in California each year and has gained a lot of popularity. By analysing the number of listings and occupancy rates, we can understand demand rates and also provide metrics for people who would like to make an investment in Airbnb and rent out their properties. Previously collected data and reviews help understand how the occupancy rate can be increased.



