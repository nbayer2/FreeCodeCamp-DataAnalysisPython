import pandas as pd
import numpy as np
df = pd.read_csv('adult.data.csv')
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    total=len(df.age)


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(np.array([len(df.loc[df.race=='White']),
                              len(df.loc[df.race=='Black']),
                              len(df.loc[df.race=='Asian-Pac-Islander']),
                              len(df.loc[df.race=='Amer-Indian-Eskimo']),
                              len(df.loc[df.race=='Other'])]),
                              index=['White','Black','Asian-Pac-Islander','Amer-Indian-Eskimo','Other'])

    # What is the average age of men?
    average_age_men = round(df.loc[df.sex=='Male','age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df.loc[df.education=='Bachelors'])/total*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df.education=='Bachelors')|(df.education=='Masters')|(df.education=='Doctorate'),['education','salary']]
    lower_education = df.loc[(df.education!='Bachelors')&(df.education!='Masters')&(df.education!='Doctorate'),['education','salary']]
    
    # percentage with salary >50K
    higher_education_rich = round(len(higher_education.loc[higher_education.salary=='>50K'])/len(higher_education)*100,1)
    lower_education_rich = round(len(lower_education.loc[lower_education.salary=='>50K'])/len(lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week']==min_work_hours,['hours-per-week','salary']]
    rich_percentage = round(len(num_min_workers.loc[num_min_workers.salary=='>50K'])/len(num_min_workers)*100,1)
    
    
    
    # What country has the highest percentage of people that earn >50K?
    rich_country=df.loc[df.salary=='>50K',['native-country','salary']]
    y=rich_country['native-country'].value_counts()
    x=df['native-country'].value_counts()
    df2=pd.merge(y, x, left_index=True, right_index=True)
    df2.columns={'rich in country', 'total population in df'}
    df2['perc_rich']=round(df2['rich in country']/df2['total population in df']*100,1)
    df2=df2.sort_values('perc_rich',ascending=False)
    highest_earning_country = df2.index[0]
    highest_earning_country_percentage = df2['perc_rich'][0]

    # Identify the most popular occupation for those who earn >50K in India.
    india_prof=df.loc[(df['native-country']=='India')&(df.salary=='>50K'),['native-country','occupation','salary']]
    z=india_prof.occupation.value_counts()
    top_IN_occupation =  z.index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
