# Weather Data Analysis and Text Clustering with MapReduce and Mahout

This project explores applying big data analytics techniques, specifically the MapReduce computational model and Apache Mahout, to analyze weather data and perform text clustering. The project is divided into two main parts:

1. Weather Data Analysis (Question 1): Finding descriptive statistics for temperature data using MapReduce.
2. Text Clustering (Question 2): Performing clustering analysis using Apache Mahout on a given text dataset.

## Dataset Description

### Weather Data (Question 1)
The dataset used for weather data analysis is "200704hourly.txt". It contains various features such as temperature, humidity, wind speed, and more.

### Text Data (Question 2)
The dataset used for text clustering is the "western_classics" corpus, specifically the files in the "western_classics/british-fiction-corpus/" directory.

## Project Structure

The project is organized into two main directories:

- `Question1/`: Contains the MapReduce code and output for weather data analysis tasks.
  - `Q1-1/`: Task 1 - Find the difference between each day's maximum and minimum wind speed.
  - `Q1-2/`: Task 2 - Find the daily minimum relative humidity.
  - `Q1-3/`: Task 3 - Find the daily mean and variance of dew point temperature.
  - `Q1-4/`: Task 4 - Find the correlation matrix for relative humidity, wind speed, and dry bulb temperature.

- `Question2/`: Contains the Apache Mahout commands and output for text clustering tasks.
  - `Q2-1/`: Task 1 - Implement K-means clustering with Euclidean and Manhattan distance measures.
  - `Q2-2/`: Task 2 - Find the optimum number of clusters (K) for K-means clustering.
  - `Q2-3/`: Task 3 - Implement K-means clustering with cosine distance measure.
  - `Q2-4/`: Task 4 - Plot the elbow graph for K-means clustering with cosine distance measure.
  - `Q2-5/`: Task 5 - Compare different clusters obtained with different distance measures.

## Requirements

- Python 3.x
- Hadoop
- Apache Mahout

## Usage

1. Clone the repository:
   ```
   https://github.com/carlos-alves-one/Weather-Cluster.git
   ```

2. Set up Hadoop and Apache Mahout environment.

3. Download the required datasets and place them in the appropriate directories.

4. Navigate to the specific task directory and run the MapReduce or Mahout commands as described in the project report.

5. Analyze the output files generated for each task.

## Results

The project report provides a detailed analysis of the results obtained for each task, including:

- Descriptive statistics for weather data using MapReduce.
- Clustering analysis using Apache Mahout with different distance measures and varying numbers of clusters.
- Evaluation metrics and insights for each clustering task.
- Comparison of different distance measures and optimal settings for K-means clustering.

## Limitations

The project report also discusses the limitations of the MapReduce methodology and Hadoop's MapReduce computing engine for this project, such as data locality, iterative algorithms, data shuffling, and more.

Please refer to the project report for detailed information on each task, results, and analysis.
