Download the "project" folder and run the below commands:

Windows (Anaconda)
Note:
venv\Scripts\activate # For venv environment activation windows  

# 1️⃣ Create a new conda environment with Python 3.10
conda create -n xgb-flask-env python=3.10 -y

# 2️⃣ Activate the environment
conda activate xgb-flask-env

# 3️⃣ Install dependencies from requirements.txt
pip install -r requirements.txt

# 4️⃣ Go to your project folder
cd C:\path\to\your\project

# 5️⃣ Run the Flask app
python index.py


# once setup complete to run again (server):

cd C:\path\to\your\project
python index.py
