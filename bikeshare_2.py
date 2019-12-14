import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
city_value = ""


def get_filters():  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> get_filters function >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data.')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # -------------------------------------------------------------------------------------------------------------
    global city_value
    print("Would you like to see data for Chicago, New York City or Washington? Make a choice!")
    city_value = input()
    while True:
        # Let check the content
        if city_value.lower() != "chicago".lower() and city_value.lower() != "new york city".lower() and city_value.lower() != "washington".lower():
            print(
                "The value entered is incorrect. Kindly enter the right value: Chicago, New York City or Washington.")
            city_value = input()
        else:
            print("City's value received.")
            city = city_value.lower()
            city_value = city_value.lower()
            break
    # Check if the user intend to filter the data, and eventually collect te data.
    # ----------------------------------------------------------------------------
    print("Would you like to filter the data by 'month', 'day', 'both', or not at all? Type 'none' for no time filter.")
    response_given = input()
    expected_response = ["month", "day", "both", "none"]
    response_given = response_given.lower()
    # Now let make sure the entered value is correct
    while True:
        if response_given not in expected_response:
            print(
                "The response value must be 'month', 'day', 'both', or 'none'. Enter the value again.")
            response_given = input()
        else:
            response_given = response_given.lower()
            break

    # Let get the values base on the entered response--------------------------------
    if response_given == "none":  # response_given='none'
        month = ""
        day = ""
    elif response_given == "month":  # response_given='month'
        # get user input for month (all, january, february, ... , june)
        months = ['all', 'january', 'february',
                  'march', 'april', 'may', 'june']
        while True:
            print("Enter the month (all, january, february,march,april,may or june).")
            month = input()
            month = month.lower()
            if month not in months:
                print("Wrong value entered for month.")
            else:
                day = "all"
                break

    elif response_given == "day":  # response_given='day'
        # get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['all', 'monday', 'tuesday',
                'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while True:
            print(
                "Enter the day (all, monday, tuesday,wednesday,thursday,friday,saturday, or sunday ).")
            day = input()
            day = day.lower()
            if day not in days:
                print("Wrong value entered for day.")
            else:
                month = "all"
                break
    elif response_given == "both":  # response_given='both'
        # Getting the month .........................
        months = ['all', 'january', 'february',
                  'march', 'april', 'may', 'june']
        while True:
            print("Enter the month (all, january, february,march,april,may or june).")
            month = input()
            month = month.lower()
            if month not in months:
                print("Wrong value entered for month.")
            else:
                break
         # Getting the day .........................
        days = ['all', 'monday', 'tuesday',
                'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while True:
            print(
                "Enter the day (all, monday, tuesday,wednesday,thursday,friday,saturday, or sunday ).")
            day = input()
            day = day.lower()
            if day not in days:
                print("Wrong value entered for day.")
            else:
                break
    print('-'*40)
    return city, month, day


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
    # load data file into a dataframe
    city = city.replace(" ", "_")  # Replaces spaces in city variable with "_"
    df = pd.read_csv("bikeshare-2/" + city + ".csv")

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    df['month'] = df['Start Time'].dt.month_name().str.lower()

    # df['day_of_week'] = df['Start Time'].dt.dayofweek  # dt.dayofweek give the index int value ie monday=0 , sunday=6 of the day
    df['day_of_week'] = df['Start Time'].dt.weekday_name.str.lower()
    # dt.weekday_name give the string or literal value of the day

    # If month and day not applicable
    if month != "" and day != "":
        # filter by month if applicable
        if month != 'all':

            # filter by month to create the new dataframe
            df = df[df["month"] == month]

        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    print("Most common month:   ", common_month)

    # display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("Most common day of week:   ", common_day)

    # display the most common start hour
    common_start_hour = df["Start Time"].dt.hour.mode()[0]
    print("Most common start hour:   ", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("Most common start station:   ", common_start_station)

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("Most common end station:   ", common_end_station)

    # display most frequent combination of start station and end station trip
    # common_start_and_end_station = df[['Start Station', 'End Station']].mode()
    # print("Most common start and end station:   ", common_start_and_end_station)
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print("Most common start and end station:   ", popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    sum_travel_time = df['Trip Duration'].sum()
    print("Total travel time:   ", sum_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time:   ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # print("Customers:   ", df[df["User Type"] == "Customer"].count())
    # print("Subscribers:   ", df[df["User Type"] == "Subscriber"].count())
    print("Display counts of user types:   ")
    print(df.groupby('User Type').size())

    # washington does not contain Gender and Birth year
    if city_value != "washington":

        # Display counts of gender
        # print("Male:   ", df[df["Gender"] == "Male"].Value_counts())
        # print("Female:   ", df[df["Gender"] == "Female"].Value_counts())
        print("Display counts of gender:   ")
        print(df.groupby('Gender').size())

        # Display earliest, most recent, and most common year of birth
        print("Earliest year of birth:   ", df["Birth Year"].min())
        print("Most recent year of birth:   ", df["Birth Year"].max())
        print("Most common year of birth:   ", df["Birth Year"].mode()[0])

    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    min_limit = 0
    max_limit = 5
    response = input('Do you want to see raw data? yes/no')
    if response.lower() == 'yes':
        print(df.iloc[min_limit:max_limit, :])
        while True:
            response = input('Do you want to see more 5 lines of raw data?')
            if response.lower() == 'yes':
                # increase the limits
                min_limit = max_limit
                max_limit += 5
                print(df.iloc[min_limit:max_limit, :])
            else:
                break


def main():
    while True:
        city, month, day = get_filters()
        print(city + " " + month + " " + day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
