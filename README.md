# Project title: sentiment-analysis-of-youtube-comments
## Team members: 
- Kushal Gaywala, kushal.gaywala@stud.uni-heidelberg.de
- Rishabh Tiwari, rishabh.tiwari@stud.uni-heidelberg.de
- Jonathan Alexander Hirsch, ww251@stud.uni-heidelberg.de 
- Jakob Forstmann, jakob.forstmann@stud.uni-heidelberg.de

## utilzed libraries: 
- <a herf="https://pandas.pydata.org/">Pandas</a> used to clean up the data
	## processing libraries:
	- <a herf="https://www.nltk.org/api/nltk.stem.html">Stem</a>: used  WordNet Lemmatizer for lematization
	- <a herf="https://www.nltk.org/api/nltk.corpus.html">Corpus</a>: used  to remove stopwords
	- <a herf="https://www.nltk.org/">NLTK</a>: used to preprocess the data
	- <a herf="">re</a>: used to implement regular expression during processing

## used dataset 
We use the Movies and TV [amazon reviews dataset](https://nijianmo.github.io/amazon/index.html) from the following paper:

Justifying recommendations using distantly-labeled reviews and fined-grained aspects

Jianmo Ni, Jiacheng Li, Julian McAuley
Empirical Methods in Natural Language Processing (EMNLP), 2019

## project log
Contribution by Rishabh and Jonathan:

Date: 15/11/22
1) https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html - for the pipelining of the data and more traditional models.
2) https://www.tensorflow.org/tutorials - To train the data 
3) We studied about the sickit learn tutorial/implemented it/learning the usage of the sickit learn for the vectorization and training the data set. 

Date: 20/11/22

1) We continued to study scikit learn and its usage for text analysis.

Date: 01/12/22 - 04/12/22
1) Tried many ways by which I can read and process such huge dataset in my computer.
2) Methods I tried to use:
	a) Spliting the data
	b) Installed a linux distro and used swap memory(10GB) as extension to RAM(8GB) but it also didn't worked.
3) Atlast after unable to find a feasible method. We settled on the idea to use reduced dataset.

Date: 05/12/22
1) Now I just used a single file from the multiple splited to do the pre-processing and tesitng of the code.