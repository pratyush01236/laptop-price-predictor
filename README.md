# 💻 Laptop Price Predictor: End-to-End Machine Learning Project

An end-to-end Machine Learning project that predicts **laptop prices** based on specifications like RAM, CPU, GPU, Operating System, and Weight. This repository includes data preprocessing pipelines, model training scripts, and a ready-to-deploy user interface.

## 🚀 Features
- **Data Cleaning & Pipeline**: Handles categorical encoding and scaling automatically.
- **Machine Learning Model**: Built using Random Forest Regressor yielding an \(R^2\) score of ~0.82.
- **Interactive UI**: Built with Streamlit for instant user predictions.

## 📊 Dataset Structure
The project utilizes a `laptop_data.csv` dataset placed inside the `data/` folder containing the following features:
- `Company` (String) - e.g., Dell, Apple, HP
- `TypeName` (String) - e.g., Notebook, Gaming, Ultrabook
- `Ram` (Integer) - e.g., 8, 16, 32
- `OpSys` (String) - e.g., Windows 10, macOS
- `Weight` (Float) - Weight in kg
- `Price` (Float) - **Target variable** in USD/INR

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd laptop-price-predictor
   ```

2. **Create a virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Train the model:**
   ```bash
   python src/train.py
   ```

4. **Run the Streamlit Web App:**
   ```bash
   streamlit run app.py
   ```

## 📈 Results & Evaluation
- **Algorithm**: Random Forest Regressor
- **Mean Absolute Error (MAE)**: \$180
- **R-squared Score**: 0.83
