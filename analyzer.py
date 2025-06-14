import pandas as pd
import matplotlib.pyplot as plt
try:
    df = pd.read_csv('movies.csv')  
except Exception as e:
    print(f"❌ Error loading CSV file: {e}")
    exit()
df.columns = df.columns.str.strip() 
df.columns = df.columns.str.capitalize() 
if 'Rating' in df.columns:
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
else:
    print("❌ 'Rating' column not found. Please check the CSV.")
    exit()
if 'Year' in df.columns:
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df.dropna(subset=['Year'], inplace=True)
    df['Year'] = df['Year'].astype(int)
else:
    print("❌ 'Year' column not found. Please check the CSV.")
    exit()
def top_n_movies():
    n = int(input("🔢 Enter number of top rated movies to display: "))
    top_movies = df.sort_values(by='Rating', ascending=False).head(n)
    print("\n🎬 Top Rated Movies:\n")
    print(top_movies[['Title', 'Genre', 'Rating', 'Year']])
def genre_avg_rating():
    avg_rating = df.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
    print("\n📊 Average Rating by Genre:\n")
    print(avg_rating)
def movies_per_year_chart():
    count = df['Year'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    bars = plt.bar(count.index.astype(str), count.values, color=plt.cm.viridis(range(len(count))))
    plt.title('🎥 Movies Released Per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def genre_pie_chart():
    genre_counts = df['Genre'].value_counts()
    plt.figure(figsize=(7, 7))
    genre_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title('📊 Genre Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
def avg_rating_by_year_chart():
    avg_by_year = df.groupby('Year')['Rating'].mean()
    plt.figure(figsize=(10, 5))
    plt.plot(avg_by_year.index, avg_by_year.values, marker='o', linestyle='-', color='green')
    plt.title('📈 Average Movie Rating by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Rating')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def filter_by_min_rating():
    min_rating = float(input("⭐ Enter minimum rating to filter movies: "))
    filtered = df[df['Rating'] >= min_rating]
    print(f"\n🎬 Movies with rating ≥ {min_rating}:\n")
    print(filtered[['Title', 'Genre', 'Rating', 'Year']])
def filter_by_genre():
    genre = input("🎭 Enter genre to filter: ").capitalize()
    filtered = df[df['Genre'].str.capitalize() == genre]
    if not filtered.empty:
        print(f"\n🎬 Movies in Genre: {genre}\n")
        print(filtered[['Title', 'Rating', 'Year']])
    else:
        print(f"\n⚠️ No movies found in genre '{genre}'.")
def display_menu():
    print("\n🎬 Movie Rating Analyzer")
    print("1. Top N Rated Movies")
    print("2. Genre-wise Average Rating")
    print("3. Movies Released per Year (Bar Chart)")
    print("4. Genre Distribution (Pie Chart)")
    print("5. Average Rating by Year (Line Chart)")
    print("6. Filter by Minimum Rating")
    print("7. Filter by Genre")
    print("8. Exit")
while True:
    display_menu()
    choice = input("🔘 Choose an option (1-8): ")
    if choice == '1':
        top_n_movies()
    elif choice == '2':
        genre_avg_rating()
    elif choice == '3':
        movies_per_year_chart()
    elif choice == '4':
        genre_pie_chart()
    elif choice == '5':
        avg_rating_by_year_chart()
    elif choice == '6':
        filter_by_min_rating()
    elif choice == '7':
        filter_by_genre()
    elif choice == '8':
        print("👋 Exiting... Have a great day!")
        break
    else:
        print("❌ Invalid choice. Try again.")