# 🏡Real Estate Valuation App  

This is a **machine learning-powered web application** that predicts house prices based on user inputs such as bedrooms, bathrooms, square footage, and zip code. It utilizes **Ensemble Regression Models** for high-accuracy predictions.

---

## **🚀 Features**  
✅ Predicts house prices based on real estate features  
✅ Uses **Ensemble Learning (Stacking, Bagging, Boosting)**  
✅ **User-Friendly Web App** with **Streamlit**  
✅ **Responsive & Mobile-Friendly** UI  
✅ **Deployed Online for Easy Access**  

---

## **📌 Tech Stack**  
🔹 **Frontend & UI**: Streamlit  
🔹 **Machine Learning Models**: Random Forest, Gradient Boosting, Stacking Regressor  
🔹 **Backend & Deployment**: Python, Scikit-Learn, Joblib  

---

## **📂 Project Structure**  
📦 House-Price-Prediction 
┣ 📜 app.py # Streamlit Web App 
┣ 📜 model_training.ipynb # ML Model Training Notebook 
┣ 📜 house_price_model.pkl # Trained Model 
┣ 📜 requirements.txt # Required Dependencies 
┗ 📜 README.md # Project Documentation


---

## **🔧 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
# Navigate to your project directory
cd HousePrice_Prediction

# Initialize Git (if not already initialized)
git init

# Add remote repository (Replace 'your-username' and 'new-repo-name')
git remote add origin https://github.com/H4NUM4NTH4/HousePricePrediction_Ensemble.git

# Add all files and commit
git add .
git commit -m "Initial commit with Ensemble Regression models"

# Push the code to GitHub
git branch -M main
git push -u origin main

streamlit run app.py


