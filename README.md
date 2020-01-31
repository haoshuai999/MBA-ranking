# MBA rankings by The Economist
The script is used to scrape [the annual MBA rankings]("https://www.economist.com/whichmba/full-time-mba-ranking?year=2019&term_node_tid_depth=77631") in north america. For the rankings of other regions, please contact the author.

**To scrape the ranking data, please:**
1. Install Python3 on your laptop or computer
2. Download the script MBA_ranking.py
3. In the same directory, Run the following command:
```sh
$ python MBA_ranking.py [year] [page] 
(replace [year] with the year of the ranking and replace [page] with the total number pages you want)
``` 

**Example:**
The following command will scrape the 2020 ranking of every school in north america and output the result into a CSV file named "MBA_ranking_2020.csv".
```sh
$ python MBA_ranking.py 2020 6
``` 

**Notes:**
The total number of pages is usually 6 for a given year. You can make sure the number is correct by double checking the page number on the website.