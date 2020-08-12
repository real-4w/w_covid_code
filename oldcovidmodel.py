import time
import datetime

#data 9/4/2020
new_sick = 44 
sick = 1283
new_hospital = 2
hospital = 16
new_recovered = 56
recovered = 373 
new_deaths = 1
deaths = 2

# initial calculation of model parameters

dt = datetime.date.today() #+ datetime.timedelta(days=-1)
sick_growth = 1 + (new_sick / (sick - new_sick))
hospital_growth = 1 + (new_hospital / (hospital - new_hospital))
recovered_growth = 1 + (new_recovered / (recovered - new_recovered))
death_growth = 1 # + (new_deaths / (deaths - new_deaths))

#simple forecast - lineair model
non_lineair = 0.99 #as of 30-3-2020 slowing spread down below linair

for x in range (1, 32) :
    print ("Day", dt, "sick people", round(sick), "growth factor", round(sick_growth,2), "in hospital", round(hospital),"total recovered", round(recovered),
           "death", round(deaths))

    #now update the new input

    dt = dt + datetime.timedelta(days=1)

    new_sick = (sick * sick_growth) - sick
    sick = sick * sick_growth

    new_hospital = (hospital * hospital_growth) - hospital
    hospital = hospital * hospital_growth
    
    new_recovered = (recovered * recovered_growth) - recovered
    recovered = recovered * recovered_growth

    new_deaths = (deaths * death_growth) - deaths
    deaths =  (deaths * death_growth)

    #recalculate the growth model - not needed for lineair model
    
    sick_growth = 1 + non_lineair * (new_sick / (sick - new_sick)) 
    hospital_growth = 1 + non_lineair * (new_hospital / (hospital - new_hospital))
    recovered_growth = 1 + non_lineair * non_lineair * (new_recovered / (recovered - new_recovered))
    death_growth = 1 + non_lineair * (new_deaths / (deaths - new_deaths))
    non_lineair = non_lineair * 0.99

print ("END")

#old data

#data 9/4/2020
#new_sick = 29 
#sick = 1210
#new_hospital = 1
#hospital = 14
#new_recovered = 35
#recovered = 317 
#new_deaths = 1
#deaths = 2

#data 8/4/2020
#new_sick = 50 
#sick = 1210
#new_hospital = 1
#hospital = 12
#new_recovered =41
#recovered = 282
#new_deaths = 1
#deaths = 2

#data 7/4/2020
#new_sick = 67 
#sick = 1106
#new_hospital = 1
#hospital = 13
#new_recovered =29
#recovered = 176
#new_deaths = 1
#deaths = 2

#data 5/4/2020
#new_sick = 89 
#sick = 1039
#new_hospital = 1
#hospital = 15
#new_recovered =29
#recovered = 156
#new_deaths = 1
#deaths = 2

#data 3/4/2020
#new_sick = 71 
#sick = 868
#new_hospital = 1
#hospital = 13
#new_recovered =11
#recovered = 103
#new_deaths = 1
#deaths = 2


#data 2/4/2020
#new_sick = 89 
#sick = 797
#new_hospital = 1
#hospital = 13
#new_recovered =10
#recovered = 92
#new_deaths = 1
#deaths = 2

#data 1/4/2020
#new_sick = 61 
#sick = 708
#new_hospital = 1
#hospital = 14
#new_recovered =8
#recovered = 82
#new_deaths = 1
#deaths = 2

#data 30/3/2020
#new_sick = 58 
#sick = 647
#new_hospital = 2
#hospital = 14
#new_recovered =11
#recovered = 74
#new_deaths = 1
#deaths = 2

#data 30/3/2020
#new_sick = 75
#sick = 589
#new_hospital = 3
#hospital = 12
#new_recovered = 7
#recovered = 63
#new_deaths = 1
#deaths = 2


#data 29/3/2020
#new_sick = 63
#sick = 514
#new_hospital = 3
#hospital = 9
#new_recovered = 6
#recovered = 56
#new_deaths = 1
#deaths = 2

#data 28/3/2020
#new_sick = 83
#sick = 451
#new_hospital = 3
#hospital = 12
#new_recovered = 13
#recovered = 50
#new_deaths = 0
#deaths = 0

#Data 27/3/2020
#new_sick = 85
#sick = 368
#new_hospital = 1
#hospital = 8
#new_recovered = 10
#recovered = 37
#new_deaths = 0
#deaths = 0

# Data 26/3/2020
# sick = 283
# new_sick = 78
# hospital = 7
# new_hospital = 2
# recovered = 27
# new_recovered = 5
# deaths = 0
# new_deaths = 0
