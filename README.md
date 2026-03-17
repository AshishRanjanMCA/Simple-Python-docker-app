# 🐍 Python Docker App – Random Quote Generator

## 📌 Project Overview

This is a simple Python application that generates random quotes and runs inside a Docker container.
The purpose of this project is to practice Docker basics like building images, running containers, and pushing images to Docker Hub.

---

## 🚀 Features

* Generates random quotes
* Lightweight and simple Python application
* Fully containerized using Docker
* No external dependencies required

---

## 🛠️ Technologies Used

* Python 3
* Docker

---

## 📂 Project Structure

```
python-docker-app/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## ▶️ How to Run Locally

### 1. Clone the Repository

```
git clone https://github.com/your-username/python-docker-app.git
cd python-docker-app
```

### 2. Build Docker Image

```
docker build -t python-app .
```

### 3. Run Docker Container

```
docker run python-app
```

---

## 🧪 Sample Output

```
🚀 Python Docker App Started...

Quote 1: Code is like humor. When you have to explain it, it’s bad.
Quote 2: Simplicity is the soul of efficiency.
Quote 3: First, solve the problem. Then, write the code.

✅ App Finished
```

---

## 📦 Push Image to Docker Hub

### Tag the image

```
docker tag python-app your-dockerhub-username/python-app:latest
```

### Push the image

```
docker push your-dockerhub-username/python-app:latest
```

---

## 💡 Learning Outcomes

* Understanding Dockerfile basics
* Building Docker images
* Running containers
* Tagging and pushing images to Docker Hub

---

## 👨‍💻 Author

Ashish Ranjan

---

## ⭐ Note

This project is created for learning Docker and DevOps fundamentals.
