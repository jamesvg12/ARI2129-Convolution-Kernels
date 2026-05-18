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
│   ├── requirements_simulator.txt
│   └── README_SIMULATOR.md
└── further_reading/
    ├── Chollet (2017).pdf
    ├── Fukushima (1980).pdf
    ├── Haussler (1999).pdf
    ├── Howard et al. (2017).pdf
    ├── Krizhevsky et al. (2012).pdf
    ├── LeCun et al. (1998).pdf
    ├── Waibel et al. (1989).pdf
    └── Yu & Koltun (2016).pdf

---

## Running the Simulator

**Step 1 — Install dependencies:**
```bash
pip install -r simulator/requirements_simulator.txt
```

**Step 2 — Launch:**
```bash
streamlit run simulator/app.py
```

The simulator opens in your browser automatically. It allows you to adjust kernel type, kernel size, stride, padding, and dilation, and see the visual output update in real time.

---

## Running the Notebook

Install dependencies:

    pip install -r requirements.txt

Then launch:

    jupyter notebook walkthrough.ipynb

---

## Team

James Vella Gera, Gregory Vella, Nathan Tanti, Dusan Dinic, Dimitrios Paschalidis
