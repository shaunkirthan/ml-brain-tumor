# Shaun Kirthan

## Project Scoping: Brain Tumor Detection

### I. Introduction
Brain tumors represent a significant health challenge, ranking as the 10th leading cause of death for both men and women. In 2023, approximately 24,810 adults in the United States were diagnosed with brain tumors, and this number is projected to increase to 30,000 per year. Globally, the incidence of primary brain or spinal cord tumors reached 308,102 in 2020. Given the rising prevalence, early and accurate detection is crucial for improving patient outcomes. The complexity of brain tumors, with significant variability in their size, location, and nature, poses challenges in fully understanding and accurately diagnosing them. 

MRI analysis, essential for diagnosis, typically requires the expertise of professional neurosurgeons. However, in developing countries, there is often a shortage of skilled doctors, and the lack of specialized knowledge about tumors can lead to delays and inaccuracies in generating MRI reports. To address these challenges, this project leverages advancements in machine learning (ML) to develop a comprehensive end-to-end ML pipeline. This automated system will assist doctors in diagnosing brain tumors more effectively, especially in regions with limited access to skilled medical professionals. By deploying this system on the cloud, we aim to provide scalable, reliable, and timely diagnostic support, ultimately improving patient outcomes and reducing the burden on healthcare systems.

### II. Dataset Information

#### Dataset Introduction
The dataset for this project combines three sources: figshare, SARTAJ, and Br35H. It consists of MRI images of human brains, categorized into four classes: glioma, meningioma, no tumor, and pituitary. The dataset's purpose is to facilitate the development of a robust model for detecting and classifying brain tumors, supporting medical professionals in making accurate diagnoses.

#### Data Card
- **Dataset Name:** Brain Tumor MRI Images
- **Size:** 7023 images
- **Format:** JPEG
- **Data Types:** MRI images of human brains
- **Classes:** Glioma, Meningioma, No Tumor, Pituitary
- **Source Datasets:** figshare, SARTAJ, Br35H

