import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['january', 'feburary', 'march', 'april', 'may', 'june', 'all']
Days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all' ]

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
    while True:
        city = input('Enter the name of city to analyse chicago, new york city, washington: ').strip().lower()
        if city not in CITY_DATA:
            input("\ninvalid city. try again\n")
            continue
        else:
            break

    while True:
        month = input ("Enter the month to analyse january, feburary, march, april, may, june or all: ").lower()
        if month not in Months:
            input("\ninvalid month. try again\n")
            continue
        else:
            break

    while True:
        day = input ("Enter the day to analyse monday, tuesday, wednesday, thursday, friday, saturday, sunday or all: ").lower()
        if day not in Days:
            input('\n invalid day. try again\n')
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print('Popular_month: {}'.format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print(popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print(popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station'] = df['Start Station'] + ' to '+ df['End Station']
    print(df['combination_station'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print(Total_travel_time)


    # TO DO: display mean travel time
    Average_travel_time = df['Trip Duration'].mean()
    print(Average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        Gender_count = df['Gender'].value_counts()
        print(Gender_count)
    else:
        print('No gender found')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('No Birth Year in this city')

    else:
        earliest_birth_year = df['Birth Year'].min()
        print(earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print(most_recent_birth_year)
        common_birth_year = df['Birth Year'].mode()[0]
        print(common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_load(df):
    """Displays some raw data."""

    # TO DO: Display some raw data
    data_load = input('\nWould you like to view some data?\nPlease enter yes or no\n').lower()
    pd.set_option('display.max_rows',200)
    if data_load in ('yes', 'y'):
        n = 0
        while True:
            print(df.iloc[n:n+5])
            n+=5
            more_data = input('\nWould you like to view more data?\nPlease enter yes or no\n').lower()
            if more_data not in ('yes','y'):
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_load(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
