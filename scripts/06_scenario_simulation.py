
# 1. Import pandas, numpy
# 2. Load processed_data.csv
# 3. For each (province, crop) group:
#      a. Compute historical mean/std of average_yield and average_price
#      b. Run N Monte Carlo sims:
#           - sample yield ~ Normal(mean_yield, std_yield)
#           - sample price ~ Normal(mean_price, std_price)
#           - compute production = sampled_yield * seeded_area_ha
#           - compute value = production * sampled_price
#      c. Store simulations in a DataFrame
#      d. Save group’s simulations to '../outputs/simulations/{province}_{crop}.csv'
#      e. Plot histogram of simulated values, save figure
