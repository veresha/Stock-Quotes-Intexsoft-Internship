# Stock-Quotes-Intexsoft-Internship
It's a fisrt part of ***ETL-pipeline*** application for collection and aggregation Stock Quotes data.
Second part: <https://github.com/veresha/Kafka-Spark-Intexsoft-Internship>.
This app get Stock Quotes data from yahoo finance. 
***
## There are two options:
- **get historical data** - you can choose period(default: 1 year per day)
- **get realtime data** - you also can choose period with the help of **Celery Scheduler**
***
After the data has been received they sending to **Kafka** topic is JSON-format.
For this purpose app creating **Singletone** Kafka Producer.
