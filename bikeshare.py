import time
import pandas as pd
import numpy as np
import random

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
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            # a try, execpt block was used to handle invalid user inputs
            city_list = ['chicago', 'new york city', 'washington']
            #Prompting the user tp input a city only from the selected group
            city = str(input("Please specify which city would you like to see data for? Choose from 'Chicago, New York City, or Washington':\n\n").lower())
            if city not in city_list:
                raise KeyError
                #if the city entered is not in the list, an error is raised
       
        except KeyError as CityError:
            print("\nSorry, we don't have this data yet!. ")
            continue
            #after the previous message, it goes back automatically to the beginning of the loop
        
        else:
            break
                
              
    while True:
        try: 
            # TO DO: get user input for month (all, january, february, ... , june)  
            month_list = ['all', 'january','february','march','april','may','june']
            #Prompting the user tp input a month only from the selected group
            month = str(input("Please select a month from 'January to June' to filter by, or type 'all' to display them all:\n\n").lower()) # making sure that whatever the user inputs, it is converted to lowercase
            if month not in month_list:
                raise KeyError
                
        except KeyError as MonthError:
            print("\nError. Invalid month spelling. ")
            continue
                #of month is not in the list, a error message is printed and the user is brought back to the                    beginning of the loop 
        else:
            break
        
    while True: # TO DO: get user input for day of week (all, monday, tuesday,       day)
        try:
            #a try, except block was used to handle invalid inputs
            day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            #Prompting the user tp input a city only from the selected group
            day = str(input("Please select a day to filter by, or just type 'all' to display the whole week:\n\n").lower()) # making sure that whatever the user inputs, it is converted to lowercase
            if day not in day_list:
                raise KeyError
                #if the day is not in the list, we raise an error message
                
            
        except KeyError as DayError:
                    print("\nError. Invalid day spelling. ")
                    continue
                
        
        else:
            break
            # if no invalid errors occured, we exit the loop
                                    
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
    

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extracting the hours from Start Time to create new column 'hour'
    df['hour'] = df['Start Time'].dt.hour
    #df['Updated Birth Year'] = df['Birth Year'].astype(int)

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
    else:
         #if the user inputs 'all' we display no filter
        df['month'] = df['Start Time'].dt.month
        

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    else:
        #if the user inputs 'all' we display no filter
        df['day_of_week'] = df['Start Time'].dt.weekday_name
             
            
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nCalculating The Most Common Month...')
    #calculating the most common month using mode()
    print('The Most Common Month is: {}.'.format(df['month'].mode()[0]))


    # TO DO: display the most common day of week
    print('\nCalculating The Most Common Day...')
    #calculating the most common day using mode()
    print('The Most Common Day is: {}.'.format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print('\nCalculating The Most Common Sart Hour...')
    #calculating the most common start hour using mode()
    print('The Most Common Start Hour is: {}.'.format(df['hour'].mode()[0]))


    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The Most Commonly Used Start Station is: {}.\n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The Most Commonly Used End Station is: {}.\n'.format(df['End Station'].mode()[0]))

    
    # TO DO: display most frequent combination of start station and end station trip
    print('The Most Frequent Combination Of Start Station and End Station is: {}.\n'.format((df['Start Station'] + ' & ' + df['End Station']).mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #craeting a new column to calculate the difference between the end time and start time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    print('\nThe Total Travel Time is: {}'.format(df['Travel Time'].sum()))

    # TO DO: display mean travel time
    print('\nThe Mean Travel Time is: {}'.format(df['Travel Time'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n\nCalculating The Counts of User Type...')
    print('\nThe Counts of User Type are:\n{}.'.format(df['User Type'].value_counts()))

    while True:
        try:
            #use of try, except block to handle if the a dataframe does't contain certain columns
            print('\n\nCalculating The Counts of Gender...')
            if 'Gender' not in df:
                #if the Gender column doesn't exist, an error message is raised
                raise KeyError
                
        except KeyError as GenderColumnDoesNotExist:
            
            print('\nOOPS.. It Seems That This City Doesn\'t Have Data on Gender. ')
            while True:
                """ here I created a while loop to handle invalid inputs from the user..
                for example if the user just typed random letters, the program will not
                crash, and It only allows the user to either type 'yes' or 'no'
                which result in an unbreakable code
                """
                # after the error message, the user is asked if they want to continue
                restart_now = input('Would you like to quit? Enter \'yes\' or \'no\'.\n')
                if restart_now.lower() == 'yes':
                    quit()  #if the user types 'yes' the program ends
                    
                    
                elif restart_now.lower() == 'no':
                    break  # if the user types 'no' the program exits the 'first loop' and continues.
                          
                else:
                    print("\nYour input is invalid! ")
                    continue    #if the user enters anything else, the program outputs an Error message and                                     takes them back to the earlier loop
                  
            
        else:   
            # TO DO: Display counts of gender
            #if no errro presists, the code carries on in the else block
            print('The Counts of Gender are:\n{}.'.format(df['Gender'].value_counts()))

            # TO DO: Display earliest, most recent, and most common year of birth   

        try:
            #another try statement to handle anoth column. in this case.. Birth Year
            print('\n\nCalculating Earliest Year of Birth...')
            if 'Birth Year' not in df:
                #if the Gender column doesn't exist, an error message is raised
                raise KeyError
                
        except KeyError as BirthYearColumnDoesNotExist:
            
            print('\nOOPS.. It Seems That This City Doesn\'t Have Data on Birth Year. ')
            while True:
                """ here I created a while loop to handle invalid inputs from the user..
                for example if the user just typed random letters, the program will not
                crash, and It only allows the user to either type 'yes' or 'no'
                which result in an unbreakable code
                """
                # after the error message, the user is asked if they want to continue
                quit_now = input('Would you like to quit? Enter \'yes\' or \'no\'.\n')
                if quit_now.lower() == 'yes':
                    quit()  #if the user types 'yes' the program ends
                    
                    
                elif quit_now.lower() == 'no':
                    return  # if the user types 'no' the program exits the '2 loops' and continue on
                          
                else:
                    print("\nYour input is invalid! ")
                    continue    #if the user enters anything else, the program outputs an Error message and                                     takes them back to the earlier loop
                    
                    
                    
            #Displaying the Earliest Year of Birth...
        else:
            # if no error occured, the code carries on
            #dropping the non-finite values (NA of inf)
            #df['Birth Year'] = df[df['Birth Year'].dropna(axis=0)]
            # converting the Birth Year column to integer
            #df['Birth Year'] = df[df['Birth Year'].astype(int)]
            #df['Updated Birth Year'] = df[df['Birth Year'].astype('int', errors='ignore')]
            #df['NAN Birth Year'] = df['Birth Year'].fillna(0)
            #df['Updated Birth Year'] = df['NAN Birth Year'].astype('int', errors='ignore')
            #df['Updated Birth Year'] = df['NAN Birth Year'].astype(int)
            print('The Earliest Birth Year is: {}'.format(df['Birth Year'].min()))
    
            #Dispalying The Most Recent Year Of Birth...
            print('\n\nCalculating Most Recent Year of Birth...')
            print('The Most Recent Birth Year is: {}'.format(df['Birth Year'].max()))
    
            #Displaying the Most Common Year Of Birth...
            print('\nCalculating Most Common Year of Birth...')
            print('The Most Common Birth Year is: {}'.format(df['Birth Year'].mode()[0]))
            break
    

    print("\n\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ in this function the user is asked whether they want to see random trip data, if the user chooses             'yes' we display each time 5 rows, with 6 most important columns of the data set, if the chosen city           at beginnig has NAN values, swe could use the .dropna(axis=0) to delete all the NANs, but this would           also delete the whole dataframe if the a whole column doesn't exist, like
        in 'Washington' dataframe, so fillna(0) is the better option here.
        
        I tried using the random.randint to output random 5 rows each time, but for some reason It                     only worked when applying no filter...
    """
    # TO DO: convert the user input to lower case using lower() function
    
    #i = random.randint(0, data_frame_size) # a random int generator
    i = 5
    raw = str(input("\nWould you like to see random individual trip data? Type 'yes' or 'no':\n").lower())
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            if df.empty == True:
                print('DataFrame is Empty')
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            print(df.loc[0:i, ['User Type', 'Gender', 'Birth Year', 'Travel Time', 'Start Station', 'End Station']].fillna(0))
                
            # TO DO: convert the user input to lower case using lower() function
            raw = str(input("\nWould you like to see random individual trip data? Type 'yes' or 'no':\n").lower())
            i += 5
               
        else:
            raw = str(input("\nYour input is invalid! Please enter only 'yes' or 'no'\n").lower())
            # the loop keeps asking the user to input the right word, and doesn't crash the program
            
                    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        
        while True:
            """ here I created a while loop to handle invalid inputs from the user..
                for example if the user just typed random letters, the program will not
                crash, and It only allows the user to either type 'yes' or 'no'
                which result in an unbreakable code.
            """
            restart = str(input('Program Ended!. Would you like to run it again? Enter yes or no.\n').lower())
            if restart == 'no':
                quit()      #if user types 'no' the program ends.
                    
            elif restart == 'yes':
                break
                continue    # if user types 'yes', we break out of the inner while loop, and reach for the                                  bigger one at the begginning of the main() function
                
                    
            elif restart != 'yes' or restart != 'no':
                print("\nYour input is invalid. ")
                continue    #if user doesn't type either of those, the program keeps on going, and asks the                                 user to type the right answer
                

if __name__ == "__main__":
	main()
