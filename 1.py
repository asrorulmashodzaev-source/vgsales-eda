import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:\Users\VICTUS\Desktop\vgsales.csv')


# Clean data - drop missing values
df = df.dropna(subset=['Year', 'Publisher'])
df['Year'] = df['Year'].astype(int)

# Top 10 genres by global sales
top_genres = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='Blues_r')
plt.title('Top 10 Genres by Global Sales (millions)', fontsize=14)
plt.xlabel('Global Sales (millions)')
plt.ylabel('Genre')
plt.tight_layout()
plt.savefig('top_genres.png')
plt.show()

print("Done!")


# Sales trend by year
yearly_sales = df.groupby('Year')['Global_Sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_sales, x='Year', y='Global_Sales', color='steelblue', linewidth=2.5)
plt.title('Global Video Game Sales by Year', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Global Sales (millions)')
plt.tight_layout()
plt.savefig('sales_by_year.png')
plt.show()

print("Done!")



# Top 10 platforms
top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_platforms.index, y=top_platforms.values, palette='viridis')
plt.title('Top 10 Platforms by Global Sales (millions)', fontsize=14)
plt.xlabel('Platform')
plt.ylabel('Global Sales (millions)')
plt.tight_layout()
plt.savefig('top_platforms.png')
plt.show()

print("Done!")