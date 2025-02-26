# Presidential Speech Classifier

This project implements a Multinomial Naïve Bayes classifier to analyze the speeches of candidates for the Presidency of Romania. The goal is to determine the most likely author of a given speech based on linguistic patterns and key terms.

Project Overview
	•	Data Collection: Gathered speeches from five major candidates: Marcel Ciolacu, Nicolae Ciucă, Elena Lasconi, George Simion, and Mircea Geoană.
	•	Preprocessing: Tokenized and structured the speeches into a frequency-based dataset using Python dictionaries.
	•	Key Term Extraction: Identified words that are significantly more frequent in one candidate’s speeches than in others.
	•	Probability Computation:
	•	Prior Probabilities: Estimated the likelihood of a speech belonging to a given candidate.
	•	Conditional Probabilities: Used Bayes’ Theorem to determine the probability of a speech belonging to a candidate given a set of key terms.
	•	Classification:
	•	Processed an unseen speech and computed probability scores for each candidate.
	•	Assigned the speech to the candidate with the highest probability.
	•	Testing: Validated the model on real speech samples from each candidate.

Usage
	1.	Prepare Data: Ensure training speeches are stored in the correct format.
	2.	Run Analysis: Execute the script to process input speeches and generate predictions.
	3.	Interpret Results: The program outputs the candidate with the highest probability along with detailed probability scores.

Dependencies
	•	Python 3.x
	•	NumPy
	•	Pandas (optional, for structured data handling)

Contributors
	•	Militaru Ștefan-Octavian
	•	Cucu Mihnea
