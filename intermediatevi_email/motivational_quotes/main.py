# AUTOMATED MOTIVATIONAL EMAIL SENDER
# Purpose: Sends motivational quotes via email specifically on Mondays, using quotes from a text file
# Hints:
# 1 use datetime module to obtain current day
# 2 open the .txt file to obtain the list_quotes of quotes
# 3 Use random module to pick a random quote form list_quotes of quotes.
# 4. Use smtlib to send email 


# 1. GET THE CURRENT DAY OF THE WEEK
import datetime as dt

now = dt.datetime.now() # Prints the current datetime
day_of_week = now.weekday() # [0, 1, 2, 3, 4, 5, 6]


# 2. GET THE LIST OF QUOTES
quotes_file = './quotes.txt'

def get_quotes(filepath):
    """Read quotes from a .txt file and return a cleaned list_quotes.

    Args:
        filepath (str): Path to the text file containing the quotes

    Returns:
        list_quotes: List of quotes with whitespaces removed.
    Raises:
        FileNotFoundError: If the specified file does not exist
        UnicodeDecodeError: If the file is not UTF-8 encoded

    Example:
        >>> quotes = get_quotes(filepath)
        >>> print(quotes[0])
        "Be the change you wish to see in the world"
    """
    with open(filepath, 'r', encoding='utf8') as file:
        raw_quotes = file.readlines()
        return [line.strip() for line in raw_quotes]
         
cleaned_quotes = get_quotes(quotes_file)


# SELECT RANDOM QUOTES
import random

def pick_quote(list_quotes):
    """
    Randomly selects and prints a quote from a list of quotes.

    Args:
        list_quotes (list): A list containing quotes as strings

    Returns:
        str: The randomly selected quote if list is not empty
        None: If the list is empty (Note: prints 'No quotes available')

    Raises:
        IndexError: If list_quotes is an empty sequence

    Example:
        >>> quotes = ["Quote 1", "Quote 2", "Quote 3"]
        >>> selected1 = pick_quote(quotes[3])
        IndexError
        >>> selected2 = pick_quote(quotes)
        Quote 2
        >>> print(selected)
        Quote 2
    """
    if list_quotes: # Check if list is not empty
        daily_quote = random.choice(list_quotes)
        # print(daily_quote)
        return daily_quote
    else:
        print('No quotes available')


# EMAIL SERVER CONNECTION SET UP AND SEND EMAIL
import smtplib

email = 'oil@gmail.com'
to_email = '991@gmail.com'
password = 'rfip iquo fdri dpyn' # Add Password

def send_email(email, password, quote):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        msg = f"Subject:Daily Quote for YOU!\n\nFrase del día:\n\n{quote}"
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=msg.encode('utf-8') # ensures that all characters are properly encoded
            )

if day_of_week == 3:
    daily_quote = pick_quote(cleaned_quotes)
    send_email(email, password, daily_quote)
    
# ------------------------------ SOLUTION --------------------------------
# Daniel M. approach
# 1. Get and save today's date and the day of the week
# 2. open and read the .txt file.
# 3. get the quotes from the file, process them and save them in a list.