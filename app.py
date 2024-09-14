from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = "c3ee8bab41a39709aee0054d01345f15"  # For session management

@app.route('/')
def index():
    # Get user data from WebApp initData sent by Pyrogram
    init_data = request.args.get('initData', '')
    user_info = {}

    if init_data:
        # Parse initData which contains the user's first name, user id, and username
        user_info = json.loads(init_data)

    return render_template('index.html', user_info=user_info)

@app.route('/farming')
def farming():
    # Check if the user has virtual dollars, if not initialize
    if 'virtual_dollars' not in session:
        session['virtual_dollars'] = 0  # Set initial virtual dollar count to 0
    return render_template('farming.html', virtual_dollars=session['virtual_dollars'])

@app.route('/start_farming', methods=['POST'])
def start_farming():
    # Increment virtual dollars when the button is clicked
    session['virtual_dollars'] += 10  # Example: Add 10 virtual dollars
    return redirect(url_for('farming'))

if __name__ == '__main__':
    app.run(debug=True)
