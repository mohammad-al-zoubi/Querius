# Querious: Logfile Analysis, Summary, and Chat


![QA Mode](images/logo.png)

![QA Mode](images/welcome.png)

## 1. Intoduction
Welcome to the Querious GitHub repository! Querious is a powerful tool designed for logfile analysis, summary generation, and interactive chatting with logs. Below, you'll find a comprehensive guide to each of its key functionalities. For more technical details, please refer to one of the folders above and read their respective READMEs.



## 1. QA Mode
### Asking Specific Questions About Logs
Querious allows users to ask specific questions about logfiles, such as "What SSH errors happened in these logs?" The answers are generated using large language models, providing full traceability to the loglines used in generating the answer.

![QA Mode](images/qa.png)

## 2. Log Search Mode
### Asking Questions and Retrieving Top Loglines
In Log Search Mode, users can pose specific questions about the logs in a logfile. Querious then displays the top N loglines from the respective log file that best match the query.

![Log Search Mode](images/search.png)

## 3. Dynamic Summary Generation
### Generate Individualized Logfile Summaries
Querious allows users to input parameters, such as start and end dates, start and end lines, and specific topics (e.g., SSH authorization or errors). Based on these parameters, Querious automatically generates a dynamic summary of the log file.

![Dynamic Summary](images/summary.png)

## 4. User Feedback and Continuous Improvement
### Submit Improvement Suggestions
Querious empowers users to submit improvement suggestions for the ranking algorithm through annotations. Users can navigate to specific lines, select them, and submit a query for which these lines are the answer. Submitted labels contribute to a continuous training system, enhancing embeddings generation and reranking algorithms.

![User Feedback](images/anno_1.png)

![User Feedback](images/anno_2.png)

---

Feel free to explore the full potential of Querious, and don't hesitate to provide feedback or contribute to its development. Happy log exploring! 🚀