from datetime import date
import holidays
import pandas 
import matplotlib.pyplot as plt
print("\n")

tr_holidays = holidays.Turkey(years=2020,observed=False)
for date in tr_holidays:
    print(date,tr_holidays[date])

print("\n")

it_holidays = holidays.Italy(years=2020,observed=False)
for date in it_holidays:
    print(date,it_holidays[date])   

print("\n")

statesUS=holidays.US.STATES
lists=[]
for state in statesUS:
    lists.append(
                {"State": state,
                "Holiday_Days": len(holidays.US(years=2020,observed=False,state=state))}
    )
us=pandas.DataFrame(lists) 
us=us.sort_values(by="Holiday_Days",ascending=False)
us[0:10].plot(kind="bar",x="State",y="Holiday_Days")
plt.show() 

provinces=holidays.IN.PROVINCES
dataset=[]
for province in provinces:
    dataset.append(
                {"Province": province,
                "Holiday_Days": len(holidays.IN(years=2020,observed=False,prov=province))
                }
                )
india=pandas.DataFrame(dataset) 
india=india.sort_values(by="Holiday_Days",ascending=False)
india[0:10].plot(kind="bar",x="Province",y="Holiday_Days")
plt.show()

countries=[]
for country in holidays.list_supported_countries():
    if len(country)>3:
        countries.append(country)
    else:
        pass
print(countries)        
print("\n")
datasett=[]
for country in countries:
    try:
        datasett.append(
                {"Country": country,
                "Holiday_Days": len(holidays.CountryHoliday(country,years=2020,observed=False))
                }
                )
    except:
        pass
f=pandas.DataFrame(datasett) 
f=f.sort_values(by="Holiday_Days",ascending=False)
f[0:10].plot(kind="bar",x="Country",y="Holiday_Days")
plt.show()

