import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    """Loads cleaned data from SQLite database."""
    conn = sqlite3.connect("data/raw/job_market.db")
    query = "SELECT * FROM job_salaries"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def plot_salary_distribution(df):
    """Plots the salary distribution."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df['salary_in_usd'], bins=30, kde=True, color='blue')
    plt.title("Salary Distribution")
    plt.xlabel("Salary in USD")
    plt.ylabel("Frequency")
    plt.show()

def plot_experience_vs_salary(df):
    """Plots average salary by experience level."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x='experience_level', y='salary_in_usd', data=df, ci=None, palette='viridis')
    plt.title("Experience Level vs Average Salary")
    plt.xlabel("Experience Level")
    plt.ylabel("Salary in USD")
    plt.show()

def plot_company_size_vs_salary(df):
    """Plots average salary by company size."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x='company_size', y='salary_in_usd', data=df, ci=None, palette='magma')
    plt.title("Company Size vs Average Salary")
    plt.xlabel("Company Size")
    plt.ylabel("Salary in USD")
    plt.show()

def plot_remote_work_impact(df):
    """Plots remote vs onsite job salaries."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='remote_ratio', y='salary_in_usd', data=df, palette='coolwarm')
    plt.title("Remote Work Impact on Salary")
    plt.xlabel("Remote Ratio")
    plt.ylabel("Salary in USD")
    plt.show()

def plot_job_title_vs_salary(df):
    """Plots top job titles by average salary."""
    top_jobs = df.groupby('job_title')['salary_in_usd'].mean().nlargest(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_jobs.values, y=top_jobs.index, palette='plasma')
    plt.title("Top 10 Job Titles by Average Salary")
    plt.xlabel("Average Salary in USD")
    plt.ylabel("Job Title")

def plot_location_vs_salary(df):
    """Plots average salary by job location."""
    top_locations = df.groupby('company_location')['salary_in_usd'].mean().nlargest(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_locations.values, y=top_locations.index, palette='coolwarm')
    plt.title("Top 10 Locations by Average Salary")
    plt.xlabel("Average Salary in USD")
    plt.ylabel("Location")
    plt.show()

def run_eda():
    df = load_data()
    plot_salary_distribution(df)
    plot_experience_vs_salary(df)
    plot_company_size_vs_salary(df)
    plot_remote_work_impact(df)
    plot_job_title_vs_salary(df)
    plot_location_vs_salary(df)


if __name__ == "__main__":
    run_eda()
