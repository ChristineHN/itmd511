# Course: ITMD-511
# Name: Hoa Le & Hyesoo Noh

# File: career_db.py

# The 40-role career database is based on a comprehensive analysis of global labor market trends,
# primarily sourced from the World Economic Forum's "Future of Jobs Report 2025" and supplemented
# by data from other reputable industry reports such as Visual Capitalist – Fastest Growing Jobs
# (2025–2030) and U.S. Bureau of Labor Statistics (BLS).

# *** Gemini-generated code with human assistance (prompting and careers editing) ***

# --- Expanded Global Fastest-Growing Career Database ---
CAREERS = [
    {
        "title": "AI Engineer",
        "description": "Develops AI solutions with deep learning, automation, and AI infrastructure.",
        "skills": ["Python", "Machine Learning", "Deep Learning", "MLOps"],
        "progression": ["AI Engineer", "Senior AI Eng.", "AI Architect"]
    },
    {
        "title": "Machine Learning Engineer",
        "description": "Implements and deploys machine learning models at scale.",
        "skills": ["Python", "Model Deployment", "PyTorch", "TensorFlow"],
        "progression": ["ML Engineer", "Senior ML Engineer", "ML Architect"]
    },
    {
        "title": "Data Scientist",
        "description": "Abilities in Python, data analysis, machine learning, and visualization.",
        "skills": ["Python", "Data Analysis", "Machine Learning", "Data Visualization"],
        "progression": ["Data Scientist", "Senior DS", "Lead Data Scientist"]
    },
    {
        "title": "Data Engineer",
        "description": "Builds pipelines and manages large datasets for analytics.",
        "skills": ["ETL", "SQL", "Python", "Big Data"],
        "progression": ["Data Engineer", "Senior DE", "DE Lead"]
    },
    {
        "title": "Cloud Architect",
        "description": "Designs and maintains cloud infrastructure and services.",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes"],
        "progression": ["Cloud Architect", "Senior CA", "Head CA"]
    },
    {
        "title": "Cybersecurity Analyst",
        "description": "Protects systems, networks, and data from cyber threats.",
        "skills": ["Network Security", "Risk Assessment", "Firewalls", "SIEM"],
        "progression": ["Cybersecurity Analyst", "Lead CA", "Security Architect"]
    },
    {
        "title": "Ethical Hacker",
        "description": "Tests and secures systems by simulating cyberattacks.",
        "skills": ["Penetration Testing", "Scripting", "Vulnerability Assessment", "Networking"],
        "progression": ["Ethical Hacker", "Senior EH", "Security Consultant"]
    },
    {
        "title": "Robotics Engineer",
        "description": "Designs and builds robotics systems for automation.",
        "skills": ["Mechanical Design", "Python", "Automation", "Control Systems"],
        "progression": ["Robotics Engineer", "Senior RE", "Robotics Lead"]
    },
    {
        "title": "Automation Engineer",
        "description": "Builds automated systems to improve operational efficiency.",
        "skills": ["Python", "PLC Programming", "Testing", "Robotics"],
        "progression": ["Automation Engineer", "Senior AE", "Automation Lead"]
    },
    {
        "title": "Blockchain Developer",
        "description": "Builds decentralized applications and smart contracts.",
        "skills": ["Smart Contracts", "Solidity", "APIs", "Cryptography"],
        "progression": ["Blockchain Developer", "Senior BD", "Blockchain Architect"]
    },
    {
        "title": "Full Stack Developer",
        "description": "Works on both frontend and backend web applications.",
        "skills": ["JavaScript", "Python", "APIs", "Databases"],
        "progression": ["Full Stack Developer", "Senior FSD", "Lead FSD"]
    },
    {
        "title": "Software Engineer",
        "description": "Experienced in design, develop, test and maintain software applications.",
        "skills": ["Python", "Database", "Data Structure", "Testing"],
        "progression": ["Software Engineer", "Senior SE", "Tech Lead"]
    },
    {
        "title": "DevOps Engineer",
        "description": "Automates deployments and manages CI/CD pipelines.",
        "skills": ["CI/CD", "Docker", "Kubernetes", "Scripting"],
        "progression": ["DevOps Engineer", "Senior DE", "DevOps Lead"]
    },
    {
        "title": "AR/VR Developer",
        "description": "Develops immersive augmented and virtual reality experiences.",
        "skills": ["Unity", "3D Modeling", "C#", "Interaction Design"],
        "progression": ["AR/VR Developer", "Senior AR/VR", "XR Lead"]
    },
    {
        "title": "UX/UI Designer",
        "description": "Designs intuitive user interfaces and improves user experience.",
        "skills": ["Wireframing", "Prototyping", "Figma", "User Research"],
        "progression": ["UX/UI Designer", "Senior UX/UI", "Design Lead"]
    },
    {
        "title": "Product Manager",
        "description": "Oversees product lifecycle, strategy, and stakeholder alignment.",
        "skills": ["Roadmapping", "Market Research", "Agile", "Communication"],
        "progression": ["Product Manager", "Senior PM", "Product Director"]
    },
    {
        "title": "AI Product Manager",
        "description": "Guides strategy and development of AI-based products.",
        "skills": ["Product Strategy", "AI Concepts", "Roadmapping", "Stakeholder Management"],
        "progression": ["AI Product Manager", "Senior AI PM", "AI Director"]
    },
    {
        "title": "Digital Transformation Consultant",
        "description": "Helps organizations modernize processes and technology.",
        "skills": ["Strategy", "Change Management", "Process Automation", "Communication"],
        "progression": ["Consultant", "Senior Consultant", "Digital Transf Director"]
    },
    {
        "title": "Data Privacy Officer",
        "description": "Ensures compliance with global data privacy regulations.",
        "skills": ["GDPR", "Data Governance", "Risk Management", "Compliance"],
        "progression": ["Data Privacy Officer", "Senior Officer", "Chief Officer"]
    },
    {
        "title": "Renewable Energy Engineer",
        "description": "Designs and manages renewable energy systems like solar and wind.",
        "skills": ["Solar Energy", "Wind Energy", "Electrical Engineering", "Project Management"],
        "progression": ["Renewable Energy Eng", "Senior RE", "RE Manager"]
    },
    {
        "title": "Renewable Energy Analyst",
        "description": "Analyzes energy data to improve sustainability strategies.",
        "skills": ["Data Analysis", "Energy Modeling", "Reporting", "Policy Knowledge"],
        "progression": ["RE Analyst", "Senior REA", "Sust. Program Lead"]
    },
    {
        "title": "Healthcare Data Analyst",
        "description": "Analyzes clinical and operational data in healthcare settings.",
        "skills": ["SQL", "Data Analysis", "Healthcare Analytics", "Python"],
        "progression": ["Healthcare Data Analyst", "Senior HDA", "HDA Lead"]
    },
    {
        "title": "Healthcare Administrator",
        "description": "Manages operations and compliance in healthcare settings.",
        "skills": ["Healthcare Regulations", "Scheduling", "Communication", "Budgeting"],
        "progression": ["Healthcare Administrator", "Senior HA", "HA Director"]
    },
    {
        "title": "Clinical Data Manager",
        "description": "Oversees clinical data collection and quality for trials.",
        "skills": ["Data Management", "Regulatory Compliance", "Documentation", "SQL"],
        "progression": ["Clinical Data Manager", "Senior CDM", "CDM Director"]
    },
    {
        "title": "Biotech Researcher",
        "description": "Conducts research in biology, genetics, and pharmaceuticals.",
        "skills": ["Lab Techniques", "Data Analysis", "Research Design", "Documentation"],
        "progression": ["Biotech Researcher", "Senior BR", "Principal Scientist"]
    },
    {
        "title": "Environmental Scientist",
        "description": "Assesses environmental impact and sustainability strategies.",
        "skills": ["Field Research", "Data Analysis", "Regulations", "Reporting"],
        "progression": ["Environmental Scientist", "Senior ES", "ES Director"]
    },
    {
        "title": "Sustainability Consultant",
        "description": "Advises organizations on reducing carbon footprint and ESG compliance.",
        "skills": ["ESG Strategy", "Carbon Accounting", "Policy Knowledge", "Project Management"],
        "progression": ["Sustainability Consultant", "Senior SC", "SC Director"]
    },
    {
        "title": "Digital Marketing Specialist",
        "description": "Manages online campaigns and analyzes marketing performance.",
        "skills": ["SEO", "Content Strategy", "Analytics", "Social Media"],
        "progression": ["Digital Specialist", "Marketing Strategist", "Marketing Director"]
    },
    {
        "title": "E-commerce Manager",
        "description": "Manages online sales platforms and digital retail strategies.",
        "skills": ["Analytics", "SEO", "Customer Experience", "Product Management"],
        "progression": ["E-commerce Manager", "Senior ECM", "Head of ECM"]
    },
    {
        "title": "Digital Content Creator",
        "description": "Produces multimedia content for platforms and marketing.",
        "skills": ["Writing", "Video Editing", "Social Media", "Branding"],
        "progression": ["Content Creator", "Senior DSC", "DSC Lead"]
    },
    {
        "title": "Instructional Designer",
        "description": "Creates learning experiences and digital training content.",
        "skills": ["Curriculum Design", "eLearning Tools", "Assessment", "Storyboarding"],
        "progression": ["Instructional Designer", "Senior ID", "ID Lead"]
    },
    {
        "title": "Business Analyst",
        "description": "Analyzes business needs and improves processes using data.",
        "skills": ["Data Analysis", "Requirements Gathering", "Stakeholder Communication", "SQL"],
        "progression": ["Business Analyst", "Senior BA", "BA Lead"]
    },
    {
        "title": "Project Manager",
        "description": "Agile, Scrum, leads projects, coordinates teams, manages timelines and budgets.",
        "skills": ["Agile", "Project Planning", "Budgeting", "Risk Management"],
        "progression": ["Project Manager", "Program Manager", "Portfolio Manager"]
    },
    {
        "title": "Operations Manager",
        "description": "Optimizes workflows and manages cross-functional operations.",
        "skills": ["Process Improvement", "Leadership", "Budgeting", "Analytics"],
        "progression": ["Operations Manager", "Senior OM", "Ops Director"]
    },
    {
        "title": "Supply Chain Analyst",
        "description": "Improves supply chain efficiency and logistics.",
        "skills": ["Data Analysis", "Forecasting", "Logistics", "Negotiation"],
        "progression": ["Supply Chain Analyst", "Senior SCA", "SCA Manager"]
    },
    {
        "title": "IT Support Specialist",
        "description": "Provides technical support and solves IT issues for users.",
        "skills": ["Troubleshooting", "Customer Service", "Networking", "Hardware"],
        "progression": ["IT Support Specialist", "IT Lead", "IT Manager"]
    },
    {
        "title": "Web Developer",
        "description": "Builds and maintains websites and web applications.",
        "skills": ["HTML", "CSS", "JavaScript", "APIs"],
        "progression": ["Web Developer", "Senior WD", "WD Lead"]
    },
    {
        "title": "Systems Analyst",
        "description": "Evaluates and improves IT systems and workflows.",
        "skills": ["Systems Design", "Troubleshooting", "SQL", "Documentation"],
        "progression": ["Systems Analyst", "Senior SA", "Systems Architect"]
    },
    {
        "title": "Database Administrator",
        "description": "Manages and optimizes database performance and security.",
        "skills": ["SQL", "Backup Management", "Performance Tuning", "Security"],
        "progression": ["Database Admin", "Senior DBA", "DB Architect"]
    },
    {
        "title": "Financial Analyst",
        "description": "Analyzes financial data to guide business decisions.",
        "skills": ["Excel", "Forecasting", "Modeling", "Reporting"],
        "progression": ["Financial Analyst", "Senior Analyst", "Finance Manager"]
    },
    {
        "title": "Human Resources Specialist",
        "description": "Handles recruiting, training, and employee relations.",
        "skills": ["Recruitment", "Onboarding", "Compliance", "Communication"],
        "progression": ["HR Specialist", "HR Manager", "HR Director"]
    }
]
