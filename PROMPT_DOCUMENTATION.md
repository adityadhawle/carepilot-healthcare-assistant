# CarePilot — AI Prompt Engineering Documentation



**Project:** CarePilot — AI Healthcare Assistant  

**Domain:** Healthcare / Website Development  

**Developer:** Aditya Dhawle  

**Repository:** https://github.com/adityadhawle/carepilot-healthcare-assistant



## 1. Project Objective



The objective was to build a functional healthcare web application that allows users to explore basic health guidance, submit appointment requests, and manage appointments through a dashboard.



The application was developed using Python, Streamlit, and Pandas. ChatGPT was used as an AI development assistant to help with implementation, debugging, iterative improvements, and documentation.



**Important limitation:** The health guidance feature uses keyword-based rules. It is a prototype, not an AI medical model, diagnostic system, or substitute for professional medical advice.



## 2. AI Tools and Technologies



\- **ChatGPT:** Assisted with code generation, debugging, UI improvements, troubleshooting, and project documentation.

\- **Python:** Application programming language.

\- **Streamlit:** Web application framework.

\- **Pandas:** Appointment data handling using CSV files.

\- **PowerShell and VS Code:** Development, testing, and project file management.

\- **Git and GitHub:** Version control and project publication.



## 3. Prompts Used During Development



The following prompts are reconstructed from the available project history where the original wording could not be verified. They describe the development requests and must not be treated as verbatim copies of every original chat message.



### Prompt 1 — Project planning and initial development



**Type:** Reconstructed prompt



“Help me build a functional AI Healthcare Assistant web application for a practical AI Growth \& Automation Associate assessment. Use Python and Streamlit. Include a home page, health guidance, appointment booking, and a dashboard. Explain the steps clearly and help me implement and test the application.”



**Purpose:** Establish the project scope and build a practical healthcare prototype rather than submitting only an idea.



### Prompt 2 — Health guidance and safety



**Type:** Reconstructed prompt



“Implement a health guidance feature that responds to common symptom-related keywords with basic informational guidance. Include a clear disclaimer that the feature is rule-based and does not provide medical diagnosis. Add appropriate emergency guidance for warning signs such as chest pain, breathing difficulty, severe bleeding, unconsciousness, and stroke symptoms.”



**Purpose:** Make the prototype useful while communicating its limitations and directing users toward emergency assistance when appropriate.



### Prompt 3 — Appointment booking and data persistence



**Type:** Reconstructed prompt



“Implement an appointment booking form using Streamlit and Pandas. Collect the patient's name, email, appointment date, and reason for the visit. Store appointment records in `data/appointments.csv` and make sure existing records are preserved when new appointments are added.”



**Purpose:** Turn the project into a working application with persistent appointment records.



### Prompt 4 — Debugging a broken application file



**Type:** Reconstructed prompt based on the recorded debugging session



“My `app.py` file is broken and begins with old text instead of Python imports, causing an `IndentationError`. Help me inspect the file, preserve a backup, restore valid Python code, and verify that the Streamlit application runs correctly.”



**Purpose:** Recover the application safely instead of continuing to build on a broken file.



### Prompt 5 — Fixing Home page navigation



**Type:** Reconstructed prompt



“The Home page navigation is causing a `StreamlitWidgetAlreadyInstantiatedError` when changing the page navigation state after a widget has been created. Help me fix the navigation flow without breaking the existing pages or appointment functionality.”



**Purpose:** Resolve a Streamlit state-management issue and make navigation reliable.



### Prompt 6 — Dashboard appointment management



**Type:** Reconstructed prompt



“Improve the dashboard by displaying appointment summary cards, adding appointment search and status filters, enabling CSV download, and allowing the user to update an appointment's status. Save changes to the existing CSV file and preserve appointment records when the application is refreshed or restarted.”



**Purpose:** Improve usability and add practical record-management functionality.



### Prompt 7 — GitHub safety and project documentation



**Type:** Reconstructed prompt



“Help me prepare the CarePilot project for GitHub. Configure `.gitignore` to exclude virtual environments, appointment data, backup files, and secrets. Prepare a README and organize screenshots for the Home page, Health Guidance, Book Appointment, and Dashboard. Verify the staged files before committing and pushing.”



**Purpose:** Publish the project while reducing the risk of exposing local data or configuration secrets.



## 4. Iterative Prompt Refinement and Problem-Solving



The development process involved multiple rounds of implementation, testing, and refinement.



| Challenge | Refinement approach | Outcome |

|---|---|---|

| Broken Python file | Inspect, back up, and repair the application code | Valid application structure restored |

| Navigation state error | Refine the page-navigation logic | Navigation issue addressed |

| Appointment persistence | Verify CSV read/write behaviour and status updates | Appointment management implemented |

| GitHub privacy | Review ignore rules and staged files | Data and backup files excluded from the commit |

| Project presentation | Add README and four screenshots | Repository documentation improved |



## 5. Development and Verification Approach



The application was developed incrementally. Each significant change was followed by inspection, execution, or manual testing. The appointment workflow and dashboard status update were checked during development. Git status was inspected before the documentation commit.



The README and four screenshots were committed and pushed to the `main` branch in commit `a40d791`.



## 6. Final Outcome



CarePilot is a Streamlit healthcare prototype with:



\- A home page introducing the application.

\- Rule-based health guidance with safety disclaimers.

\- Appointment booking and CSV-based persistence.

\- A dashboard with appointment search, status filtering, status updates, and CSV export.

\- A README and screenshots published in a GitHub repository.



**Project link:** https://github.com/adityadhawle/carepilot-healthcare-assistant



## 7. Transparency Note



This document summarizes the development workflow using the available project history. The prompt examples above are reconstructed summaries, not a guaranteed verbatim transcript of every prompt used. Before final submission, they should be supplemented with any original prompts that can still be recovered from the conversation history.



Only features and tests actually completed should be claimed in the final video presentation.




