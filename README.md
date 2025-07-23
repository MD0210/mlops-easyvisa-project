# mlops-easyvisa-project

- Anaconda
- Vs Code
- Git
- Evidently AI
- MongoDB
- Data link: https://www.kaggle.com/datasets/moro23/easyvisa-dataset

# Git Command
- git Clone URL 
- git add .
- git commit -m "comment here"
- git push origin main

# Create Environment using Conda
- conda create -n {environment name} python={version} -y
- conda init
- conda activate {environment name}
- pip install -r requirements.txt #this is inside the environment

# Export the environment variable using git bash
- export MONGODB_URL="mongodb+srv://<username>:<password>...."

# Workflow
1. constants
2. entity
3. components
4. pipeline
5. Main file