DarachGorham-FODA

This repository contains files related to the "FUNDAMENTALS OF DATA ANALYSIS" module, including tasks, projects, notebooks, and README files.

Contents:
1. tasks.ipynb: This file contains tasks related to the module.
2. project.ipynb: This file contains the iris dataset project.

Task Descriptions:

Task 1: Collatz Conjecture Verifier

Program Aim:
Verify, using Python, that the Collatz conjecture holds true for the first 10,000 positive integers.

Explanation:
The Python script found within the tasks.ipynb file contains a function Collatz(n) that generates the Collatz sequence for a given integer. The main loop goes through the first 10,000 positive integers, categorizing them into two lists (True, False) based on whether the Collatz conjecture holds true or false.

How to Run:
To run the code, execute it within the notebook.

Outcome:
The terminal should list integers that hold true before those that are false.

Task 2: Overview of Penguins Dataset

Explanation:
Provide an overview of the famous penguins dataset, explaining the types of variables it contains. Suggest the types of variables that should be used to model them in Python, explaining your rationale.

Task 3: Probability Distribution for Penguins Dataset

Explanation:
Suggest the most appropriate probability distribution from the numpy random distributions list to model the variables found within the penguins dataset.

Task 4: Plotting Entropy for Two Coin Flips

Program Aim:
Plot the entropy of the total number of heads versus the probability (p) for two coin flips.

How to Run:
To run the code, execute it within the notebook.

Outcome:
A plot will display the relationship between the probability distribution and entropy for two coin flips. Low probability of heads results in low entropy, indicating less uncertainty. As the probability increases, the entropy also increases.

Task 5: Plotting Variables from Penguins Dataset

Program Aim:
Plot the variables appropriately from the penguins dataset.

How to Run:
Run the code in the notebook itself.

Outcome:
Various histograms, scatterplots, and pairplots will be generated to present the data for analysis.

Summary:
The plots aim to provide a clear representation of the data for analysis, including histograms, scatterplots, and pairplots.

Project:

Project Brief:
The project is to create a notebook investigating the variables and data points within the well-known iris flower data set associated with Ronald A Fisher. In the notebook, you should discuss the classification of each variable within the data set according to common variable types and scales of measurement in mathematics, statistics, and Python. Select, demonstrate, and explain the most appropriate summary statistics to describe each variable. Select, demonstrate, and explain the most appropriate plot(s) for each variable.

Contents:

1. Introduction:
   - Overview of the Iris flower dataset, its origin, and significance.
   - Information about the features: sepal length, sepal width, petal length, petal width.
   
2. Classification of Variables:
   - Nominal (Species/Variety): Categorical variable representing different types of iris flowers.
   - Numeric Variables: Sepal and petal measurements, considered numerical variables.

3. Summary Statistics to Describe Each Variable:
   - Calculating mean, median, standard deviation, min, max for numeric variables.
   - Count and mode for the species/variety variable.

4. Plotting and Analysis of Data:
   a. Histograms of Variables:
      - Visualizing the distribution of each variable using histograms.
   
   b. Scatter Plots:
      - Understanding the relationship between two variables with scatter plots.
   
   c. Pairplot:
      - Comprehensive visualization of scatter plots and histograms for all variable pairs.

5. Conclusion:
   - Analysis of sepal and petal sizes across species.
   - Interpretation of pairplot findings.
   - Reflection on the overall learning experience.

