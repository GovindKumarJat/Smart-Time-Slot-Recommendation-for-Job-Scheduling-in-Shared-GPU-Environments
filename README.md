# Smart Time Slot Recommendation for Job Scheduling in Shared GPU Environments

## 📌 Overview
**Smart Time Slot Recommendation** is a system designed to optimize job scheduling in shared GPU environments by predicting the most efficient time slots for job execution.  
It leverages **historical workload data**, **GPU utilization trends**, and **machine learning models** to recommend slots that minimize **queue wait time** and **resource contention**.

This project is aimed at improving the **throughput**, **resource utilization**, and **user satisfaction** in multi-tenant GPU clusters — particularly useful for **AI/ML workloads** in research labs, cloud environments, and data centers.

---

## 🚀 Features
- 📊 **Historical Data Analysis** – Monitors past GPU usage and job completion times.
- 🧠 **Machine Learning Recommendation Engine** – Predicts optimal time slots based on workload patterns.
- ⏳ **Reduced Queue Waiting Time** – Suggests time slots when GPUs are likely to be free.
- 🌐 **Support for Multi-User Environments** – Designed for shared GPU clusters.
- 📈 **Visualization Dashboard** – Displays utilization trends and recommendations.
- ⚡ **Scalable & Modular Design** – Can be integrated with existing job scheduling systems like **Slurm**, **Kubernetes**, or **HTCondor**.

---

## 🛠️ Tech Stack
- **Programming Language**: Python 3.10
- **Machine Learning**: Scikit-learn / XGBoost / LightGBM
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Backend Scheduling Integration**: Slurm / Kubernetes API
- **Deployment**: Docker, REST API (Flask/FastAPI)
---

## ✅ Steps to run Project

Download the "project" folder and run the below commands:

Windows (Anaconda)
Note:
venv\Scripts\activate # For venv environment activation windows  

### 1️⃣ Create a new conda environment with Python 3.10
conda create -n xgb-flask-env python=3.10 -y

### 2️⃣ Activate the environment
conda activate xgb-flask-env

### 3️⃣ Install dependencies from requirements.txt
pip install -r requirements.txt

### 4️⃣ Go to your project folder
cd C:\path\to\your\project

### 5️⃣ Run the Flask app
python index.py


# once setup complete to run again (server):

- cd C:\path\to\your\project 
- python index.py
