import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str.lower(input('Would you like to see data for Chicago, New York City, or Washington?\n'))

    while True :
        if city in CITY_DATA:
            break
        else:
            city = str.lower(input('please re-enter your city: '))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str.lower(input('Which month? all, january, february, ... , june?\n'))

    while True :
        if month in months:
            break
        else:
            month = str.lower(input('please re-enter your month: '))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str.lower(input('Which day? Please type your day of week (all, monday, tuesday, ... sunday)\n'))

    weeks = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'}
    while True :
        if day in weeks:
            break
        else:
            day = str.lower(input('please re-enter your day: '))

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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    print('Most Popular Month: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Most Popular Day of Week: ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('Most Popular Start Hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # create an popular trip column
    df['trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']

    # TO DO: display most commonly used start station
    print('Most Popular used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Popular used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most Frequent Combination of Start Station and End Station Trip: ', df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time: ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print('Counts of User Types:\n', user_types)

        # TO DO: Display counts of gender
        gender =  df['Gender'].value_counts()
        print('Counts of Gender:\n', gender)
    except KeyError:
        print("There isn't a [Gender] column in this spreedsheet!")

    try:
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The Earliest: ', df['Birth Year'].min())
        print('The Most Recent: ', df['Birth Year'].max())
        print('The Most Common Year of Birth: ', df['Birth Year'].mode())

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except KeyError:
        print("There isn't a [Birth Year] column in this spreedsheet!")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


