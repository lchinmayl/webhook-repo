# GitHub Webhook Receiver & UI – Flask + MongoDB

This project is part of a developer assessment task to receive GitHub webhook events (Push, Pull Request, Merge) and display them live in a minimal frontend UI


## 🧠 Problem Statement

Capture and display GitHub activity using a webhook:
- Triggered from actions in a separate repository: `action-repo`
- Push, PR, and Merge actions are logged
- Stored in **MongoDB**
- Displayed via a frontend UI with **auto-refresh every 15 seconds**


## 🛠️ Tech Stack

- **Backend**: Flask
- **Database**: MongoDB Atlas
- **Frontend**: HTML + JS (Fetch API)
- **Tunneling (for testing)**: ngrok


## 📦 Folder Structure

webhook-repo/
├── app.py 
├── .env 
├── requirements.txt 
├── templates/
│ └── index.html
├── static/
│ └── script.js



## 🚀 Setup Instructions (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/lchinmayl/webhook-repo.git
cd webhook-repo

Create .env File:-
MONGO_URI=mongodb+srv://<username>:<encoded-password>@cluster.mongodb.net/webhooks?retryWrites=true&w=majority

