# KW9M
A Chinese data set extracted from CN-DBpedia for training on model TransE to get word embeddings.

CN-DBpedia is a Chinese Knowledge Base of general facts with ever-increasing in size and updated frequently, which develops and maintains by Knowledge Works Research Laboratory of Fudan University, and it is the earliest and largest open encyclopedia Chinese KG in China. The sources of knowledge are from three Chinese online encyclopedias. Currently, it contains almost 65 million triple facts and exceeds 9 million entities. 
We create a Chinese dataset name KW9M based on CN-DBpedia which contains 65,001,293 triple facts with 9,412,272 entities and 377,910 relationships for training on TransE model. First, we swap the position of relation and tail entity. Second, we extract head entity and relation and add index to them respectively. Third, we remove the duplicate entity and relation and at last obtain the dataset.

Here, we provide the code (KW9M.py) to demonstrate how we process the source data and obtain KW9M. The source data you can download from this link:http://kw.fudan.edu.cn/cndbpedia/download/

In the fruture, we will contuine to optimize the data. 
Thanks for your attention and welcome to give us some suggtions warmly！
