# Airline Technician Assistant LLM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Project Description
This project fine-tunes an open-source language model to assist airline technicians. Given a problem description, the model predicts the recommended maintenance action.  
The project demonstrates **instruction-tuning with LoRA** on a small dataset while creating a practical AI assistant for industrial applications.

---

## Motivation
Airline maintenance requires fast and accurate decisions to ensure safety and minimize downtime. A model that can quickly suggest maintenance actions based on technician-reported problems can support decision-making and improve efficiency in real-world scenarios.

---

## Dataset
- Custom dataset of **problem-action pairs** in CSV format.
- Columns:
  - `problem`: Description of the maintenance issue.
  - `action`: Recommended action to solve it.
- Example:

| Problem | Action |
|---------|--------|
| Engine vibration at takeoff | Check fan blades for damage, inspect mounts, log vibration readings |

> Dataset is included in `data/Aircraft_Annotation_DataFile..csv` or can be downloaded from Kaggle.

---

## Tech Stack
- Python 3.12
- Hugging Face Transformers
- PEFT & LoRA
- Datasets (Hugging Face)
- Gradio for interactive demo
- GPU runtime (Colab recommended)
- BitsAndBytes (optional, for 8-bit training)

---

## Project Walkthrough

### 1. Dataset Exploration
<img width="1863" height="797" alt="Screenshot from 2025-10-05 14-43-36" src="https://github.com/user-attachments/assets/6f00a1bf-1944-461f-b154-f16b20f55e1c" />

Explored the airline maintenance problem-action pairs in the CSV file. Verified the structure and examples to ensure proper formatting for tokenization.

### 2. Data Preprocessing
<img width="1919" height="897" alt="Screenshot from 2025-10-05 14-44-44" src="https://github.com/user-attachments/assets/3e52f467-f10f-4502-97cb-bd017900819b" />

Tokenized instruction-response pairs using Hugging Face tokenizer and prepared `input_ids` and `labels` for training. Set `pad_token = eos_token` to handle padding issues in causal LM.

### 3. LoRA Fine-Tuning
<img width="1858" height="376" alt="Screenshot from 2025-10-05 14-45-10" src="https://github.com/user-attachments/assets/8382e678-5181-46c1-bfb5-7a542b609dd9" />

Fine-tuned the MPT-7B-Instruct model using **LoRA** in Google Colab. Training was done on a small dataset for demonstration purposes. Monitored loss to ensure learning.

### 4. Model Testing
<img width="1858" height="376" alt="Screenshot from 2025-10-05 14-47-04" src="https://github.com/user-attachments/assets/67d38764-cfba-4158-8c53-1c3c11b331bf" />

Tested the model with new problems. Example input: *“Problem: Engine vibration at takeoff. What should the technician do?. Shows the model generalizes well to unseen problems.

### 5. Gradio Demo


https://github.com/user-attachments/assets/db9ee0e7-68c5-4203-ba86-3d2f94ccb49f


Interactive interface for technicians to type problems and get recommended actions. Demonstrates **real-world applicability** and usability.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
