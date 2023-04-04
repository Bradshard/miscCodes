# Settings things up for access

getwd()
setwd("C:/Users/Wilkins Inc/OneDrive/Desktop/novel-corona-virus-2019-dataset")

confirmed <- read.csv("time_series_covid_19_confirmed.csv", header = TRUE)
deaths <- read.csv("time_series_covid_19_deaths.csv", header = TRUE)
recovered <- read.csv("time_series_covid_19_recovered.csv", header = TRUE)

install.packages("GGally")
install.packages("ggplot2")
library("ggplot2")
library("ggpairs")

#Turkey_dead <- b[b$Country.Region == "Turkey",]
#Italy_dead <- b[b$Country.Region == "Italy",]

# To find countries we want to locate

confirmed$Country.Region
deaths$Country.Region
recovered$Country.Region

day <- c(1:77)

# For Turkey
Turkey_confirmed <- confirmed[which(confirmed$Country.Region %in% c("Turkey")),5:81]
Turkey_confirmed <- unname(unlist(Turkey_confirmed[1,]))

Turkey_dead <- deaths[which(deaths$Country.Region %in% c("Turkey")),5:81]
Turkey_dead <- unname(unlist(Turkey_dead[1,]))

Turkey_recovered <- recovered[which(recovered$Country.Region %in% c("Turkey")),5:81]
Turkey_recovered <- unname(unlist(Turkey_recovered[1,]))

# For Italy
Italy_confirmed <- confirmed[which(confirmed$Country.Region %in% c("Italy")),5:81]
Italy_confirmed <- unname(unlist(Italy_confirmed[1,]))

Italy_dead <- deaths[which(deaths$Country.Region %in% c("Italy")),5:81]
Italy_dead <- unname(unlist(Italy_dead[1,]))

Italy_recovered <- recovered[which(recovered$Country.Region %in% c("Italy")),5:81]
Italy_recovered <- unname(unlist(Italy_recovered[1,]))

# For South Korea
South_Korea_confirmed <- confirmed[which(confirmed$Country.Region %in% c("Korea, South")),5:81]
South_Korea_confirmed <- unname(unlist(South_Korea_confirmed[1,]))

South_Korea_dead <- deaths[which(deaths$Country.Region %in% c("Korea, South")),5:81]
South_Korea_dead <- unname(unlist(South_Korea_dead[1,]))

South_Korea_recovered <- recovered[which(recovered$Country.Region %in% c("Korea, South")),5:81]
South_Korea_recovered <- unname(unlist(South_Korea_recovered[1,]))

# Create Data Frame

Turkey_data <- data.frame(confirmed = Turkey_confirmed, deaths = Turkey_dead, recovered = Turkey_recovered, day = day)

Italy_data <- data.frame(confirmed = Italy_confirmed, deaths = Italy_dead, recovered = Italy_recovered, day = day)

South_Korea_data <- data.frame(confirmed = South_Korea_confirmed, deaths = South_Korea_dead, recovered = South_Korea_recovered, day = day)

# PLOTS

#Confirmed Case Comparison

Turkey_Italy_Confirmed_Plot <- ggplot(Turkey_data, aes(x = day, y = confirmed, color="Turkey")) +
  geom_line()+
  geom_line(data = Italy_data, aes(x = day, y = confirmed,color="Italy"))

Turkey_Italy_Confirmed_Plot

Turkey_South_Korea_Confirmed_Plot <- ggplot(Turkey_data, aes(x = day, y = confirmed, color="Turkey")) +
  geom_line()+
  geom_line(data = South_Korea_data, aes(x = day, y = confirmed,color="South Korea"))

Turkey_South_Korea_Confirmed_Plot

Italy_South_Korea_Confirmed_Plot <- ggplot(Italy_data, aes(x = day, y = confirmed, color="Italy")) +
  geom_line()+
  geom_line(data = South_Korea_data, aes(x = day, y = confirmed, color="South Korea"))

Italy_South_Korea_Confirmed_Plot

# Death Comparison

Turkey_Italy_Death_Plot <- ggplot(Turkey_data, aes(x = day, y = deaths, color="Turkey")) +
  geom_line()+
  geom_line(data = Italy_data, aes(x = day, y = deaths,color="Italy"))

Turkey_Italy_Death_Plot

Turkey_South_Korea_Death_Plot <- ggplot(Turkey_data, aes(x = day, y = deaths, color="Turkey")) +
  geom_line()+
  geom_line(data = South_Korea_data, aes(x = day, y = deaths,color="South Korea"))

Turkey_South_Korea_Death_Plot

Italy_South_Korea_Death_Plot <- ggplot(Italy_data, aes(x = day, y = deaths, color="Italy")) +
  geom_line()+
  geom_line(data = South_Korea_data, aes(x = day, y = deaths, color="South Korea"))

Italy_South_Korea_Death_Plot

# Recovery Comparison
Turkey_Italy_Recovered_Plot <- ggplot(Turkey_data, aes(x = day, y = recovered, color="Turkey")) +
  geom_line()+
  geom_line(data = Italy_data, aes(x = day, y = recovered,color="Italy"))

Turkey_Italy_Recovered_Plot

Turkey_South_Korea_Recovered_Plot <- ggplot(Turkey_data, aes(x = day, y = recovered, color="Turkey")) +
  geom_line()+
  geom_line(data = South_Korea_data, aes(x = day, y = recovered,color="South Korea"))

Turkey_South_Korea_Recovered_Plot

Italy_South_Korea_Recovered_Plot <- ggplot(Italy_data, aes(x = day, y = recovered, color="Italy")) +
  geom_line()+
  geom_line(data = South_Korea_data, aes(x = day, y = recovered, color="South Korea"))

Italy_South_Korea_Recovered_Plot
