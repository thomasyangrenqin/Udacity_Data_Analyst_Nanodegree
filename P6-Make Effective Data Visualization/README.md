# P6
# Make effective data visualization
---
## Summary
The picked dataset is about the historical(1790-2010) proportion change of the population of the city of NewYork and its boroughs. It mainly reflect the population distribution shift from '**most people lived in Manhattan**' to '**People have more diverse living place choices**'. Specifically, people firstly move out of Manhattan, and chose the Brooklyn to live during around 1830-1930, and Brooklyn gradually replaced Manhattan as the most popular living place. Since around 1900, Queens and Bronx witnessed rapidly population increase in these area, and Queens also exceeded the Manhattan, becoming the second most popular living place since 1960. 

##Design
* Before the changes according to the feedbacks: 
Since the dataset I obtained only contains the population percentages of different places during 1790-2010, I chose the stacked bar chart to represent this dataset. I Used x coordinates to represent different years, and different color stacked bar to present different places. Y coordinates are used to measure the percentages. Each bar within the specific year will have the same height, which represent the sum of the percentages of population of different places within the specific year is 100%. I chose to add tooltip at the part where hover over happens as the interaction of my chart, giving the readers the ability to check with the specific data of each place during different year.

* Adaptions according to the feedbacks:
First, I change the colors which representing different places. The former picked colors including the same color I used as the font color of the tooltips. Also I chose some more comparable colors to better represent the change trends through different years this time.
I also changed some details of the interaction. I used 'add all the detailed data  of the specific year as tooltip when the reader hover over the specific year' to replace the original 'only show the data of specific place within the specific year'.
Finally, I changed the format of the information in the tooltip. I directly using the exact percent values in the tooltips to enable readers to better inspect the detailed data.

## Feedbacks
* "Since you are displaying the change trends through out different years, I think it would be better to show all the detailed data of the specific year as tooltip. For example, if I want to compare the exact percentages of different area within the specific year, I need hover all the different places, which is a little bit not use-friendly."
* "I noticed that the information in the tooltips, you used them  by using the original data without telling me, as a reader, whether this is the exact number of population or the percentage of the total population. I would suggest to denote the unite of the data."
* "It's a nice work. I could only think of one suggestion on color. I don't understand why you used the same color as the font color of the information in the tooltip and the symbol of 'Staten Island', I just recommend to pick some other colors to represent your different areas."
*  "From my point of view, I would say, for this kind of stacked bar chart, 'erasing' the track of coordinates would make your chart more fluent and concise."


## Resources
* https://plot.ly/~Dreamshot/113/city-of-new-york-boroughs-population/#plot
* http://bl.ocks.org/tmaybe/6144082
* http://bl.ocks.org/katirg/5f168b5c884b1f9c36a5
