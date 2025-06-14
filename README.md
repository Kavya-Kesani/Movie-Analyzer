# 🎬 Movie Rating Analyzer

A Python-based movie analysis tool that reads a `movies.csv` file and offers data exploration and visualization features including **bar charts**, **pie charts**, and **line graphs**. It enables users to view top-rated movies, filter by genre or rating, and visualize trends using `pandas` and `matplotlib`.

---

## 📁 Project Structure

Movie-Rating-Analyzer

├── analyzer.py      # Python script for movie analysis  
├── movies.csv       # Dataset of Telugu movies  
└── README.md        # Instructions and details

---

## 🐍 Requirements

- Python 3.13 or higher  
- Visual Studio Code (optional but recommended)

---

## 🛠️ Setup Instructions (Windows)

### 1. 📥 Install Python

Download and install Python from: https://www.python.org/downloads/

> ✅ **Note:** During installation, ensure the checkbox  
> **"Add Python to PATH"** is selected.

---

### 2. 📁 Open Project Folder in VS Code

Use **Terminal > New Terminal** inside VS Code or open PowerShell:

```powershell
cd path\to\your\Movie-Rating-Analyzer
```

---

### 3. 📦 Create a Virtual Environment

```powershell
python -m venv myenv
```

> ⚠️ If you face a `venvlauncher.exe` copy error, reinstall Python  
> and ensure it's fully installed with all components.

---

### 4. 🔄 Activate Virtual Environment

Use the batch file to bypass PowerShell script policy issues:

```powershell
myenv\Scripts\activate.bat
```

---

### 5. 📚 Install Required Libraries

```powershell
pip install pandas matplotlib
```

---

### 6. ▶️ Run the Application

```powershell
python analyzer.py
```

---

## 📊 Features & Menu Options

Once the script is running, you'll see a menu like:

```
🎬 Movie Rating Analyzer
1. Top N Rated Movies
2. Genre-wise Average Rating
3. Movies Released per Year (Bar Chart)
4. Genre Distribution (Pie Chart)
5. Average Rating by Year (Line Chart)
6. Filter by Minimum Rating
7. Filter by Genre
8. Exit
```

---

## ✨ What Each Option Does

- **Top N Rated Movies** – Input how many top-rated movies you want to see  
- **Genre-wise Average Rating** – Displays average rating per genre  
- **Bar Chart** – Number of movies released per year  
- **Pie Chart** – Genre distribution across dataset  
- **Line Chart** – Year-wise average rating trend  
- **Minimum Rating Filter** – Show movies with rating above a certain threshold  
- **Genre Filter** – View all movies in a particular genre (e.g., Action, Drama, Romance)  
- **Exit** – Close the program

---

## 🧾 Dataset (movies.csv)

This file includes columns:

- `Title`: Movie name  
- `Genre`: Genre (e.g., Drama, Romance, Action)  
- `Rating`: IMDb-like rating  
- `Year`: Year of release  

Example entry:

```
Murari,Drama,7.6,2001
```

---

## 📸 Sample Visual Output

- **Bar Chart**: Year vs. Number of Movies  
- **Pie Chart**: Genre Proportion  
- **Line Chart**: Average Rating Trend Over Years  

---

## 🚫 Troubleshooting

- **ModuleNotFoundError**: Activate the environment before running:
  ```powershell
  myenv\Scripts\activate.bat
  ```

- **Pip not recognized**: Ensure Python is added to your system PATH

- **Script execution disabled**: Use `.bat` instead of `.ps1` to activate

---

## 🤝 Contribution

Feel free to fork, improve, or suggest features via pull requests or issues.

---

## 📬 Contact

**Developed by K.Kavya**  
🎓 Student, SRM University AP  
💡 Enthusiastic about data analysis and visualization with Python  
📧 Connect with me via Gmail: [kavyarambabu232@gmail.com](mailto:kavyarambabu232@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/kavya-kesani-700a51292](https://www.linkedin.com/in/kavya-kesani-700a51292)


---

## 🏷️ License

This project is open-source and free to use for educational or personal purposes.
