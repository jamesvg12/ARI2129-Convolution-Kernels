# ARI 2129 — Convolution Kernels Learning Pack

**Module:** ARI 2129 · Principles of Computer Vision for AI
**Topic:** Area Processing — Convolution Kernels
**Deadline:** 18th May 2026

---

## Overview

This repository contains the full Learning Pack for the Convolution Kernels topic. It contains the following structure:

```
/
├── README.md
├── requirements.txt
├── study_notes.docx
├── study_notes.pdf
├── quiz_with_rationale.docx
├── quiz_with_rationale.pdf
├── quiz_link.txt
├── slides.pptx
├── slides.pdf
├── walkthrough.ipynb
├── ai_journal.pdf
├── simulator/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── further_reading/
    └── further_reading.pdf
```

---

## Running the Simulator

**Step 1 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 2 — Launch:**
```bash
streamlit run simulator/app.py
```

The simulator opens in your browser automatically. It allows you to adjust kernel type, kernel size, stride, padding, and dilation, and see the visual output update in real time.

---

## Running the Notebook

```bash
jupyter notebook walkthrough.ipynb
```

---

## Team

James Vella Gera, Gregory Vella, Nathan Tanti, Dusan Dinic, Dimitrios Paschalidis