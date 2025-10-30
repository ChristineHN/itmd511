# Course: ITMD-511
# Name: Hoa Le & Hyesoo Noh

# File: career_db.py

# The 60-role career database is based on a comprehensive analysis of global labor market trends,
# primarily sourced from the World Economic Forum's "Future of Jobs Report 2025" and supplemented
# by data from other reputable industry reports such as Visual Capitalist – Fastest Growing Jobs
# (2025–2030) and U.S. Bureau of Labor Statistics (BLS).

# *** Gemini-generated code with human assistance (prompting and careers editing) ***

# --- Expanded Global Fastest-Growing Career Database ---
CAREERS = [
    {
        "title": "AI Engineer",
        "description": "Develops AI solutions with machine learning, deep learning, automation, MLOps, and AI infrastructure. Key skills include Python, Machine Learning, Deep Learning, and MLOps.",
        "skills": ["Python", "Machine Learning", "Deep Learning", "MLOps"],
        "progression": ["AI Engineer", "Senior AI Eng.", "AI Architect"]
    },
    {
        "title": "Machine Learning Engineer",
        "description": "Implements and deploys machine learning models at scale. Key skills include Python, Model Deployment, PyTorch, and TensorFlow.",
        "skills": ["Python", "Model Deployment", "PyTorch", "TensorFlow"],
        "progression": ["ML Engineer", "Senior ML Engineer", "ML Architect"]
    },
    {
        "title": "Data Scientist",
        "description": "Abilities in Python, data analysis, machine learning, and visualization. Key skills include Python, Data Analysis, Machine Learning, and Data Visualization.",
        "skills": ["Python", "Data Analysis", "Machine Learning", "Data Visualization"],
        "progression": ["Data Scientist", "Senior DS", "Lead Data Scientist"]
    },
    {
        "title": "Data Engineer",
        "description": "Builds pipelines and manages large datasets for analytics. Key skills include ETL, SQL, Python, and Big Data.",
        "skills": ["ETL", "SQL", "Python", "Big Data"],
        "progression": ["Data Engineer", "Senior DE", "DE Lead"]
    },
    {
        "title": "Cloud Architect",
        "description": "Designs and maintains cloud infrastructure and services. Key skills include AWS, Azure, Docker, and Kubernetes.",
        "skills": ["AWS", "Azure", "Docker", "Kubernetes"],
        "progression": ["Cloud Architect", "Senior CA", "Head CA"]
    },
    {
        "title": "Cybersecurity Analyst",
        "description": "Protects systems, networks, and data from cyber threats. Key skills include Network Security, Risk Assessment, Firewalls, and SIEM.",
        "skills": ["Network Security", "Risk Assessment", "Firewalls", "SIEM"],
        "progression": ["Cybersecurity Analyst", "Lead CA", "Security Architect"]
    },
    {
        "title": "Ethical Hacker",
        "description": "Tests and secures systems by simulating cyberattacks. Key skills include Penetration Testing, Scripting, Vulnerability Assessment, and Networking.",
        "skills": ["Penetration Testing", "Scripting", "Vulnerability Assessment", "Networking"],
        "progression": ["Ethical Hacker", "Senior EH", "Security Consultant"]
    },
    {
        "title": "Robotics Engineer",
        "description": "Designs and builds robotics systems for automation. Key skills include Mechanical Design, Python, Automation, and Control Systems.",
        "skills": ["Mechanical Design", "Python", "Automation", "Control Systems"],
        "progression": ["Robotics Engineer", "Senior RE", "Robotics Lead"]
    },
    {
        "title": "Automation Engineer",
        "description": "Builds automated systems to improve operational efficiency. Key skills include Python, PLC Programming, Testing, and Robotics.",
        "skills": ["Python", "PLC Programming", "Testing", "Robotics"],
        "progression": ["Automation Engineer", "Senior AE", "Automation Lead"]
    },
    {
        "title": "Blockchain Developer",
        "description": "Builds decentralized applications and smart contracts. Key skills include Smart Contracts, Solidity, APIs, and Cryptography.",
        "skills": ["Smart Contracts", "Solidity", "APIs", "Cryptography"],
        "progression": ["Blockchain Developer", "Senior BD", "Blockchain Architect"]
    },
    {
        "title": "Full Stack Developer",
        "description": "Works on both frontend and backend web applications. Key skills include JavaScript, Python, APIs, and Databases.",
        "skills": ["JavaScript", "Python", "APIs", "Databases"],
        "progression": ["Full Stack Developer", "Senior FSD", "Lead FSD"]
    },
    {
        "title": "Software Engineer",
        "description": "Experienced in design, develop, test and maintain software applications. Key skills include Python, Database, Data Structure, and Testing.",
        "skills": ["Python", "Database", "Data Structure", "Testing"],
        "progression": ["Software Engineer", "Senior SE", "Tech Lead"]
    },
    {
        "title": "DevOps Engineer",
        "description": "Automates deployments and manages CI/CD pipelines. Key skills include CI/CD, Docker, Kubernetes, and Scripting.",
        "skills": ["CI/CD", "Docker", "Kubernetes", "Scripting"],
        "progression": ["DevOps Engineer", "Senior DE", "DevOps Lead"]
    },
    {
        "title": "AR/VR Developer",
        "description": "Develops immersive augmented and virtual reality experiences. Key skills include Unity, 3D Modeling, C#, and Interaction Design.",
        "skills": ["Unity", "3D Modeling", "C#", "Interaction Design"],
        "progression": ["AR/VR Developer", "Senior AR/VR", "XR Lead"]
    },
    {
        "title": "UX/UI Designer",
        "description": "Designs intuitive user interfaces and improves user experience. Key skills include Wireframing, Prototyping, Figma, and User Research.",
        "skills": ["Wireframing", "Prototyping", "Figma", "User Research"],
        "progression": ["UX/UI Designer", "Senior UX/UI", "Design Lead"]
    },
    {
        "title": "Product Manager",
        "description": "Oversees product lifecycle, strategy, and stakeholder alignment. Key skills include Roadmapping, Market Research, Agile, and Communication.",
        "skills": ["Roadmapping", "Market Research", "Agile", "Communication"],
        "progression": ["Product Manager", "Senior PM", "Product Director"]
    },
    {
        "title": "AI Product Manager",
        "description": "Guides strategy and development of AI-based products. Key skills include Product Strategy, AI Concepts, Roadmapping, and Stakeholder Management.",
        "skills": ["Product Strategy", "AI Concepts", "Roadmapping", "Stakeholder Management"],
        "progression": ["AI Product Manager", "Senior AI PM", "AI Director"]
    },
    {
        "title": "Digital Transformation Consultant",
        "description": "Helps organizations modernize processes and technology. Key skills include Strategy, Change Management, Process Automation, and Communication.",
        "skills": ["Strategy", "Change Management", "Process Automation", "Communication"],
        "progression": ["Consultant", "Senior Consultant", "Digital Transf Director"]
    },
    {
        "title": "Data Privacy Officer",
        "description": "Ensures compliance with global data privacy regulations. Key skills include GDPR, Data Governance, Risk Management, and Compliance.",
        "skills": ["GDPR", "Data Governance", "Risk Management", "Compliance"],
        "progression": ["Data Privacy Officer", "Senior Officer", "Chief Officer"]
    },
    {
        "title": "Renewable Energy Engineer",
        "description": "Designs and manages renewable energy systems like solar and wind. Key skills include Solar Energy, Wind Energy, Electrical Engineering, and Project Management.",
        "skills": ["Solar Energy", "Wind Energy", "Electrical Engineering", "Project Management"],
        "progression": ["Renewable Energy Eng", "Senior RE", "RE Manager"]
    },
    {
        "title": "Renewable Energy Analyst",
        "description": "Analyzes energy data to improve sustainability strategies. Key skills include Data Analysis, Energy Modeling, Reporting, and Policy Knowledge.",
        "skills": ["Data Analysis", "Energy Modeling", "Reporting", "Policy Knowledge"],
        "progression": ["RE Analyst", "Senior REA", "Sust. Program Lead"]
    },
    {
        "title": "Healthcare Data Analyst",
        "description": "Analyzes clinical and operational data in healthcare settings. Key skills include SQL, Data Analysis, Healthcare Analytics, and Python.",
        "skills": ["SQL", "Data Analysis", "Healthcare Analytics", "Python"],
        "progression": ["Healthcare Data Analyst", "Senior HDA", "HDA Lead"]
    },
    {
        "title": "Healthcare Administrator",
        "description": "Manages operations and compliance in healthcare settings. Key skills include Healthcare Regulations, Scheduling, Communication, and Budgeting.",
        "skills": ["Healthcare Regulations", "Scheduling", "Communication", "Budgeting"],
        "progression": ["Healthcare Administrator", "Senior HA", "HA Director"]
    },
    {
        "title": "Clinical Data Manager",
        "description": "Oversees clinical data collection and quality for trials. Key skills include Data Management, Regulatory Compliance, Documentation, and SQL.",
        "skills": ["Data Management", "Regulatory Compliance", "Documentation", "SQL"],
        "progression": ["Clinical Data Manager", "Senior CDM", "CDM Director"]
    },
    {
        "title": "Biotech Researcher",
        "description": "Conducts research in biology, genetics, and pharmaceuticals. Key skills include Lab Techniques, Data Analysis, Research Design, and Documentation.",
        "skills": ["Lab Techniques", "Data Analysis", "Research Design", "Documentation"],
        "progression": ["Biotech Researcher", "Senior BR", "Principal Scientist"]
    },
    {
        "title": "Environmental Scientist",
        "description": "Assesses environmental impact and sustainability strategies. Key skills include Field Research, Data Analysis, Regulations, and Reporting.",
        "skills": ["Field Research", "Data Analysis", "Regulations", "Reporting"],
        "progression": ["Environmental Scientist", "Senior ES", "ES Director"]
    },
    {
        "title": "Sustainability Consultant",
        "description": "Advises organizations on reducing carbon footprint and ESG compliance. Key skills include ESG Strategy, Carbon Accounting, Policy Knowledge, and Project Management.",
        "skills": ["ESG Strategy", "Carbon Accounting", "Policy Knowledge", "Project Management"],
        "progression": ["Sustainability Consultant", "Senior SC", "SC Director"]
    },
    {
        "title": "Digital Marketing Specialist",
        "description": "Manages online campaigns and analyzes marketing performance. Key skills include SEO, Content Strategy, Analytics, and Social Media.",
        "skills": ["SEO", "Content Strategy", "Analytics", "Social Media"],
        "progression": ["Digital Specialist", "Marketing Strategist", "Marketing Director"]
    },
    {
        "title": "E-commerce Manager",
        "description": "Manages online sales platforms and digital retail strategies. Key skills include Analytics, SEO, Customer Experience, and Product Management.",
        "skills": ["Analytics", "SEO", "Customer Experience", "Product Management"],
        "progression": ["E-commerce Manager", "Senior ECM", "Head of ECM"]
    },
    {
        "title": "Digital Content Creator",
        "description": "Produces multimedia content for platforms and marketing. Key skills include Writing, Video Editing, Social Media, and Branding.",
        "skills": ["Writing", "Video Editing", "Social Media", "Branding"],
        "progression": ["Content Creator", "Senior DSC", "DSC Lead"]
    },
    {
        "title": "Instructional Designer",
        "description": "Creates learning experiences and digital training content. Key skills include Curriculum Design, eLearning Tools, Assessment, and Storyboarding.",
        "skills": ["Curriculum Design", "eLearning Tools", "Assessment", "Storyboarding"],
        "progression": ["Instructional Designer", "Senior ID", "ID Lead"]
    },
    {
        "title": "Business Analyst",
        "description": "Analyzes business needs and improves processes using data. Key skills include Data Analysis, Requirements Gathering, Stakeholder Communication, and SQL.",
        "skills": ["Data Analysis", "Requirements Gathering", "Stakeholder Communication", "SQL"],
        "progression": ["Business Analyst", "Senior BA", "BA Lead"]
    },
    {
        "title": "Project Manager",
        "description": "Agile, Scrum, leads projects, coordinates teams, manages timelines and budgets. Key skills include Agile, Project Planning, Budgeting, and Risk Management.",
        "skills": ["Agile", "Project Planning", "Budgeting", "Risk Management"],
        "progression": ["Project Manager", "Program Manager", "Portfolio Manager"]
    },
    {
        "title": "Operations Manager",
        "description": "Optimizes workflows and manages cross-functional operations. Key skills include Process Improvement, Leadership, Budgeting, and Analytics.",
        "skills": ["Process Improvement", "Leadership", "Budgeting", "Analytics"],
        "progression": ["Operations Manager", "Senior OM", "Ops Director"]
    },
    {
        "title": "Supply Chain Analyst",
        "description": "Improves supply chain efficiency and logistics. Key skills include Data Analysis, Forecasting, Logistics, and Negotiation.",
        "skills": ["Data Analysis", "Forecasting", "Logistics", "Negotiation"],
        "progression": ["Supply Chain Analyst", "Senior SCA", "SCA Manager"]
    },
    {
        "title": "IT Support Specialist",
        "description": "Provides technical support and solves IT issues for users. Key skills include Troubleshooting, Customer Service, Networking, and Hardware.",
        "skills": ["Troubleshooting", "Customer Service", "Networking", "Hardware"],
        "progression": ["IT Support Specialist", "IT Lead", "IT Manager"]
    },
    {
        "title": "Web Developer",
        "description": "Builds and maintains websites and web applications. Key skills include HTML, CSS, JavaScript, and APIs.",
        "skills": ["HTML", "CSS", "JavaScript", "APIs"],
        "progression": ["Web Developer", "Senior WD", "WD Lead"]
    },
    {
        "title": "Systems Analyst",
        "description": "Evaluates and improves IT systems and workflows. Key skills include Systems Design, Troubleshooting, SQL, and Documentation.",
        "skills": ["Systems Design", "Troubleshooting", "SQL", "Documentation"],
        "progression": ["Systems Analyst", "Senior SA", "Systems Architect"]
    },
    {
        "title": "Database Administrator",
        "description": "Manages and optimizes database performance and security. Key skills include SQL, Backup Management, Performance Tuning, and Security.",
        "skills": ["SQL", "Backup Management", "Performance Tuning", "Security"],
        "progression": ["Database Admin", "Senior DBA", "DB Architect"]
    },
    {
        "title": "Financial Analyst",
        "description": "Analyzes financial data to guide business decisions. Key skills include Excel, Forecasting, Modeling, and Reporting.",
        "skills": ["Excel", "Forecasting", "Modeling", "Reporting"],
        "progression": ["Financial Analyst", "Senior Analyst", "Finance Manager"]
    },
    {
        "title": "Human Resources Specialist",
        "description": "Handles recruiting, training, and employee relations. Key skills include Recruitment, Onboarding, Compliance, and Communication.",
        "skills": ["Recruitment", "Onboarding", "Compliance", "Communication"],
        "progression": ["HR Specialist", "HR Manager", "HR Director"]
    },
    {
        "title": "Nurse Practitioner",
        "description": "Provides advanced nursing care, often diagnosing and treating illnesses, prescribing medications, and managing patient health. Key skills include Clinical Assessment, Diagnosis, Medication Management, and Patient Communication.",
        "skills": ["Clinical Assessment", "Diagnosis", "Medication Management", "Patient Communication"],
        "progression": ["Nurse Practitioner", "Senior NP", "NP Lead / Director"]
    },
    {
        "title": "Physician Assistant",
        "description": "Works under physician supervision, performing exams, diagnosing illnesses, and prescribing treatments. Key skills include Physical Examination, Diagnostics, Treatment Planning, and Patient Counseling.",
        "skills": ["Physical Examination", "Diagnostics", "Treatment Planning", "Patient Counseling"],
        "progression": ["Physician Assistant", "Senior PA", "PA Supervisor"]
    },
    {
        "title": "Home Health Aide",
        "description": "Provides personal care and basic healthcare services to patients in their homes. Key skills include Personal Care Assistance, Medication Reminders, Vital Sign Monitoring, and Reporting.",
        "skills": ["Personal Care Assistance", "Medication Reminders", "Vital Sign Monitoring", "Reporting"],
        "progression": ["Home Health Aide", "Senior Home Health Aide", "Home Care Supervisor"]
    },
    {
        "title": "Physical Therapist Assistant",
        "description": "Assists physical therapists in delivering rehabilitation programs and exercises. Key skills include Therapeutic Exercise, Patient Mobility Support, Treatment Assist, and Progress Monitoring.",
        "skills": ["Therapeutic Exercise", "Patient Mobility Support", "Treatment Assist", "Progress Monitoring"],
        "progression": ["Physical Therapist Assistant", "Lead PTA", "PTA Manager"]
    },
    {
        "title": "Medical and Health Services Manager",
        "description": "Oversees operations of healthcare facilities, plans budgets, and coordinates staff and services. Key skills include Healthcare Administration, Budgeting, Regulatory Compliance, and Strategic Planning.",
        "skills": ["Healthcare Administration", "Budgeting", "Regulatory Compliance", "Strategic Planning"],
        "progression": ["Health Services Manager", "Senior Manager", "Director of Health Services"]
    },
    {
        "title": "Occupational Therapy Assistant",
        "description": "Supports occupational therapists in patient treatment plans to improve daily living skills. Key skills include Therapeutic Activities, Patient Coaching, Adaptive Equipment Use, and Progress Tracking.",
        "skills": ["Therapeutic Activities", "Patient Coaching", "Adaptive Equipment Use", "Progress Tracking"],
        "progression": ["Occupational Therapy Assistant", "Lead OTA", "OTA Supervisor"]
    },
    {
        "title": "Speech-Language Pathologist",
        "description": "Works with patients on speech, language, voice, and swallowing disorders. Key skills include Communication Assessment, Therapy Plan Design, Patient Exercises, and Progress Evaluation.",
        "skills": ["Communication Assessment", "Therapy Plan Design", "Patient Exercises", "Progress Evaluation"],
        "progression": ["Speech-Language Pathologist", "Senior SLP", "SLP Lead"]
    },
    {
        "title": "Registered Nurse",
        "description": "Provides direct patient care, administers medications, monitors outcomes, and coordinates with healthcare teams. Key skills include Patient Assessment, Medication Administration, Care Coordination, and Documentation.",
        "skills": ["Patient Assessment", "Medication Administration", "Care Coordination", "Documentation"],
        "progression": ["Registered Nurse", "Charge Nurse", "Nurse Manager"]
    },
    {
        "title": "Occupational Therapist",
        "description": "Helps patients regain skills for daily living and work after injury or illness. Key skills include Activity Analysis, Therapeutic Intervention, Adaptive Tools, and Patient Education.",
        "skills": ["Activity Analysis", "Therapeutic Intervention", "Adaptive Tools", "Patient Education"],
        "progression": ["Occupational Therapist", "Senior OT", "OT Director"]
    },
    {
        "title": "Medical Assistant",
        "description": "Supports clinical and administrative duties in medical offices, such as taking vitals, assisting with exams, and managing records. Key skills include Vital Signs, Clinical Support, EHR Documentation, and Patient Interaction.",
        "skills": ["Vital Signs", "Clinical Support", "EHR Documentation", "Patient Interaction"],
        "progression": ["Medical Assistant", "Senior MA", "MA Supervisor"]
    },
    {
        "title": "Phlebotomist",
        "description": "Specializes in drawing blood samples for tests, transfusions, or donations. Key skills include Venipuncture, Specimen Handling, Patient Prep, and Safety Protocols.",
        "skills": ["Venipuncture", "Specimen Handling", "Patient Prep", "Safety Protocols"],
        "progression": ["Phlebotomist", "Lead Phlebotomist", "Phlebotomy Supervisor"]
    },
    {
        "title": "Dietitian / Nutritionist",
        "description": "Advises clients and patients on healthy eating to improve or manage conditions. Key skills include Nutritional Assessment, Meal Planning, Diet Counseling, and Monitoring.",
        "skills": ["Nutritional Assessment", "Meal Planning", "Diet Counseling", "Monitoring"],
        "progression": ["Dietitian", "Senior Dietitian", "Nutrition Director"]
    },
    {
        "title": "Massage Therapist",
        "description": "Uses hands-on techniques to manipulate muscles and tissues to promote health and relaxation. Key skills include Soft Tissue Manipulation, Client Assessment, Tissue Stretching, and Wellness Education.",
        "skills": ["Soft Tissue Manipulation", "Client Assessment", "Tissue Stretching", "Wellness Education"],
        "progression": ["Massage Therapist", "Senior MT", "Wellness Spa Manager"]
    },
    {
        "title": "Certified Registered Nurse Anesthetist (CRNA)",
        "description": "Administers anesthesia and monitors patient status during surgery and procedures. Key skills include Anesthesia Planning, Airway Management, Monitoring, and Pharmacology.",
        "skills": ["Anesthesia Planning", "Airway Management", "Monitoring", "Pharmacology"],
        "progression": ["CRNA", "Senior CRNA", "Anesthesia Director"]
    },
    {
        "title": "Health Information Technologist / Medical Registrar",
        "description": "Manages and analyzes medical records and health data systems. Key skills include EHR Management, Data Analytics, Information Security, and Health Coding.",
        "skills": ["EHR Management", "Data Analytics", "Information Security", "Health Coding"],
        "progression": ["Health Information Tech", "Senior HIT", "Health Informatics Manager"]
    },
    {
        "title": "Biomedical Equipment Technician",
        "description": "Installs, maintains, and repairs medical equipment used in healthcare settings. Key skills include Equipment Calibration, Troubleshooting, Preventive Maintenance, and Technical Documentation.",
        "skills": ["Equipment Calibration", "Troubleshooting", "Preventive Maintenance", "Technical Documentation"],
        "progression": ["Biomedical Equipment Technician", "Senior Technician", "Equipment Manager"]
    },
    {
        "title": "Respiratory Therapist",
        "description": "Treats patients with breathing or cardiopulmonary disorders, administering therapies and managing ventilators. Key skills include Respiratory Assessment, Ventilator Management, Patient Education, and Airway Support.",
        "skills": ["Respiratory Assessment", "Ventilator Management", "Patient Education", "Airway Support"],
        "progression": ["Respiratory Therapist", "Senior RT", "RT Supervisor"]
    },
    {
        "title": "Epidemiologist",
        "description": "Studies patterns and causes of diseases in populations to inform public health interventions. Key skills include Statistical Analysis, Epidemiologic Methods, Data Modeling, and Public Health Policy.",
        "skills": ["Statistical Analysis", "Epidemiologic Methods", "Data Modeling", "Public Health Policy"],
        "progression": ["Epidemiologist", "Senior Epidemiologist", "Public Health Director"]
    },
    {
        "title": "Speech Language Pathology Assistant",
        "description": "Supports speech-language pathologists in treatment sessions, preparing materials and assisting with therapy. Key skills include Therapy Preparation, Communication Exercises, Patient Monitoring, and Progress Reporting.",
        "skills": ["Therapy Preparation", "Communication Exercises", "Patient Monitoring", "Progress Reporting"],
        "progression": ["SLP Assistant", "Lead Assistant", "SLP Support Manager"]
    },
    {
        "title": "Audiologist",
        "description": "Diagnoses and treats hearing and balance disorders. Key skills include Audiometric Testing, Hearing Aid Fitting, Counseling, and Vestibular Assessment.",
        "skills": ["Audiometric Testing", "Hearing Aid Fitting", "Counseling", "Vestibular Assessment"],
        "progression": ["Audiologist", "Senior Audiologist", "Audiology Manager"]
    },
    {
        "title": "Orthotist / Prosthetist",
        "description": "Designs and fits orthotic and prosthetic devices to support patient mobility. Key skills include Biomechanical Assessment, Device Design, Fitting, and Adjustment.",
        "skills": ["Biomechanical Assessment", "Device Design", "Fitting", "Adjustment"],
        "progression": ["Orthotist / Prosthetist", "Senior OP", "OP Director"]
    },
    {
        "title": "Chiropractor",
        "description": "Diagnoses and treats neuromuscular disorders, focusing on spine alignment. Key skills include Spinal Adjustment, Patient Assessment, Manual Therapy, and Rehabilitation Planning.",
        "skills": ["Spinal Adjustment", "Patient Assessment", "Manual Therapy", "Rehabilitation Planning"],
        "progression": ["Chiropractor", "Senior Chiropractor", "Clinic Owner"]
    },
    {
        "title": "Medical Laboratory Technician",
        "description": "Performs lab tests and analyses on patient samples to support diagnosis. Key skills include Sample Handling, Laboratory Techniques, Quality Control, and Data Reporting.",
        "skills": ["Sample Handling", "Laboratory Techniques", "Quality Control", "Data Reporting"],
        "progression": ["Lab Technician", "Senior Lab Technician", "Lab Supervisor"]
    }
]
