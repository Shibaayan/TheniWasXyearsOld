import datetime as dt

d_dob, m_dob, y_dob = map(int,input("Enter Your Date of Birth in DD MM YYYY format : \n").split())
# d_dob -> takes the date from Date of Birth
# m_dob -> takes the month from Date of Birth
# y_dob -> takes the year from Date of Birth

y_incident, m_incident, d_incident = map(int,input("Enter the Date when the incident happened in YYYY MM DD format : \n").split())
# y_incident -> takes the year from the date of incident
# m_incident -> takes the month from the date of incident
# d_incident -> takes the day from the date of incident

dob = dt.date(y_dob, m_dob, d_dob)
# we're just creating an datetime object here to store date of birth year, month and date

incident = dt.date(y_incident, m_incident, d_incident)
# we're just creating an datetime object here to store date of incident year, month and date

difference = incident - dob

print("Then I was approximately {} years {} months and {} days old.".format(   
        int(difference.days/30/12),
        int(difference.days/30%12),
        int(difference.days%365%30)
    )
)