# Canopy-Power-Assignment

# Background information:
Project ABC is an off-grid project with diesel genset and solar PV system. The energy output by solar PV is directly proportional to irradiance, we can roughly consider energy output by solar system in kW to be 0.09 of irradiance in W/m2. E.g when irradiance is 700W/m2, the solar system is producing at 63kW. The rest of the load is taken by the genset. Producing 1kWh by genset requires burning 0.3liter diesel. Production is always equal to consumption. When PV production is higher than the load, PV production is curtailed to be the same as the load, since genset power cannot be negative.
Reference Datasheet:
1. 1 day data of both irradiance and load
Task:
Please do the following:
1. Draw the 24 hours power distribution graph of genset, load and PV.
2. Calculate how many liters of diesel will be used this day

# Data cleasing and preprocessing 
1. Check for the null data. Assume that the data will be linear-distrubuted, so we can replace the null data with the mean of 2 closest data
2. Calculating total time interval 

# Calculation
The PV is first calculated by using the irradiance (PV = irradiance x 0.09)
If the PV is larger than total load, PV is equal total load
The genset is calculated by: genset = total load - PV
Then the total amount of diesel can be calculated by using the intergral form of genset: diesel = Δt∑genset.

# Graph
![Figure_1](https://user-images.githubusercontent.com/59272955/153173404-a1ba9dab-79ab-4666-98df-d6f1ad2fe2ce.png)
