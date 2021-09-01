# Capstone Proposal
#### Theo Rowlett Class Panda

## A full stack app to project energy costs and savings for solar power depending on location

## Overview
This application uses a web interface where a client can input their geographic location, number/size of panels, and receive a best case projection for energy generation and cost savings over time. The application will only provide a best case scenario for panels and not take into account angle of placement or shade, these would cause the scope to balloon to unmanagable levels within the time constraints given.

#### The website will use the following API's: 
* https://www.eia.gov/opendata/ << US Energy Information Administration. It will be used to provide historical data of annual energy cost. This data will be used to create a line of best fit to determine projected energy costs over time.
* https://developer.nrel.gov/docs/solar/solar-resource-v1/ << National Renewabal Energy Laboratory. It will be used to provide the average global horizontal irradiance, which is measured in kilowatt hours per square meter per day, to be used in the calculations to determine how much actual power the panels will be receiving.
#### Undecided API's/Data
* The rate of degradation of panels. I am consulting industry experts to try and develop a model, but for now we can assume 80% efficiency lost linearly over 25 years.
* The rate of efficiency of panels. Still working on figuring out an estimate to how efficient the panels could be.

## Functionality

