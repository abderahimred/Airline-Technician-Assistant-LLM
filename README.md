# Airline Technician Assistant LLM

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Table of Contents
- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Dataset](#dataset)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Results](#results)
- [Future Work](#future-work)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Project Overview
This project fine-tunes an open-source language model to assist airline technicians. Given a problem description, the model predicts the recommended maintenance action.  
The goal is to demonstrate **instruction-tuning with LoRA** on a small dataset while creating a practical AI assistant for industry applications.

---

## Motivation
Airline maintenance requires fast, accurate decisions to ensure safety and reduce downtime. A model that can quickly suggest appropriate actions based on problem reports can assist technicians, especially in high-pressure scenarios.

---

## Dataset
- **Source:** Custom dataset of problem-action pairs.
- **Format:** CSV file with two columns:
  - `problem`: Description of the maintenance issue.
  - `action`: Recommended action to solve it.
- **Example:**

| Problem | Action |
|---------|--------|
| Engine vibration at takeoff | Check fan blades for damage, inspect mounts, log vibration readings |

> **Note:** Dataset is included in `data/` or can be downloaded from Kaggle: [dataset link]

---

## Tech Stack
- **Python 3.12**
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [PEFT & LoRA](https://github.com/huggingface/peft)
- [Datasets](https://huggingface.co/docs/datasets/)
- [Gradio](https://gradio.app/) (for interactive demo)
- GPU runtime (Colab recommended)
- Optional: [BitsAndBytes](https://github.com/TimDettmers/bitsandbytes) for 8-bit training

---

## Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/airline-tech-assistant.git
cd airline-tech-assistant
pip install -r requirements.txt
