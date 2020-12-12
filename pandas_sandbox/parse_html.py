from bs4 import BeautifulSoup
import pandas as pd
import re

# This script practice the data from the html file containing citroen dealer information. 
# Get the dealer name and location.   
# Sort to get the duplicate dealer


if __name__ == "__main__":
    rows = []
    with open('citroen.html', 'r', encoding="utf-8") as f:
        htmltxt = f.read()
        soup = BeautifulSoup(htmltxt, 'lxml')
        a = soup.find_all('a')   # get all <a>...</a>
        for d in a:
            if len(d) > 1:    
                s = d.contents[1]  # contains the deal full name
                if isinstance(s, str) and s.startswith(' - '): 
                    i = d.contents[0].text  # get the location
                    # remove unnecessary infomration
                    if "A/S -" in s:
                        s = re.sub(r'A/S\s+-.+', '', s)
                    if "A/S" in s:
                        s = s.replace("A/S", "")
                    if "Aps" in s:
                        s = s.replace("Aps", "")
                    if "," in s:
                        s = re.sub(r',.+', '', s)
                    row = [s, i]
                    rows.append(row)
    # create the data frame                    
    forhandler = pd.DataFrame(rows, columns=['name', 'location'])
    forhandler = forhandler.set_index('name')
    forhandler = forhandler.sort_index()
    # forhandler = forhandler.groupby(forhandler.index)
    with pd.option_context('display.max_rows', None):
        print(forhandler)
    forhandler.to_csv('citroen.csv')