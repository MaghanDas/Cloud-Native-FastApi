# Cloud‑Native FastAPI + React Application (DevOps Project)

This repository demonstrates a **production‑ready, cloud‑native web application** built with **FastAPI (backend)**, **React (frontend)**, **PostgreSQL**, **Docker**, **Terraform**, **AWS**, and **CI/CD using GitHub Actions**.

The project is designed to showcase **end‑to‑end DevOps practices** — from local development to automated cloud deployment.

---

## 🚀 What This Project Does

* CRUD Product Management application
* REST API built with FastAPI
* React UI consuming the API
* PostgreSQL database
* Fully containerized using Docker
* Infrastructure provisioned using Terraform (AWS EC2 + RDS)
* Automated deployment using GitHub Actions

---

## 🧱 Architecture Overview

```
User Browser
     ↓
React Frontend (Docker)
     ↓ HTTP
FastAPI Backend (Docker)
     ↓ SQL
PostgreSQL (RDS or Container)
```

---

## 🛠 Tech Stack

| Layer      | Technology             |
| ---------- | ---------------------- |
| Frontend   | React, Axios           |
| Backend    | FastAPI, SQLAlchemy    |
| Database   | PostgreSQL             |
| Containers | Docker, Docker Compose |
| Cloud      | AWS EC2, AWS RDS       |
| IaC        | Terraform              |
| CI/CD      | GitHub Actions         |

---

## 📂 Repository Structure

```
.
├── backend/              # FastAPI backend
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/             # React frontend
│   ├── src/
│   ├── Dockerfile
│   └── nginx.conf
│
├── terraform/            # AWS infrastructure
│   ├── main.tf
│   ├── ec2.tf
│   ├── rds.tf
│   └── variables.tf
│
├── docker-compose.yml
└── README.md
```

---

## ▶️ Running the Project Locally (Docker Compose)

### Prerequisites

* Docker
* Docker Compose

### Steps

```bash
git clone https://github.com/MaghanDas/Cloud-Native-FastApi.git
cd Cloud-Native-FastApi
```

Create backend environment file:

```bash
backend/.env
```

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
```

Run the application:

```bash
docker compose up --build
```

Access:

* Frontend: [http://localhost](http://localhost)
* Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ☁️ Cloud Deployment (AWS + Terraform)

### Infrastructure Provisioned

Terraform automatically creates:

* EC2 instance (application host)
* Security Groups
* RDS PostgreSQL database
* Key pair for SSH

### Steps

```bash
cd terraform
terraform init
terraform apply
```

Terraform outputs:

* EC2 public IP
* RDS endpoint

---

## 🔐 Application Configuration on EC2

### SSH into EC2

```bash
ssh -i ~/.ssh/ci-cd-ec2-key.pem ec2-user@<EC2_PUBLIC_IP>
```

### Clone Repository

```bash
git clone https://github.com/MaghanDas/Cloud-Native-FastApi.git
cd Cloud-Native-FastApi
```

### Backend Environment

```bash
backend/.env
```

```env
DATABASE_URL=postgresql://postgres:<PASSWORD>@<RDS_ENDPOINT>:5432/postgres
```

### Frontend Environment Variable

```bash
export REACT_APP_API_URL=http://<EC2_PUBLIC_IP>:8000
```

### Run Containers

```bash
docker compose build
docker compose up -d
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

### What Happens on Each `git push`

1. Backend & frontend Docker images are built
2. Images are pushed to Docker Hub
3. GitHub Actions connects to EC2 via SSH
4. EC2 pulls latest images
5. Containers are restarted automatically

### Required GitHub Secrets

| Secret Name       | Description         |
| ----------------- | ------------------- |
| EC2_HOST          | EC2 public IP       |
| EC2_KEY           | Private SSH key     |
| DOCKER_USERNAME   | Docker Hub username |
| DOCKER_PASSWORD   | Docker Hub password |
| REACT_APP_API_URL | Backend API URL     |

---

## 📦 docker-compose.yml (Production‑Ready)

```yaml
version: "3.9"

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env

  frontend:
    build:
      context: ./frontend
      args:
        REACT_APP_API_URL: ${REACT_APP_API_URL}
    ports:
      - "80:80"
    depends_on:
      - backend
```

---

## 🧠 DevOps Concepts Demonstrated

* Infrastructure as Code (Terraform)
* Environment‑based configuration
* Secure secret management
* Containerized microservices
* Automated CI/CD deployment
* Cloud‑native design principles

---

## 📈 Future Improvements

* Kubernetes (EKS) deployment
* AWS Application Load Balancer
* HTTPS with ACM
* Auto Scaling Group
* Blue‑Green deployments

---

## 👨‍🎓 Academic Note

This project was built as a **hands‑on DevOps learning project**, demonstrating real‑world cloud deployment challenges and solutions.

---

## 📜 License

MIT License

---

**Author:** Maghan Das
