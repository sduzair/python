|     | Feature                         | Description                                                     |
|----:|:--------------------------------|:----------------------------------------------------------------|
|   0 | Year                            | Year                                                            |
|   1 | Quarter                         | Quarter                                                         |
|   2 | Month                           | Month                                                           |
|   3 | DayofMonth                      | Day of Month                                                    |
|   4 | DayOfWeek                       | Day of Week (numeric)                                           |
|   5 | FlightDate                      | Date of Flight                                                  |
|   6 | Reporting_Airline               | Airline Unique Carrier Code                                     |
|   7 | DOT_ID_Reporting_Airline        | Number assigned by US DOT to identify a unique airline          |
|   8 | IATA_CODE_Reporting_Airline     | Airline Code assigned by IATA                                   |
|   9 | Tail_Number                     | Aircraft tail number                                            |
|  10 | Flight_Number_Reporting_Airline | Flight Number                                                   |
|  11 | OriginAirportID                 | Origin Airport ID                                               |
|  12 | OriginAirportSeqID              | Origin Airport Sequence ID                                      |
|  13 | OriginCityMarketID              | Origin City Market ID                                           |
|  14 | Origin                          | Origin Airport Code                                             |
|  15 | OriginCityName                  | Origin City Name                                                |
|  16 | OriginState                     | Origin State                                                    |
|  17 | OriginStateFips                 | Origin State FIPS place code                                    |
|  18 | OriginStateName                 | Origin State Name                                               |
|  19 | OriginWac                       | Origin Airport World Area Code                                  |
|  20 | DestAirportID                   | Destination Airport ID                                          |
|  21 | DestAirportSeqID                | Destination Airport Sequence ID                                 |
|  22 | DestCityMarketID                | Destination City Market ID                                      |
|  23 | Dest                            | Destination Airport Code                                        |
|  24 | DestCityName                    | Destination City Name                                           |
|  25 | DestState                       | Destination State                                               |
|  26 | DestStateFips                   | Destination State FIPS code                                     |
|  27 | DestStateName                   | Destination State Name                                          |
|  28 | DestWac                         | Destination Airport World Area Code                             |
|  29 | CRSDepTime                      | Computer Reservation System (scheduled) Departure Time          |
|  30 | DepTime                         | Departure Time (hhmm)                                           |
|  31 | DepDelay                        | Departure delay (minutes)                                       |
|  32 | DepDelayMinutes                 | Absolute value of DepDelay                                      |
|  33 | DepDel15                        | Departure Delay >15?                                            |
|  34 | DepartureDelayGroups            | Departure delay 15 minute interval group                        |
|  35 | DepTimeBlk                      | Computer Reservation System (scheduled) time block              |
|  36 | TaxiOut                         | Taxi out time (minutes)                                         |
|  37 | WheelsOff                       | Wheels off time (local time, hhmm)                              |
|  38 | WheelsOn                        | Wheels on time (local time hhmm)                                |
|  39 | TaxiIn                          | Taxi in time (minutes)                                          |
|  40 | CRSArrTime                      | Computer Reservation System (scheduled) Arrival Time            |
|  41 | ArrTime                         | Arrival time (local time, hhmm)                                 |
|  42 | ArrDelay                        | Arrival delay (minutes)                                         |
|  43 | ArrDelayMinutes                 | Absolute value of ArrDelay                                      |
|  44 | ArrDel15                        | Arrival Delay >15?                                              |
|  45 | ArrivalDelayGroups              | Arrival delay 15 minute interval group                          |
|  46 | ArrTimeBlk                      | Computer Reservation System (scheduled) arrival time block      |
|  47 | Cancelled                       | 1 = canceled                                                    |
|  48 | CancellationCode                | A = Carrier, B = Weather, C = National Air System, D = Security |
|  49 | Diverted                        | 1 = diverted                                                    |
|  50 | CRSElapsedTime                  | Computer Reservation System (scheduled) elapsed time            |
|  51 | ActualElapsedTime               | Actual elapsed time                                             |
|  52 | AirTime                         | Flight time (minutes)                                           |
|  53 | Flights                         | Number of flights                                               |
|  54 | Distance                        | Distance between airports (miles)                               |
|  55 | DistanceGroup                   | 250 mile distance interval group                                |
|  56 | CarrierDelay                    | Carrier delay (minutes)                                         |
|  57 | WeatherDelay                    | Weather delay (minutes)                                         |
|  58 | NASDelay                        | National Air System delay (minutes)                             |
|  59 | SecurityDelay                   | Security delay (minutes)                                        |
|  60 | LateAircraftDelay               | Late aircraft delay (minutes)                                   |
|  61 | FirstDepTime                    | First gate departure time at origin airport                     |
|  62 | TotalAddGTime                   | Total ground time away from gate                                |
|  63 | LongestAddGTime                 | Longest time away from gate                                     |
|  64 | DivAirportLandings              | Number of diverted airport landings                             |
|  65 | DivReachedDest                  | 1 = diverted flight reached scheduled destination               |
|  66 | DivActualElapsedTime            | Elapsed time of diverted flight reaching scheduled destination  |
|  67 | DivArrDelay                     | Difference in minutes between scheduled and actual arrival time |
|  68 | DivDistance                     | Distance between scheduled and diverted airport                 |
|  69 | Div1Airport                     | Diverted Airport 1                                              |
|  70 | Div1AirportID                   | Diverted Airport 1 ID                                           |
|  71 | Div1AirportSeqID                | Diverted Airport 1 Sequence ID                                  |
|  72 | Div1WheelsOn                    | Diverted Airport 1 wheels on time (local, hhmm)                 |
|  73 | Div1TotalGTime                  | Diverted Airport 1 total ground time away from gate             |
|  74 | Div1LongestGTime                | Diverted Airport 1 longest ground time away from gate           |
|  75 | Div1WheelsOff                   | Diverted Airport 1 wheels off time (local, hhmm)                |
|  76 | Div1TailNum                     | Diverted Airport 1 aircraft tail number                         |
|  77 | Div2Airport                     | Diverted Airport 2                                              |
|  78 | Div2AirportID                   | Diverted Airport 2 ID                                           |
|  79 | Div2AirportSeqID                | Diverted Airport 2 Sequence ID                                  |
|  80 | Div2WheelsOn                    | Diverted Airport 2 wheels on time (local, hhmm)                 |
|  81 | Div2TotalGTime                  | Diverted Airport 2 total ground time away from gate             |
|  82 | Div2LongestGTime                | Diverted Airport 2 longest ground time away from gate           |
|  83 | Div2WheelsOff                   | Diverted Airport 2 wheels off time (local, hhmm)                |
|  84 | Div2TailNum                     | Diverted Airport 2 aircraft tail number                         |
|  85 | Div3Airport                     | Diverted Airport 3                                              |
|  86 | Div3AirportID                   | Diverted Airport 3 ID                                           |
|  87 | Div3AirportSeqID                | Diverted Airport 3 Sequence ID                                  |
|  88 | Div3WheelsOn                    | Diverted Airport 3 wheels on time (local, hhmm)                 |
|  89 | Div3TotalGTime                  | Diverted Airport 3 total ground time away from gate             |
|  90 | Div3LongestGTime                | Diverted Airport 3 longest ground time away from gate           |
|  91 | Div3WheelsOff                   | Diverted Airport 3 wheels off time (local, hhmm)                |
|  92 | Div3TailNum                     | Diverted Airport 3 aircraft tail number                         |
|  93 | Div4Airport                     | Diverted Airport 4                                              |
|  94 | Div4AirportID                   | Diverted Airport 4 ID                                           |
|  95 | Div4AirportSeqID                | Diverted Airport 4 Sequence ID                                  |
|  96 | Div4WheelsOn                    | Diverted Airport 4 wheels on time (local, hhmm)                 |
|  97 | Div4TotalGTime                  | Diverted Airport 4 total ground time away from gate             |
|  98 | Div4LongestGTime                | Diverted Airport 4 longest ground time away from gate           |
|  99 | Div4WheelsOff                   | Diverted Airport 4 wheels off time (local, hhmm)                |
| 100 | Div4TailNum                     | Diverted Airport 4 aircraft tail number                         |
| 101 | Div5Airport                     | Diverted Airport 5                                              |
| 102 | Div5AirportID                   | Diverted Airport 5 ID                                           |
| 103 | Div5AirportSeqID                | Diverted Airport 5 Sequence ID                                  |
| 104 | Div5WheelsOn                    | Diverted Airport 5 wheels on time (local, hhmm)                 |
| 105 | Div5TotalGTime                  | Diverted Airport 5 total ground time away from gate             |
| 106 | Div5LongestGTime                | Diverted Airport 5 longest ground time away from gate           |
| 107 | Div5WheelsOff                   | Diverted Airport 5 wheels off time (local, hhmm)                |
| 108 | Div5TailNum                     | Diverted Airport 5 aircraft tail number                         |