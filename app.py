from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

# Excel file path
USERS_FILE = 'users.csv'

# Role definitions
ROLES = {
    '1': 'Administrator',
    '2': 'Investor',
    '3': 'Researcher'
}

def load_users():
    """Load users from Excel file"""
    try:
        if not os.path.exists(USERS_FILE):
            flash(f'Error: {USERS_FILE} not found. Please run create_users.py first.', 'error')
            return pd.DataFrame()
        
        df = pd.read_excel(USERS_FILE, engine='openpyxl')
        return df
    except Exception as e:
        flash(f'Error loading users database: {str(e)}', 'error')
        return pd.DataFrame()

def authenticate_user(username, password, role_id):
    """Authenticate user against Excel database"""
    try:
        users_df = load_users()
        
        if users_df.empty:
            return None
        
        # Find user with matching credentials
        user = users_df[
            (users_df['username'].str.strip() == username.strip()) & 
            (users_df['password'].astype(str).str.strip() == password.strip()) & 
            (users_df['role_id'] == int(role_id)) &
            (users_df['active'] == True)
        ]
        
        if not user.empty:
            return user.iloc[0].to_dict()
        
        return None
    except Exception as e:
        flash(f'Authentication error: {str(e)}', 'error')
        return None

@app.route('/')
def index():
    """Redirect to login page"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        role_id = request.form.get('role', '').strip()
        
        # Validate inputs
        if not username or not password or not role_id:
            flash('Please fill in all fields', 'error')
            return render_template('login.html', roles=ROLES)
        
        # Authenticate user
        user = authenticate_user(username, password, role_id)
        
        if user:
            # Create session
            session.permanent = True
            session['user_id'] = int(user['user_id'])
            session['username'] = str(user['username'])
            session['email'] = str(user['email'])
            session['role'] = str(user['role'])
            session['role_id'] = int(user['role_id'])
            session['department'] = str(user['department'])
            
            flash(f'Welcome back, {user["username"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Please check your username, password, and role.', 'error')
            return render_template('login.html', roles=ROLES)
    
    # GET request
    return render_template('login.html', roles=ROLES)

@app.route('/dashboard')
def dashboard():
    """Dashboard page - requires authentication"""
    if 'user_id' not in session:
        flash('Please login to access the dashboard', 'warning')
        return redirect(url_for('login'))
    
    user = {
        'user_id': session.get('user_id'),
        'username': session.get('username'),
        'email': session.get('email'),
        'role': session.get('role'),
        'department': session.get('department')
    }
    
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    """Logout user"""
    username = session.get('username', 'User')
    session.clear()
    flash(f'Goodbye, {username}! You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/minerals')
def minerals():
    """Minerals database page"""
    if 'user_id' not in session:
        flash('Please login to access this page', 'warning')
        return redirect(url_for('login'))
    
    flash('Minerals database coming soon!', 'info')
    return redirect(url_for('dashboard'))

@app.route('/map')
def map_view():
    """Interactive map page"""
    if 'user_id' not in session:
        flash('Please login to access this page', 'warning')
        return redirect(url_for('login'))
    
    flash('Interactive map coming soon!', 'info')
    return redirect(url_for('dashboard'))

@app.route('/analytics')
def analytics():
    """Analytics page"""
    if 'user_id' not in session:
        flash('Please login to access this page', 'warning')
        return redirect(url_for('login'))
    
    flash('Analytics dashboard coming soon!', 'info')
    return redirect(url_for('dashboard'))

@app.route('/reports')
def reports():
    """Reports page"""
    if 'user_id' not in session:
        flash('Please login to access this page', 'warning')
        return redirect(url_for('login'))
    
    flash('Reports section coming soon!', 'info')
    return redirect(url_for('dashboard'))

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    flash('Page not found', 'error')
    return redirect(url_for('dashboard') if 'user_id' in session else url_for('login'))

@app.errorhandler(500)
def internal_error(e):
    """500 error handler"""
    flash('Internal server error occurred', 'error')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Check if users file exists
    if not os.path.exists(USERS_FILE):
        print(f"\n⚠️  WARNING: {USERS_FILE} not found!")
        print("Please run: python create_users.py\n")
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)