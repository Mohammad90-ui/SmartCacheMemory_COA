# 🧠 Smart Cache Memory Simulator

An interactive educational web application that simulates and compares **FIFO** (First-In, First-Out) and **LRU** (Least Recently Used) cache replacement policies side by side.

Built with **Python**, **Streamlit**, and **Plotly**.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Dual Simulation** | Run FIFO and LRU on the same input and compare results |
| **Step-by-Step View** | See each memory reference's hit/miss result and cache state |
| **Interactive Charts** | Grouped bar chart, hit-ratio gauges, cumulative line chart |
| **Input Validation** | Clear error messages for invalid sequences or capacity |
| **Learning Panel** | Sidebar explanations of key cache concepts |
| **Result Analysis** | Auto-generated plain-language comparison of policy outcomes |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or later

### Installation

```bash
# Clone or navigate to the project directory
cd Smart_Cache_Memory

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The app opens in your default browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
Smart_Cache_Memory/
├── app.py                 # Streamlit interface (presentation layer)
├── cache_algorithms.py    # FIFO and LRU simulation functions
├── metrics.py             # Hit/miss and ratio calculations
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🎯 How to Use

1. **Enter a sequence** – Type comma-separated non-negative integers (e.g. `1, 2, 3, 1, 4, 2, 5`) in the sidebar.
2. **Set cache capacity** – Choose how many blocks the cache can hold (default: 3).
3. **Run Simulation** – Click the button to execute both FIFO and LRU.
4. **Explore results** – View summary metrics, comparison charts, step-by-step tables, final cache states, and an explanation of the outcome.
5. **Experiment** – Change the sequence or capacity and re-run to see how results change.

---

## 📖 Key Concepts

| Term | Definition |
|------|-----------|
| **Cache Hit** | The requested block is already in the cache |
| **Cache Miss** | The requested block is not in the cache |
| **FIFO** | Evicts the block that entered the cache earliest |
| **LRU** | Evicts the block that was accessed least recently |
| **Hit Ratio** | Hits ÷ Total Requests (as a percentage) |

---

## ⚠️ Disclaimer

This is a **software simulation** for educational purposes. It does not interact with or measure your computer's physical CPU cache.

---

## 📄 License

This project is provided for educational use.
