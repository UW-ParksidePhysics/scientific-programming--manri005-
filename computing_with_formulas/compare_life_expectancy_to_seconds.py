#life expectancy from CDC
life_expectancy_in_years = 78.8 
# converts one billion seconds to years
one_billion_seconds_in_years = 1e9 / (60 * 60 * 24 * 365) 

print(f"One billion seconds in years: {one_billion_seconds_in_years}")
print(f"CDC life expectancy in years: {life_expectancy_in_years}")

if one_billion_seconds_in_years < life_expectancy_in_years:
  print ("A new born baby can expect to live for one billion seconds.")

else:
  print ("A new born baby cannot expect to live for one billion seconds.")

