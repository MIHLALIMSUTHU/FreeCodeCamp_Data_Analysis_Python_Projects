# demographic_data_analyzer.py

import pandas as pd

df = pd.read_csv("adult.data.csv")

def calculate_demographic_data(print_data=True):
    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1
    )

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').mean() * 100, 1
    )

    country_50k = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts() / df['native-country'].value_counts() * 100
    ).dropna()
    highest_earning_country = country_50k.idxmax()
    highest_earning_country_percentage = round(country_50k.max(), 1)

    india_top_occupation = (
        df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
        ['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': india_top_occupation
    }