#### Data Sources
- **figshare Dataset:** [figshare brain tumor dataset](https://figshare.com/articles/dataset/brain_tumor_dataset/1512427)
- **SARTAJ Dataset:** [Kaggle brain tumor classification MRI](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
- **Br35H Dataset:** [Kaggle brain tumor detection](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection?select=no)

#### Data Rights and Privacy
All data used in this project are sourced from publicly available datasets with proper usage permissions. We ensure compliance with data protection regulations.

### III. Data Planning and Splits
Our data preprocessing strategy includes resizing images, normalization, and data augmentation to enhance model generalization. We will split the dataset into training, validation, and test sets in a typical 70-20-10 ratio. Stratified sampling will be used to ensure each class is adequately represented across all splits.

### IV. GitHub Repository
- **URL:** [GitHub - Omii2899/Brain-Tumor-Classification](https://github.com/Omii2899/Brain-Tumor-Classification)
- **Folder Structure:**
  - **README.md:** Includes essential project information, installation instructions, and usage guidelines.
  - **requirements.txt:** Information about the packages and versions required for the project.
  - **src:** All preprocessing and training code will be placed in this folder.
  - **test:** All test files will be placed in this folder.
  - **.gitignore**
  - **.github/workflows:** Includes workflow YAML files to automate build, test, and deployment pipelines.

### V. Project Scope
The objective of this project is to design, develop, and deploy a robust ML pipeline capable of detecting brain tumors from medical imaging data. The pipeline will be user-friendly and scalable, providing valuable insights to healthcare professionals.

#### Key Components of the Project:
- **Data Collection and Preprocessing:** Aggregate a large dataset of brain MRI scans from various sources, ensuring data diversity and quality. Preprocess the images to standardize formats, enhance image quality, and annotate tumors accurately.
- **Model Development:** Utilize state-of-the-art deep learning techniques, such as Convolutional Neural Networks (CNNs), to build and train a model for tumor detection. Experiment with different architectures and hyperparameters to optimize performance.
- **Model Evaluation and Validation:** Implement rigorous evaluation metrics, including accuracy, precision, recall, and F1 score, to assess model performance. Conduct cross-validation and utilize external validation datasets to ensure generalizability.
- **Deployment:** Develop an API and a user-friendly interface for healthcare professionals to upload MRI scans and receive diagnostic results. Ensure the system is secure, scalable, and complies with healthcare regulations.
- **Monitoring and Maintenance:** Establish monitoring tools to track model performance in real-time and detect any degradation in accuracy. Implement mechanisms for continuous learning and model updates based on new data.

#### Challenges:
- **Data Quality and Availability:** Obtaining diverse, high-quality data while navigating privacy regulations is challenging.
- **Model Generalization:** Ensuring consistent performance across different populations and MRI machines is crucial.
- **Computational Resources:** Optimizing resource usage for training deep learning models on large datasets is challenging.
- **Regulatory Compliance:** Adhering to healthcare regulations like HIPAA for patient data privacy and system reliability is essential.

#### Proposed Solutions:
- Implement a CNN-based multi-task classification model to perform detection and classification by type within a single framework.
- Use advanced data augmentation and preprocessing techniques to enhance model performance.
- Integrate the system into a user-friendly interface for clinical use.

### VI. Current Approach Flow Chart and Bottleneck Detection
- **Limited Access to Annotated Data:** High-quality, annotated medical imaging data is scarce, making it difficult to train and validate models effectively.
- **Variability in Imaging Techniques:** Differences in MRI machines and imaging protocols across institutions can lead to variability in the data, affecting model performance.
- **Interpretability of Models:** Deep learning models, especially CNNs, are often seen as black boxes. Improving model interpretability to gain the trust of healthcare professionals is a significant bottleneck.
- **Scalability and Real-Time Processing:** Deploying the model in a clinical setting requires real-time processing capabilities, which can be challenging to achieve without compromising accuracy.

### VII. Metrics, Objectives, and Business Goals

#### Metrics:
- **Precision and Recall:** For each tumor class to measure the model's performance.
- **F1-Score:** Harmonic mean of precision and recall.
- **ROC-AUC:** To evaluate the classifier's performance across different thresholds.

#### Objectives:
- Develop a highly accurate model for brain tumor detection and classification.
- Reduce diagnostic time and support radiologists with reliable AI tools.
- Enhance patient outcomes through early and precise tumor identification.

### VIII. Failure Analysis

#### Potential Risks:
- **Model Overfitting:** Extensive validation can help mitigate this.
- **Data Privacy Breaches:** Regular audits of data handling practices are essential.
- **Hardware Failures During Deployment:** Robust backup systems for deployment infrastructure are necessary.

#### Mitigation Strategies:
- **Misclassification of Non-Tumor Conditions:** Implement measures to handle false positives.
- **Corrupted File Uploads:** Ensure the model can handle or reject corrupted files.
- **Inappropriate MRI Uploads:** Validate the uploaded MRI for relevance before analysis.
- **Poor Image Quality:** Establish quality control measures to enhance or reject inadequate images.

### IX. Deployment Infrastructure

#### Project Development on Google Cloud Platform (GCP):
- **Scalability:** GCP provides dynamic scaling options for efficient MRI data processing and analysis.
- **Reliability:** Robust infrastructure and uptime guarantees ensure operational accessibility.
- **Ease of Use:** Intuitive interface and comprehensive documentation simplify cloud resource management.
- **Tool Support:** Integration with a wide range of tools and services for data storage, machine learning, and analytics.

#### Frontend Development:
- **Streamlit:** Compatible with Linux, macOS, and Windows, allowing quick creation of interactive dashboards for visualizing MRI data analysis and model outputs.

#### Backend Infrastructure:
- Hosted on GCP to ensure scalability, security, and integration with powerful computing resources.

#### Key GCP Tools Utilized:
- **Buckets:** For scalable and secure storage of MRI images and other data.
- **Vertex AI:** Managed machine learning service aiding in training, tuning, and deploying the model on GCP.
- **Data Studio:** For creating interactive dashboards to visualize model performance metrics and operational analytics.

### X. Monitoring Plan

#### Statistics and Metadata of the Image Received for Prediction:
- **Purpose:** Ensure the quality and appropriateness of each MRI image uploaded for analysis.
- **Benefits:** Detect anomalies or deviations from expected standards, ensuring accurate model performance.

#### Metrics Representing Health of the Model:
- **Purpose:** Continuously assess model performance and operational status.
- **Benefits:** Regular evaluation ensures the model maintains its efficacy over time.

#### Monitoring for Dataset Shift and Dataset Skew:
- **Dataset Shift:** Occurs when statistical properties of incoming data differ from the training data.
- **Dataset Skew:** When the model receives data not representative of the population data it was trained on.
- **Purpose:** Detect and correct shifts or skews in the data.
- **Benefits:** Proactive monitoring allows for timely adjustments, maintaining model accuracy and generalization capabilities.

### XI. Success and Acceptance Criteria

#### Good Feedback from Doctors About the Performance of the Model:
- **Definition:** Collect qualitative feedback from medical professionals focusing on accuracy, reliability, and usability.
- **Measurement:** Implement surveys or interviews to gather detailed feedback.
- **Success Threshold:** A high level of satisfaction

 (e.g., above 80% positive feedback).

#### End User Trust:
- **Definition:** Users' confidence in the model's predictions and willingness to rely on it for clinical decisions.
- **Measurement:** Assess trust through direct feedback and indirect indicators such as the rate of follow-through on the model's recommendations.
- **Success Threshold:** Establish benchmarks for levels of trust and acceptance, such as less than 20% override rates.

### XII. Timeline Planning
*To be detailed based on project milestones and phases.*

### XIII. Additional Information
The methodologies for data preprocessing, modeling, deployment, and monitoring described above could change throughout the development process. Any changes will be documented, and the corresponding documentation will be updated to reflect these modifications.
