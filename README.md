```markdown
# 🚗 Vehicle Data ML Project

A complete end-to-end Machine Learning project with MongoDB integration, AWS deployment, CI/CD pipeline using GitHub Actions, Docker, and EC2. This project follows MLOps principles to ensure smooth automation, scalability, and reproducibility.

---

## 📁 Project Structure & Workflow

### 🔧 Step 1: Initial Project Setup
1. Run `template.py` to generate the basic folder structure.
2. Configure local package imports using `setup.py` and `pyproject.toml`.  
   📖 *Refer to `crashcourse.txt` for more info on these files.*

### 🐍 Step 2: Virtual Environment & Dependencies
```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list  # Verify local packages
```

---

## 🍃 MongoDB Atlas Setup
1. Sign up and create a new project on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a **free M0 cluster**, a DB user, and set IP access to `0.0.0.0/0`.
3. Copy the Python connection string.
4. Create a folder `notebook` and file `mongoDB_demo.ipynb`.
5. Load dataset and push to MongoDB via notebook.
6. Verify data in MongoDB Atlas > Database > Browse Collections.

---

## 🪵 Logging & ❗ Exception Handling
- Create `logger.py` and `exception.py` modules.
- Test both using `demo.py`.

---

## 📊 EDA & Feature Engineering
- Perform EDA in a Jupyter Notebook within the `notebook` folder.
- Feature Engineering steps are documented and saved.

---

## 📥 Data Ingestion Pipeline
- Setup config and connection files:
  - `constants/__init__.py`
  - `configuration/mongo_db_connections.py`
  - `data_access/proj1_data.py`
  - `entity/config_entity.py`
  - `entity/artifact_entity.py`
  - `components/data_ingestion.py`
- Run `demo.py` to test data ingestion.

> 💡 Set MongoDB URL in environment:
```bash
# Bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net"
```

---

## ✅ Data Validation & 🔄 Transformation
- Implement validation logic in `utils/main_utils.py` using `config/schema.yaml`.
- Build components: `data_validation.py`, `data_transformation.py`, `estimator.py`.

---

## 🤖 Model Training
- Build model trainer module and classes in `estimator.py`.

---

## ☁️ AWS Integration & S3 Setup
1. Create IAM user on AWS with **AdministratorAccess**.
2. Set up access credentials:
```bash
# Bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```
3. Add the following to `constants/__init__.py`:
```python
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"
```
4. Create S3 bucket: `my-model-mlopsproj`
5. Add `aws_connection.py`, `aws_storage/`, and `s3_estimator.py`.

---

## 📈 Model Evaluation & Deployment
- Add logic for model evaluation and pusher components.
- Build `Prediction Pipeline` in `app.py`.
- Add `static/` and `template/` folders.

---

## ⚙️ CI/CD with GitHub Actions & Docker

### 📦 Docker & GitHub Actions
- Create `Dockerfile` and `.dockerignore`.
- Add GitHub Actions workflow: `.github/workflows/aws.yaml`

### 🐳 AWS ECR + EC2 Setup
1. Create IAM user for CI/CD (e.g., `vehicle-user`)
2. Create ECR repo: `vehicleproj`
3. Launch EC2 Ubuntu instance and install Docker:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
4. Set up GitHub Self-Hosted Runner on EC2.
5. Add GitHub secrets:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_DEFAULT_REGION`
   - `ECR_REPO`

---

## 🌍 Deployment
- Expose EC2 instance port:
  - Edit security group > Inbound rules > Add rule:
    - Type: Custom TCP
    - Port: **5000**
    - Source: `0.0.0.0/0`
- Access your app:  
  `http://<your-ec2-public-ip>:5000`

> 🚀 Model training available at route: `/training`

---

## 📚 Tech Stack

- **Backend:** Python, FastAPI / Flask
- **Database:** MongoDB Atlas
- **ML:** scikit-learn, pandas, numpy
- **CI/CD:** GitHub Actions, Docker, AWS ECR, EC2
- **Deployment:** EC2, Docker, S3

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

Big thanks to all open-source contributors and the ML community that inspires projects like this one.
