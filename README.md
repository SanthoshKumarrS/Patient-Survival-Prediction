# Patient-Survival-Prediction
In this repository, I've developed a Deep Neural Network model to predict patient survival. The main evaluation metric for the model is Recall. 

**🧾Description:** Getting a rapid understanding of the context of a patient’s overall health has been particularly important during the COVID-19 pandemic as healthcare workers around the world struggle with hospitals overloaded by patients in critical condition. Intensive Care Units (ICUs) often lack verified medical histories for incoming patients. A patient in distress or who is brought in confused or unresponsive may not be able to provide information about chronic conditions such as heart disease, injuries, or diabetes. Medical records may take days to transfer, especially for a patient from another medical provider or system. Knowledge about chronic conditions can inform clinical decisions about patient care and ultimately improve patient survival outcomes.

**Source of the dataset:** [Click Here](https://journals.lww.com/ccmjournal/Citation/2019/01001/33__THE_GLOBAL_OPEN_SOURCE_SEVERITY_OF_ILLNESS.36.aspx)

**🧭 Problem Statement:** The target feature is hospital_death which is a binary variable. The task is to classify this variable based on the other 185 features step-by-step by going through each day's task. The scoring metric is Recall.

### Web application:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://patient-survival-prediction-r5zj.onrender.com)

** App may take a minute or 2 to load Since it's deployed in the Freemium server**. 

**Key challenge:** 

1. Large dataset with over 90K rows and 186 columns.
2. Lack of significant relations with the target feature

**Data Preprocessing**
- I performed data cleaning and preprocessing Using **Numpy** & **Pandas** to handle missing values, normalize features. 
- Used **One Hot encoding** to encode categorical variables.
- Visualised Data with **Seaborn**,**Matplotlib** & **Plotly**.
- This step ensures the data is suitable for training a machine learning model.

**Model Architecture**
The Deep Neural Network architecture consists of several layers, including densely connected layers and dropout layers to prevent overfitting. The model takes patient information as input and predicts the likelihood of survival.

**Training**
- The model is trained using a training dataset and validated on a separate validation dataset.
- The primary evaluation metric for the model is Recall, which is crucial in medical prediction tasks.
- Basic Model had a recall score of **0.29** & Validation loss was volatile

**Callbacks and Keras Tuner**
- Used Callbacks are used during training to monitor metrics, save model checkpoints, and implement early stopping.
- Utilized Keras Tuner to search for optimal hyperparameters and improve the model's performance.
- Validation loss was Stable and also Improved **Recall score to 0.86**

**Explainable AI with SHAP**
- To provide transparency and explainability to the model's predictions, I used the SHAP library's Deep Explainer.
- This allows us to understand the importance of each feature in the model's decision-making process.
- Also found the important Features of the Model and retrained the Model on the features.

**Streamlit App**
- I developed a user-friendly Streamlit app that allows users to input patient information and get predictions about patient survival.
- The app provides an interactive interface for easy interaction with the model.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://patient-survival-prediction-r5zj.onrender.com)

**Deployment**
The Streamlit app is deployed using the Render service, making it accessible for users to use and interact with the trained model.

Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request.

**License**
This project is licensed under the MIT License.
