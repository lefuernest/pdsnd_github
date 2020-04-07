import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv','new york': 'new_york_city.csv','washington': 'washington.csv' }
MONTHS = {'january': 1,'february': 2,'march': 3,'april': 4,'may': 5,'june': 6,
         'jan': 1,'feb': 2,'mar': 3,'apr': 4,'may': 5,'jun': 6}

DAYS = {'monday': 0,'tuesday': 1,'wednesday': 2,'thursday': 3,'friday': 4,'saturday': 5,'sunday': 6,
        'mon': 0,'tues': 1,'wed': 2,'thur': 3,'fri': 4,'sat': 5,'sun': 6}

def get_filters(): #edited code
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! ')
  
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('Choose city to explore')
        city = input('Enter Chicago, New York or Washington \n ').lower()
        if city not in CITY_DATA:
           print('Kindly enter a valid city\n')
           continue
        city = CITY_DATA[city]
        break
    while True:
        # TO DO: get user input for month (all, january, february, ... , june)
          month = 'all'
          print('Now, choose the month you want to explore ')
          month = input('January/jan, February/feb, March/mar, April/apr, May, June/jun \n').lower()
          if month not in MONTHS:
              print('Invalid input, Enter') 
              print('all-for none','january','february','march','april','may','june ')
              continue
          month = MONTHS[month]
          # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
          day = 'all'
          print('Finally, choose the day you want to explore, Enter ')
          day = input('Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun \n').lower()
          if day not in DAYS:
              print('invalid Input, Enter') 
              print('all-for none','Monday/mon, Tuesday/tues, Wednesday/wed, Thursday/thur, Friday/fri, Saturday/sat, Sunday/sun\n')
              continue
          day = DAYS[day]                
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
    df = pd.read_csv(city)
    
     # convert the Start Time column to datetime    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    #temporary_df = pd.read_csv(city)
    # TO DO: display the most common month
    most_freq_month = df['month'].mode()[0]
    for num in MONTHS:
        if MONTHS[num]==most_freq_month:
            most_freq_month = num.title()
    print('The most common month for travel is {}'.format(most_freq_month))

    # TO DO: display the most common day of week
    most_freq_day = df['day_of_week'].mode()[0]
    for num in DAYS:
        if DAYS[num]==most_freq_day:
            most_freq_day = num.title()
    print('The most common day of week for travel is {}'.format(most_freq_day))

    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_freq_hour = df['hour'].mode()[0]
    print('The most common hour for travel is {}'.format(most_freq_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # replaced print() with \n
    print('The most commonly used start station :{}\n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station

    print('Most commonly used end station :{}\n'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
 
    #TO DO: display most frequent combination of start station and end station trip
    x = str(df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False))
    x = x.replace('(', '').replace(')', '').replace("'", '')
    print('Most frequent combination of start and end station: ',x.strip())
    
    frequent_trip_from_start_to_end = df.groupby(["Start Station", "End Station"]).size().max()
    print('Most Common Trip From Start to End:', frequent_trip_from_start_to_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time

    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :",mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n",user_counts)
    
    # TO DO: Display counts of gender
    # if `some_column` exist. Do your computation here //edited code.
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n",gender_counts)
    else:
        #if `some_column` is not present in the dataframe.
        print("No gender information for the input:\n")
   
    # TO DO: Display earliest, most recent, and most common year of birth
    
    # if `some_column` exist. Do your computation here// edited code.
    if 'Birth Year' in df.columns: 
        birth_year = df["Birth Year"].value_counts()
        print("Counts of gender:\n",birth_year)
    
        most_common_year = birth_year.mode()
        print("The most common birth year:", most_common_year)

        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year) 
    else:
        # IF `some_column` is not present in the dataframe.
        print("No Birth times information for the input city:\n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):  #edited code
    
    
    #TO DO: display five rows of data upon user's request
    index = 0
    user_input = input('would you like to view 5 rows of raw data?, Yes or No\n')
    while True:
          print(df.iloc[index : index + 5])
          index += 5
          user_input = input('would you like to view 5 rows of raw data?,  Yes or No\n')
          if user_input == 'yes' or user_input == 'y':
             continue
          elif user_input == 'no' or user_input =='n':
              break  
          else:
              print('Invalid Input. Please try that again!. ')
              break

def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()

        if restart != 'yes' and restart != 'y' and restart != 'yus':
            break

if __name__ == "__main__":
	main()