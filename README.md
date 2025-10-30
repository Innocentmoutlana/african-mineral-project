# african-mineral-project
pip install flask pandas openpyxl
```

## 📦 Installation

### Step 1: Install Visual Studio Code
1. Download VS Code from https://code.visualstudio.com/
2. Run the installer and follow the installation wizard
3. Launch VS Code after installation

### Step 2: Install Live Server Extension
1. Open VS Code
2. Click on the Extensions icon in the sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for "Live Server" by Ritwick Dey
4. Click "Install"
5. Wait for the installation to complete

### Step 3: Clone or Download the Project
1. Download the project files to your local machine
2. Extract the files if downloaded as a ZIP
3. Open VS Code
4. Go to `File > Open Folder`
5. Select the project folder

## 📁 Project Structure
```
african-critical-minerals/
│
├── templates/
│   ├── login.html              # Login page
│   ├── admin_dashboard.html    # Administrator dashboard
│   ├── invest_dashboard.html   # Investor dashboard
│   ├── res_dashboard.html      # Researcher dashboard
│   └── map.html                # Interactive map (if available)
│
├── static/                     # Static files (CSS, JS, images)
│
├── Data Files (CSV):
│   ├── users.csv               # User credentials and roles
│   ├── minerals.csv            # Minerals database
│   ├── countries.csv           # Countries information
│   ├── production_stats.csv   # Production statistics
│   ├── sites.csv              # Mining sites data
│   └── roles.csv              # User roles definitions
│
├── app.py                     # Flask backend (optional)
├── create_users.py            # User creation script (optional)
└── README.md                  # This file
```

## 🚀 Running the Application

### Method 1: Using Live Server (Recommended for HTML files)

1. **Open the Project in VS Code**
```
   File > Open Folder > Select your project folder
