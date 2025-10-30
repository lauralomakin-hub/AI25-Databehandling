import pandas  as pd

import pandas as pd

cities_per_population = { 
    "cities" : ["Malmö", "Stokcholm",  "Uppsala", "Göteborg"],
    "population" : [347949, 975551, 233839, 583056]
                         }

df = pd.DataFrame(cities_per_population)

print(cities_per_population)