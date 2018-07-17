import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the city name among chicago, new york city, washington to analyze: \n")
    # checking for valid city name.
    while True:
        if city.lower() in CITY_DATA.keys():
            break
        else:
            city = input("oops! It seems like you have entered something wrong.\nEnter the city name among chicago, new york city, washington to analyze: \n")
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter name of the month from  ["january", "february", "march", "april", "may", "june"] to filter by, or "all" to apply no month filter: \n')
    # checking for valid month name.
    while True:
        if month.lower() in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            month = input('oops! It seems like you have entered something wrong.\nEnter name of the month from  ["january", "february", "march", "april", "may", "june"] to filter by, or "all" to apply no month filter: \n')
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter name of the day of week to filter by, or "all" to apply no day filter: \n')
    #checking for valid day.
    while True:
        if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            day = input('oops! It seems like you have entered something wrong.\nEnter name of the day of week to filter by, or "all" to apply no day filter: \n')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # reading csv file into df.
    df = pd.read_csv(CITY_DATA[city])
    # converting start time column to datetime.
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    # creating hour column.
    df["hour"] = df["Start Time"].dt.hour
    # creating month column.
    df["month"] = df["Start Time"].dt.month
    # creating day of week column.
    df["day_of_week"] = df["Start Time"].dt.weekday_name
    
    # filtering df based on month.
    if month != "all":
        months = ["january","february","march","april","may","june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]
    
    # filtering df based on day.   
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("most common month: ", df["month"].mode()[0])
    
    # TO DO: display the most common day of week
    print("most common day of week: ", df["day_of_week"].mode()[0])

    # TO DO: display the most common start hour
  
    print("most common start hour: ", df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station: ", df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print("most commonly used end station: ", df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    # creating trip combination column.
    df["Trip Combination"] ="From " + df["Start Station"] + " To " + df["End Station"]
    print("most frequent combination of start station and end station: ", df["Trip Combination"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time in seconds: ", df["Trip Duration"].sum())
    print("total travel time in minutes: ", df["Trip Duration"].sum()/60)

    # TO DO: display mean travel time
    print("mean travel time in seconds: ", df["Trip Duration"].mean())
    print("mean travel time in minutes: ", df["Trip Duration"].mean()/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("count of users:\n ", df["User Type"].value_counts())
    

    # TO DO: Display counts of gender
    # checking if Gender column is present in data.
    if "Gender" in list(df):
        print("counts of gender:\n ", df["Gender"].value_counts())
    else:
        print("Gender column is not found in data.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # checking if Birth year column is present in data.
    if "Birth Year" in list(df):
        print("earliest year of birth: {} \nmost  recent  year of birth: {} \nmost common year of birth: {} ".format(int(df["Birth Year"].min()),
                                                                                                                    int(df["Birth Year"].max()),
                                                                                                                   int(df["Birth Year"].mode()[0])))
    else:
        print("Birth Year column is not found in data")
        
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       
        # code for displaying raw data.
        count = 0
        while True:
            raw_data = input("\nWould you like to see raw data? Enter yes or no.\n")
            if raw_data.lower() != "yes":
                break
            # printing five rows at a time.
            if count > df.shape[0]-6 :
                print(df.iloc[count:, :])
            else:
                print(df.iloc[count:count+5, :])
            count = count + 5
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
