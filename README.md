#  Califronia Airbnb Data Analysis

## DATA225 project

In this project we are using **Amazon Web Service(AWS)** to perform ETL and data visualization.

For the listing files and review files we are uploading it to **Amazon S3 bucket** as csv format, while for the geojson files we will be using **Amazon Dynamodb** to store the data.

Using **AWS Glue** we will be doing Extract Transform load (ETL) process on these files to store the clean data into **Amazon Redshift** data warehouse.

Using copy commands, we will be importing data from Dynamodb to Amazon Redshift.

Finally, Using **AWS Quicksight** tool, will be doing data visualization from amazon redshift by writing sql queries.

![image](https://user-images.githubusercontent.com/60303995/117522064-13e17600-af66-11eb-8fbe-f2010ee6111d.png)

## Motivation

There are over 38300 Airbnb listings in California as of February,2021, which approximates to around 4 houses being rented per square mile. Airbnb has seen an exponential increase in the number of listings in California each year and has gained a lot of popularity. By analysing the number of listings and occupancy rates, we can understand demand rates and also provide metrics for people who would like to make an investment in Airbnb and rent out their properties. Previously collected data and reviews help understand how the occupancy rate can be increased.



