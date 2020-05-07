# Mongo Size Estimator

This is a project to help estimate what your MongoDB Atlas cluster IOPS will be, given existing MongoDB database usage.

## Installation

Make sure you have python 3.6 + on your machine

## Usage

1. open the mongostat.sh file and edit the host, username, and password
2. run mongostat.sh during a time that is representative of your application usage
3. run main.py which will read the output.txt file and output your inserts, queries, updates and deletes / second
4. repeat for high, medium, and low application times


![Output](/assets/output.png?raw=true "Output")
