# Chatgpt generated list of 200 data skills and estimated skill level from 1-10

skills_dict = {
    # Core programming & data
    "Python": 8,
    "Pandas": 7,
    "NumPy": 7,
    "Data Analysis": 9,
    "Data Cleaning": 7,
    "Data Wrangling": 6,
    "Data Structures": 6,
    "Algorithms": 5,
    "Object-Oriented Programming": 4,
    "Functional Programming": 3,
    "Code Debugging": 5,
    "Code Refactoring": 4,
    "Performance Optimization": 4,
    "Version Control (Git)": 5,
    "GitHub": 6,
    "Virtual Environments": 6,

    # Visualisation
    "Data Visualization": 9,
    "Matplotlib": 8,
    "Seaborn": 7,
    "Plotly": 4,
    "Dashboards": 5,
    "Storytelling with Data": 8,
    "Chart Design": 7,

    # Statistics & maths
    "Statistics": 6,
    "Descriptive Statistics": 10,
    "Inferential Statistics": 9,
    "Probability": 5,
    "Hypothesis Testing": 6,
    "Regression Analysis": 6,
    "Linear Algebra": 4,
    "Optimization": 3,
    "Time Series Analysis": 4,
    "Uncertainty Analysis": 5,

    # Machine learning
    "Machine Learning": 5,
    "Supervised Learning": 5,
    "Unsupervised Learning": 4,
    "Feature Engineering": 5,
    "Model Evaluation": 5,
    "Cross Validation": 5,
    "Overfitting Control": 4,
    "Scikit-learn": 5,
    "Decision Trees": 4,
    "Random Forests": 4,
    "Gradient Boosting": 3,
    "Clustering": 4,
    "Dimensionality Reduction": 3,
    "Neural Networks": 2,
    "Deep Learning": 2,

    # Data handling & formats
    "SQL": 5,
    "Relational Databases": 5,
    "Data Modeling": 5,
    "CSV Handling": 7,
    "JSON Handling": 6,
    "API Consumption": 6,
    "Web Scraping": 4,
    "ETL Pipelines": 4,

    # Tools & environments
    "Jupyter Notebooks": 8,
    "Spyder": 6,
    "PyCharm": 5,
    "VS Code": 4,
    "Command Line": 5,
    "Conda": 6,
    "Package Management": 6,
    "Linux Basics": 4,

    # Software & deployment
    "Software Engineering Principles": 4,
    "Testing": 3,
    "Unit Testing": 3,
    "Documentation": 6,
    "Reproducible Research": 6,
    "Automation": 4,
    "CI/CD Awareness": 2,

    # Cloud & big data (awareness stage)
    "Cloud Computing": 2,
    "AWS Basics": 2,
    "Azure Basics": 2,
    "Google Cloud Basics": 1,
    "Big Data Concepts": 2,
    "Spark": 1,
    "Distributed Computing": 1,

    # Research & experimentation
    "Experimental Design": 6,
    "Causal Analysis": 6,
    "A/B Testing": 5,
    "Exploratory Data Analysis": 8,
    "Model Interpretation": 5,
    "Bias Awareness": 6,
    "Ethical Data Use": 6,

    # Domain & applied knowledge
    "Life Cycle Assessment": 6,
    "Sustainability Analysis": 6,
    "Environmental Data": 6,
    "Engineering Fundamentals": 5,
    "Systems Thinking": 6,
    "Supply Chain Analysis": 5,
    "Process Optimization": 5,
    "Lean Six Sigma": 4,
    "Manufacturing Processes": 4,
    "Energy Systems": 4,

    # Communication & employability
    "Stakeholder Communication": 6,
    "Technical Writing": 6,
    "Reporting": 6,
    "Insight Generation": 7,
    "Presentation Skills": 6,
    "Data Translation": 7,
    "Business Acumen": 5,
    "Decision Support": 6,

    # Professional skills
    "Problem Solving": 7,
    "Critical Thinking": 7,
    "Learning Agility": 7,
    "Self-Directed Learning": 8,
    "Adaptability": 7,
    "Time Management": 6,
    "Project Planning": 6,
    "Prioritization": 6,
    "Attention to Detail": 7,

    # Collaboration & leadership
    "Team Collaboration": 6,
    "Interdisciplinary Work": 7,
    "Leadership": 5,
    "Mentoring": 4,
    "Knowledge Sharing": 6,
    "Conflict Resolution": 4,
    "Feedback Reception": 6,

    # Career & growth
    "Portfolio Development": 6,
    "Git-Based Portfolio": 6,
    "API Integration": 6,
    "Product Thinking": 4,
    "User-Centered Design": 4,
    "Career Planning": 6,
    "Continuous Improvement": 7,

    # Meta-skills
    "Creativity": 6,
    "Curiosity": 8,
    "Resilience": 6,
    "Systems Learning": 7,
    "Abstraction": 6,
    "Pattern Recognition": 6,
    "Communication Clarity": 6,
    "Professional Judgment": 5
}

skills_text = " ".join(
    skill
    for skill, count in skills_dict.items()
    for _ in range(count)
)