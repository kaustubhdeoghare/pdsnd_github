import time
import pandas as pd
import numpy as np
import calendar
import json

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
    #city = input("Enter the City Name you'd like to analyze (chicago, new york city, washington) : ")
    # TO DO: get user input for month (all, january, february, ... , june)
    #month =input("Enter the month for which analysis is required january, february, march, april, may, june: ")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #day = input("Enter the day of the week as monday, tuesday, wednesday, thursday, friday, saturday, sunday : ")

    city_options = ['chicago', 'new york city', 'washington']
    month_options = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    day_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    while True:
        city = input('\nInsert name of the city to analyze! (chicago, new york city, washington) :')
        city = city.lower()
        if city in city_options:
            break
        else:
            print('Your choice is not available. Please try again')

    while True:
        month = input('\nInsert month to filter by or "all" to apply no month filter! (january, february, etc.) :')
        month = month.lower()
        if month in month_options:
            break
        else:
            print('Your choice is not available. Please try again')

    while True:
        day = input('\nInsert day of the week to filter by or "all" to apply no day filter! (monday, tuesday, etc.) :')
        day = day.lower()
        if day in day_options:
            break
        else:
            print('Your choice is not available. Please try again')


    print('-'*100)
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
    # identify the file name
    filename = CITY_DATA.get(city)

    # load data file into a dataframe
    df = pd.read_csv(filename)

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
        df =  df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = calendar.month_name[df['month'].mode()[0]]
    print("The most common Month is : {}".format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of week is : {}".format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common Start Hour is {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is : {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used End Station is : {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df['Start Station'].mode()[0] + ' & ' + df['End Station'].mode()[0]
    print("The most frequent combination of Start & End Station is : {}".format(popular_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time is : {} ".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time is : {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    try :
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        user_types_count = df['User Type'].value_counts()
        print("Count of User Types :\n{} ".format(user_types_count))

        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("\nCounts of Gender :\n{} ".format(gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min().astype(int)
        most_recent_birth_year = df['Birth Year'].max().astype(int)
        most_common_birth_year = df['Birth Year'].mode()[0].astype(int)

        print("\nThe earliest year of birth is : {} ".format(earliest_birth_year))
        print("\nThe most recent year of birth is : {} ".format(most_recent_birth_year))
        print("\nThe most common year of birth is : {} ".format(most_common_birth_year))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

    except KeyError as excp :
        print ("KeyError Exception has occurred for : {}".format(excp))

def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
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
