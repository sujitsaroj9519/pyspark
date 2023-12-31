# -*- coding: utf-8 -*-
"""pyspark.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18dCzI18aBqtstQL0WDWbmbwT7xcoA438
"""

from pyspark.sql import SparkSession
from pyspark.sql import Row

# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Define the data and columns
data = [('John', 90, 85, 89),
        ('Alice', 78, 92, 88),
        ('RS', 100, 78, 93),
        ('Ash', 86, 99, 95)]

columns = ['Name', 'Math', 'Physics', 'Chemistry']

# Create an RDD of Row objects
rows = [Row(*row) for row in data]

# Create a DataFrame
df1 = spark.createDataFrame(rows, columns)

# Show the DataFrame
df1.show()

# Describe the DataFrame
df1.describe().show()

from pyspark.sql.functions import col

# df1.withColumn('new_column',col('Sub1')).show()
df1.withColumn('Math',col('Math')*100).show()

"""**Number of records**"""

df1.count()

"""**Print Result**"""

print("Newly created dataframe is: ")
# print(df1.show())

df1.show()

"""**Number of Column**"""

print(type(df1))

df1.columns

"""**Summary of DataFrame**"""

df1.describe()

"""**Schema Of DataFrame**"""

df1.printSchema()

"""**Create New Columns**"""

df1.withColumn('New_Columns',col('Math')).show()

"""**Arthmatic Operation**
==>
Addition constant to a column
==> Addition of two column
"""

df1.withColumn('Add_test1',col('Math')+100).show()

df1.withColumn('Add_test2',col('Math')+col('Physics')).show()

"""**Addition of Multiple Col**"""

df1 = df1.withColumn('Total',col('Math')+col('Physics')+col('Chemistry'))
df1.show()

"""**Change Column Datatype**

Cast to int

cast to double
"""

df1.printSchema()

df1.withColumn('Total_new',col('Total').cast('int')).show()

df1.withColumn('Total_new',col('Total').cast('int')).printSchema()

"""**Change column type int**"""

df1.withColumn('Total_new',col('Total').cast('int')).show()

"""**Create a new column with constant value**"""

df1 = df1.withColumn('Total_mar_alloted',lit(300))
df1.show()

"""**Multiply and divide**"""

df1 = df1.withColumn('Percantage',col('Math')*100/col('Total'))
df1.show()

"""**Column Rounded**"""

df1.withColumn('Percentage_rounded',bround(col('Percantage'),0)).show()

df1.withColumn('Percentage_rounded',bround(col('Percantage'),1)).show()

df1.withColumn('Percentage_rounded',bround(col('Percantage'),2)).show()

"""**Final Percantage**

"""

df1=df1.withColumn('Percentage_rounded',bround(col('Percantage'),2))
df1.show()

"""**Sorting Operation** ++ Ascending ++ Descending"""

df1.sort(desc('Percentage_rounded')).show()

df1 =df1.sort(asc('Percentage_rounded'))
df1.show()

df1.orderBy(col('Math').asc()).show()

df1.orderBy(col('Math').desc()).show()

"""**Drope Columns**"""

df1.show()

df1.drop('Total').show()

df1.drop('Total').drop('Math').show()

df1.show()

df1.drop('Math','Physics').show()

"""**Rename Column**



"""

df1.show()

df1 =df1.withColumnRenamed('Percantage','Per').show()

"""**Create A column with string Constant**

"""

df1 = df1.withColumn('Performance',lit('Excelent'))
df1.show

"""**Conditional Statment**"""

df1 = df1.withColumn('Grade',when(col('Per')>90,lit('A1')).otherwise('A2'))
df1.show()

"""**Changin Case upper / Lower**

"""

df1.withColumn('case_tes',upper(col('Name'))).show()
df1.withColumn('case',lower(col('Name'))).show()

"""**Filtering**

"""

df1.where(col('Name')=='Ash').show()
df1.where(col('Math')>=90).show()

df1.filter(col('Name')!='Ash').show()

"""**Grouping and Aggrigation**"""

15 Student
3 like baseball
8 like cricket
4 like footbal

df1.groupBy('Grade').agg(count('name')).show()

df1.groupBy('Grade').agg(max('Per')).show()

df1.groupBy('Grade').agg(min('Per')).show()