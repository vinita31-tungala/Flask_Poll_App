 Flask Poll App 🗳️

This is a simple **Flask web application** for conducting a poll. Users can vote on their favorite programming language, and results are displayed in real-time.

---

 📌 Features

- Interactive voting form.
- Real-time results update.
- Simple, responsive UI using HTML/CSS.
- All data stored in memory (no database used).

---

📁 Project Structure

flask_poll_app/
├── static/
│ └── style.css # CSS file for styling
├── templates/
│ ├── index.html # Voting form page
│ └── results.html # Results display page
├── app.py # Main Flask application
└── README.md # Project documentation

yaml
Copy
Edit

---

 🖥️ Preview

- Home (Voting Page): Displays a question and multiple options.
- Results Page: Shows the number of votes for each option.

---

 🚀 Getting Started

 🔧 Prerequisites

- Python 3.x
- Flask

 ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flask_poll_app.git
   cd flask_poll_app
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\Activate.ps1     # For PowerShell
 OR
venv\Scripts\activate.bat       # For Command Prompt
Install Flask:

bash
Copy
Edit
pip install flask
Run the app:

bash
Copy
Edit
python app.py
Open in browser:

Visit http://localhost:5000

📝 Customization
You can easily change the poll question and options by editing the following lines in app.py:

python
Copy
Edit
question = "What is your favorite programming language?"
options = ["Python", "JavaScript", "Java", "C++"]
