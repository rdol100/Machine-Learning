<b>FifaPredictOverall.py</b>

This code uses supervised machine learning to predict the overall rating of a FIFA 19 player from their attributes through optimising a linear regression model.

A majority of the steps (e.g. creating training and validation data) is simplified through the implementation of the sklearn libraries. When limiting the process to players in similar positions R<sup>2</sup> of over 0.9 can be achieved.


<b>FifaNeighbour.py</b>

Prerequisite to k nearest neightbours clustering. This code takes an input of player id (from 'fifa19.csv') and then uses a nearest neighbours algorithm to determine the top five most similar players in terms of attributes.

Possible improvements include implementing the option for the user to enter the name of the player rather than having to look up the player id in the csv file. This could be achieved through using regular expressions to separate first and last names in the dataframe.

