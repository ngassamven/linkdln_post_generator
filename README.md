# 🚀 LinkedIn Post Generator & Tag Processor

Un projet Python permettant de **générer automatiquement des posts LinkedIn** à partir d’un modèle de langage (LLM) et de **traiter/structurer des posts existants** afin d’en extraire des métadonnées comme la langue, le nombre de lignes ou les tags.  
Le système s’appuie sur **LangChain**, **Groq (LLM Mistral)** et **Streamlit** pour proposer une approche modulaire et évolutive.

---

## 🧠 Fonctionnalités principales

### 🔹 Génération de posts LinkedIn
- Génère un post selon :
  - Une **longueur** : `Short`, `Medium` ou `Long`
  - Une **langue** : `English` ou `Hinglish`
  - Un **thème (tag)** : ex. `Mental Health`, `Job Search`, etc.
- Le texte est généré par le modèle **Groq Mistral (mistral-saba-24b)**.
- Si des exemples de posts similaires existent, le modèle s’en inspire (few-shot learning).

### 🔹 Traitement et enrichissement de posts existants
- Lecture d’un fichier `raw_posts.json` contenant des posts bruts.
- Extraction automatique des métadonnées :
  - Nombre de lignes
  - Langue (`English` / `Hinglish`)
  - Tags pertinents (max 2 par post)
- Unification intelligente des tags proches (ex. `Jobseekers`, `Job Hunting` → `Job Search`).

### 🔹 Base de données de posts de référence
- Les posts enrichis sont sauvegardés dans `processed_posts.json`.
- Ces données servent de base pour le **few-shot prompting**.

---

## 📁 Structure du projet

📦 ton-projet/
│
├── data/
│   ├── raw_posts.json           # Données brutes (posts initiaux)
│   ├── processed_posts.json     # Données enrichies et nettoyées
│
├── few_shot.py                  # Gestion des exemples de posts (FewShotPosts)
├── llm_helper.py                # Connexion et configuration du modèle Groq
├── main.py                      # Génération de posts LinkedIn
├── process_posts.py             # Extraction et unification des métadonnées
├── requirements.txt             # Dépendances du projet
└── .env                         # Clé API Groq


## ⚙️ Installation et configuration
### 1️⃣ Cloner le projet
git clone https://github.com/ton-utilisateur/ton-projet.git
cd ton-projet

### 2️⃣ Créer un environnement virtuel
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

### 3️⃣ Installer les dépendances
pip install -r requirements.txt

### 4️⃣ Ajouter la clé API Groq

Crée un fichier .env à la racine du projet :

GROQ_API_KEY=ta_cle_api_groq

### ▶️ Utilisation
🔹 Générer un post LinkedIn
python main.py


Ce script générera un post selon les paramètres définis :

print(generate_post("Medium", "English", "Mental Health"))

🔹Traiter des posts existants
python process_posts.py


Cela analysera le fichier data/raw_posts.json et créera data/processed_posts.json enrichi.

## 🧩 Technologies utilisées

- Python 3.10+

- LangChain

- LangChain Groq

- Groq Mistral 24B

- Pandas

- Streamlit

## 🧑‍💻 Auteur

Venceslas NGASSAM
📧 www.linkedin.com/in/venceslas-osee-ngassam-kate-data-engineer

💼 Data Engineer | Data Scientist | Cloud & Big Data | Databricks Associate Data Engineer | Azure DP-700 | Snowflake SnowPro Core | AI & Machine Learning

## 🪪 Licence

Ce projet est distribué sous licence MIT.
Tu es libre de l’utiliser, le modifier et le partager avec mention de l’auteur.
