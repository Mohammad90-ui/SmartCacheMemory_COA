"""
Smart Cache Memory Simulator
==============================
Streamlit application – presentation layer (v2 — animated & premium).
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from cache_algorithms import simulate_fifo, simulate_lru
from metrics import calculate_metrics, format_ratio

# ─────────────────────────────────────────────────────────
#  Page configuration
# ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Smart Cache Memory Simulator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────
#  Mega CSS – animations, glassmorphism, particles, glow
# ─────────────────────────────────────────────────────────

st.markdown(
    """
    <style>
    /* ============================================
       GOOGLE FONT
       ============================================ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ============================================
       CSS VARIABLES
       ============================================ */
    :root {
        --bg-primary: #080b14;
        --bg-card: rgba(16,20,34,0.75);
        --bg-card-solid: #101424;
        --accent-cyan: #00d4ff;
        --accent-violet: #a855f7;
        --accent-emerald: #10b981;
        --accent-rose: #f43f5e;
        --accent-amber: #f59e0b;
        --accent-blue: #3b82f6;
        --text-primary: #e8eaf0;
        --text-muted: #8892a8;
        --border-subtle: rgba(255,255,255,0.06);
        --border-glow: rgba(0,212,255,0.15);
        --glass-bg: rgba(14,17,30,0.6);
        --glass-border: rgba(255,255,255,0.08);
    }

    /* ============================================
       KEYFRAME ANIMATIONS
       ============================================ */

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(28px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(30px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.85); }
        to   { opacity: 1; transform: scale(1); }
    }

    @keyframes slideInScale {
        from { opacity: 0; transform: scale(0.9) translateY(15px); }
        to   { opacity: 1; transform: scale(1) translateY(0); }
    }

    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 15px rgba(0,212,255,0.15), 0 0 30px rgba(0,212,255,0.05); }
        50%      { box-shadow: 0 0 25px rgba(0,212,255,0.3), 0 0 50px rgba(0,212,255,0.1); }
    }

    @keyframes pulseGlowViolet {
        0%, 100% { box-shadow: 0 0 15px rgba(168,85,247,0.15), 0 0 30px rgba(168,85,247,0.05); }
        50%      { box-shadow: 0 0 25px rgba(168,85,247,0.3), 0 0 50px rgba(168,85,247,0.1); }
    }

    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        33%      { transform: translateY(-12px) rotate(2deg); }
        66%      { transform: translateY(6px) rotate(-1deg); }
    }

    @keyframes shimmer {
        0%   { background-position: -200% center; }
        100% { background-position: 200% center; }
    }

    @keyframes borderGlow {
        0%, 100% { border-color: rgba(0,212,255,0.15); }
        50%      { border-color: rgba(168,85,247,0.25); }
    }

    @keyframes textGlow {
        0%, 100% { text-shadow: 0 0 10px rgba(0,212,255,0.3); }
        50%      { text-shadow: 0 0 20px rgba(0,212,255,0.6), 0 0 40px rgba(168,85,247,0.2); }
    }

    @keyframes particleFloat1 {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.4; }
        25%      { transform: translate(80px, -120px) scale(1.2); opacity: 0.7; }
        50%      { transform: translate(-40px, -200px) scale(0.8); opacity: 0.3; }
        75%      { transform: translate(60px, -100px) scale(1.1); opacity: 0.6; }
    }

    @keyframes particleFloat2 {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.3; }
        25%      { transform: translate(-100px, -80px) scale(0.9); opacity: 0.6; }
        50%      { transform: translate(50px, -180px) scale(1.3); opacity: 0.4; }
        75%      { transform: translate(-70px, -140px) scale(1); opacity: 0.5; }
    }

    @keyframes particleFloat3 {
        0%, 100% { transform: translate(0, 0) rotate(0deg); opacity: 0.3; }
        50%      { transform: translate(40px, -160px) rotate(180deg); opacity: 0.6; }
    }

    @keyframes orbGlow {
        0%, 100% { opacity: 0.15; transform: scale(1); }
        50%      { opacity: 0.25; transform: scale(1.15); }
    }

    @keyframes typing {
        from { width: 0; }
        to   { width: 100%; }
    }

    @keyframes blink {
        0%, 100% { opacity: 1; }
        50%      { opacity: 0; }
    }

    @keyframes ripple {
        0%   { transform: scale(0.95); opacity: 0.7; }
        100% { transform: scale(1.8); opacity: 0; }
    }

    @keyframes badgePop {
        0%   { transform: scale(0); opacity: 0; }
        60%  { transform: scale(1.15); }
        100% { transform: scale(1); opacity: 1; }
    }

    /* ============================================
       GLOBAL RESETS & BASE
       ============================================ */
    html, body, [data-testid="stAppViewContainer"],
    [data-testid="stApp"] {
        font-family: 'Inter', -apple-system, sans-serif !important;
        color: var(--text-primary);
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(ellipse 80% 60% at 10% 20%, rgba(0,212,255,0.06) 0%, transparent 60%),
            radial-gradient(ellipse 60% 50% at 85% 70%, rgba(168,85,247,0.06) 0%, transparent 60%),
            radial-gradient(ellipse 50% 40% at 50% 50%, rgba(16,185,129,0.03) 0%, transparent 50%),
            var(--bg-primary);
    }

    /* ============================================
       FLOATING PARTICLE BACKGROUND
       ============================================ */
    .particles-container {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    .particle {
        position: absolute;
        border-radius: 50%;
    }
    .p1 { width: 6px; height: 6px; background: rgba(0,212,255,0.4); top: 85%; left: 15%;
          animation: particleFloat1 14s ease-in-out infinite; }
    .p2 { width: 4px; height: 4px; background: rgba(168,85,247,0.5); top: 90%; left: 55%;
          animation: particleFloat2 18s ease-in-out infinite 2s; }
    .p3 { width: 8px; height: 8px; background: rgba(16,185,129,0.3); top: 80%; left: 75%;
          animation: particleFloat3 22s ease-in-out infinite 4s; }
    .p4 { width: 5px; height: 5px; background: rgba(0,212,255,0.3); top: 95%; left: 35%;
          animation: particleFloat1 16s ease-in-out infinite 6s; }
    .p5 { width: 3px; height: 3px; background: rgba(244,63,94,0.4); top: 88%; left: 90%;
          animation: particleFloat2 20s ease-in-out infinite 3s; }
    .p6 { width: 7px; height: 7px; background: rgba(245,158,11,0.25); top: 92%; left: 8%;
          animation: particleFloat3 17s ease-in-out infinite 1s; }
    .p7 { width: 4px; height: 4px; background: rgba(168,85,247,0.35); top: 70%; left: 45%;
          animation: particleFloat1 19s ease-in-out infinite 5s; }
    .p8 { width: 5px; height: 5px; background: rgba(0,212,255,0.25); top: 75%; left: 65%;
          animation: particleFloat2 15s ease-in-out infinite 7s; }

    /* Ambient orbs */
    .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(80px);
    }
    .orb1 { width: 300px; height: 300px; background: rgba(0,212,255,0.08);
            top: 10%; left: 5%; animation: orbGlow 8s ease-in-out infinite; }
    .orb2 { width: 250px; height: 250px; background: rgba(168,85,247,0.07);
            top: 50%; right: 5%; animation: orbGlow 10s ease-in-out infinite 3s; }
    .orb3 { width: 200px; height: 200px; background: rgba(16,185,129,0.05);
            bottom: 10%; left: 40%; animation: orbGlow 12s ease-in-out infinite 5s; }

    /* ============================================
       SIDEBAR
       ============================================ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0c0f1a 0%, #111528 50%, #0e1220 100%) !important;
        border-right: 1px solid var(--glass-border);
    }
    [data-testid="stSidebar"] > div:first-child {
        animation: fadeInLeft 0.6s ease-out;
    }

    /* ============================================
       METRIC CARDS – animated
       ============================================ */
    [data-testid="stMetric"] {
        background: var(--glass-bg);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 18px 22px;
        animation: slideInScale 0.5s ease-out both,
                   borderGlow 4s ease-in-out infinite;
        transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        overflow: hidden;
    }
    [data-testid="stMetric"]::before {
        content: '';
        position: absolute;
        top: 0; left: -200%;
        width: 200%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
        animation: shimmer 4s ease-in-out infinite;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-4px) scale(1.02);
        border-color: rgba(0,212,255,0.3);
        box-shadow: 0 8px 32px rgba(0,212,255,0.15),
                    0 0 60px rgba(0,212,255,0.05);
    }
    [data-testid="stMetric"] label {
        color: var(--text-muted) !important;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-size: 0.68rem !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-weight: 800 !important;
        font-size: 1.7rem !important;
        background: linear-gradient(135deg, #fff 0%, #c4d0e0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ============================================
       BUTTONS – gradient + ripple
       ============================================ */
    .stButton > button {
        background: linear-gradient(135deg, #00d4ff 0%, #7c3aed 50%, #f43f5e 100%);
        background-size: 200% 200%;
        animation: gradientShift 4s ease infinite;
        color: #fff !important;
        border: none;
        border-radius: 14px;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: 0.04em;
        padding: 0.75rem 2rem;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        box-shadow: 0 4px 20px rgba(0,212,255,0.2), 0 0 40px rgba(168,85,247,0.1);
        position: relative;
        overflow: hidden;
    }
    .stButton > button::after {
        content: '';
        position: absolute;
        top: 50%; left: 50%;
        width: 0; height: 0;
        border-radius: 50%;
        background: rgba(255,255,255,0.2);
        transform: translate(-50%, -50%);
        transition: width 0.6s ease, height 0.6s ease;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.03);
        box-shadow: 0 8px 30px rgba(0,212,255,0.35),
                    0 0 60px rgba(168,85,247,0.2);
    }
    .stButton > button:hover::after {
        width: 300px; height: 300px;
    }
    .stButton > button:active {
        transform: translateY(-1px) scale(1.01);
    }

    /* ============================================
       EXPANDERS – glassmorphism
       ============================================ */
    [data-testid="stExpander"] {
        background: var(--glass-bg);
        backdrop-filter: blur(12px);
        border: 1px solid var(--glass-border);
        border-radius: 14px;
        overflow: hidden;
        transition: all 0.3s ease;
        animation: fadeInUp 0.4s ease-out both;
    }
    [data-testid="stExpander"]:hover {
        border-color: rgba(0,212,255,0.2);
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }

    /* ============================================
       TABS – animated underline
       ============================================ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: var(--glass-bg);
        border-radius: 14px;
        padding: 6px;
        backdrop-filter: blur(12px);
        border: 1px solid var(--glass-border);
        animation: fadeInUp 0.5s ease-out both;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        color: var(--text-muted);
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.04);
        color: var(--text-primary);
    }
    .stTabs [aria-selected="true"] {
        background: rgba(0,212,255,0.1) !important;
        color: var(--accent-cyan) !important;
        box-shadow: 0 2px 12px rgba(0,212,255,0.15);
    }

    /* ============================================
       HERO HEADER – animated gradient text
       ============================================ */
    .hero-container {
        text-align: center;
        padding: 2rem 0 1rem;
        animation: fadeInDown 0.7s ease-out both;
        position: relative;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00d4ff 0%, #a855f7 30%, #f43f5e 60%, #f59e0b 80%, #00d4ff 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientShift 6s ease infinite, textGlow 3s ease-in-out infinite;
        letter-spacing: -0.03em;
        margin-bottom: 0.3rem;
        line-height: 1.2;
    }
    .hero-sub {
        color: var(--text-muted);
        font-size: 1.1rem;
        font-weight: 400;
        animation: fadeInUp 0.8s ease-out 0.3s both;
        letter-spacing: 0.01em;
    }
    .hero-badge {
        display: inline-block;
        margin-top: 12px;
        padding: 5px 16px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        background: rgba(0,212,255,0.08);
        border: 1px solid rgba(0,212,255,0.2);
        color: var(--accent-cyan);
        animation: fadeInUp 0.9s ease-out 0.5s both, pulseGlow 3s ease-in-out infinite 1s;
    }

    /* ============================================
       HIT / MISS BADGES – pop animation
       ============================================ */
    .badge-hit {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: rgba(16,185,129,0.12);
        color: #34d399;
        border: 1px solid rgba(16,185,129,0.25);
        padding: 3px 12px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.75rem;
        letter-spacing: 0.04em;
        animation: badgePop 0.4s ease-out both;
        transition: all 0.2s ease;
    }
    .badge-hit:hover {
        background: rgba(16,185,129,0.2);
        transform: scale(1.08);
        box-shadow: 0 0 12px rgba(16,185,129,0.3);
    }
    .badge-miss {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: rgba(244,63,94,0.12);
        color: #fb7185;
        border: 1px solid rgba(244,63,94,0.25);
        padding: 3px 12px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.75rem;
        letter-spacing: 0.04em;
        animation: badgePop 0.4s ease-out both;
        transition: all 0.2s ease;
    }
    .badge-miss:hover {
        background: rgba(244,63,94,0.2);
        transform: scale(1.08);
        box-shadow: 0 0 12px rgba(244,63,94,0.3);
    }

    /* ============================================
       SECTION LABELS – animated
       ============================================ */
    .section-label {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.3rem;
        font-weight: 800;
        margin: 1.6rem 0 0.8rem;
        animation: fadeInLeft 0.5s ease-out both;
        position: relative;
    }
    .section-label::after {
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--glass-border), transparent);
        margin-left: 12px;
    }
    .section-label .icon {
        font-size: 1.6rem;
        animation: float 4s ease-in-out infinite;
    }

    /* ============================================
       INFO CARDS – glassmorphism + hover glow
       ============================================ */
    .info-card {
        background: var(--glass-bg);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--glass-border);
        border-radius: 18px;
        padding: 24px 28px;
        margin-bottom: 14px;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        animation: slideInScale 0.5s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .info-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 2px;
        background: linear-gradient(90deg, transparent, var(--accent-cyan), var(--accent-violet), transparent);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    .info-card:hover {
        border-color: rgba(0,212,255,0.2);
        transform: translateY(-3px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.3),
                    0 0 30px rgba(0,212,255,0.08);
    }
    .info-card:hover::before {
        opacity: 1;
    }
    .info-card h4 {
        margin: 0 0 8px;
        font-weight: 800;
        font-size: 1.05rem;
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-violet));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .info-card p {
        margin: 0;
        color: var(--text-muted);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* ============================================
       STEP TABLE – staggered rows
       ============================================ */
    .step-table-header {
        display: flex;
        gap: 12px;
        padding: 8px 16px;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #5a6480;
        border-bottom: 1px solid var(--glass-border);
        margin-bottom: 6px;
        animation: fadeInUp 0.3s ease-out both;
    }
    .step-row {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 16px;
        border-radius: 10px;
        margin-bottom: 3px;
        font-size: 0.88rem;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        animation: fadeInUp 0.4s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .step-row::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.02), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .step-row:hover {
        background: rgba(255,255,255,0.03);
        transform: translateX(4px);
    }
    .step-row:hover::before {
        opacity: 1;
    }
    .step-row.hit-row {
        border-left: 3px solid var(--accent-emerald);
        background: rgba(16,185,129,0.03);
    }
    .step-row.miss-row {
        border-left: 3px solid var(--accent-rose);
        background: rgba(244,63,94,0.03);
    }
    .step-num {
        min-width: 30px;
        font-weight: 800;
        color: #4a5568;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
    }
    .step-addr {
        min-width: 50px;
        font-weight: 700;
        color: var(--text-primary);
        font-family: 'JetBrains Mono', monospace;
    }
    .step-cache {
        flex: 1;
        font-family: 'JetBrains Mono', monospace;
        color: var(--text-muted);
        font-size: 0.82rem;
    }
    .step-evict {
        min-width: 70px;
        color: var(--accent-amber);
        font-weight: 600;
        font-size: 0.8rem;
        font-family: 'JetBrains Mono', monospace;
    }

    /* ============================================
       GLASS PANEL – premium container
       ============================================ */
    .glass-panel {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 28px 32px;
        margin-bottom: 16px;
        animation: slideInScale 0.5s ease-out both;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    .glass-panel:hover {
        border-color: rgba(255,255,255,0.12);
        box-shadow: 0 8px 40px rgba(0,0,0,0.25);
    }
    .glass-panel::after {
        content: '';
        position: absolute;
        top: -1px; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent 10%, rgba(0,212,255,0.3), rgba(168,85,247,0.3), transparent 90%);
    }

    /* ============================================
       CACHE SLOT BLOCKS – animated
       ============================================ */
    .cache-slot {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 48px;
        height: 48px;
        border-radius: 12px;
        padding: 6px 18px;
        margin: 5px;
        font-weight: 800;
        font-size: 1.1rem;
        font-family: 'JetBrains Mono', monospace;
        animation: scaleIn 0.4s ease-out both;
        transition: all 0.3s ease;
        position: relative;
    }
    .cache-slot:hover {
        transform: translateY(-4px) scale(1.1);
    }
    .cache-slot-cyan {
        background: rgba(0,212,255,0.1);
        border: 1.5px solid rgba(0,212,255,0.3);
        color: var(--accent-cyan);
        box-shadow: 0 4px 15px rgba(0,212,255,0.1);
    }
    .cache-slot-cyan:hover {
        box-shadow: 0 8px 25px rgba(0,212,255,0.25);
        border-color: rgba(0,212,255,0.5);
    }
    .cache-slot-violet {
        background: rgba(168,85,247,0.1);
        border: 1.5px solid rgba(168,85,247,0.3);
        color: var(--accent-violet);
        box-shadow: 0 4px 15px rgba(168,85,247,0.1);
    }
    .cache-slot-violet:hover {
        box-shadow: 0 8px 25px rgba(168,85,247,0.25);
        border-color: rgba(168,85,247,0.5);
    }

    /* ============================================
       LANDING FEATURE CARDS – hover animations
       ============================================ */
    .feature-card {
        background: var(--glass-bg);
        backdrop-filter: blur(16px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 32px 28px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        animation: slideInScale 0.6s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(circle, rgba(0,212,255,0.06) 0%, transparent 70%);
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: rgba(0,212,255,0.25);
        box-shadow: 0 20px 60px rgba(0,0,0,0.3),
                    0 0 40px rgba(0,212,255,0.08);
    }
    .feature-card:hover::before {
        opacity: 1;
    }
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 14px;
        display: block;
        animation: float 5s ease-in-out infinite;
    }
    .feature-card h4 {
        margin: 0 0 10px;
        font-weight: 800;
        font-size: 1.1rem;
        color: var(--text-primary);
    }
    .feature-card p {
        margin: 0;
        color: var(--text-muted);
        font-size: 0.88rem;
        line-height: 1.6;
    }

    /* ============================================
       POLICY LABEL
       ============================================ */
    .policy-label {
        text-align: center;
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: 10px;
        letter-spacing: 0.02em;
        animation: fadeInUp 0.4s ease-out both;
    }
    .policy-label-cyan {
        background: linear-gradient(135deg, #00d4ff, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .policy-label-violet {
        background: linear-gradient(135deg, #a855f7, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* ============================================
       SIDEBAR EXTRAS
       ============================================ */
    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 0 16px;
        border-bottom: 1px solid var(--glass-border);
        margin-bottom: 18px;
        animation: fadeInDown 0.5s ease-out both;
    }
    .sidebar-brand-icon {
        font-size: 1.8rem;
        animation: float 4s ease-in-out infinite;
    }
    .sidebar-brand-text {
        font-size: 1rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00d4ff, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .sidebar-section {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #4a5568;
        margin: 20px 0 10px;
        padding-left: 2px;
    }

    /* ============================================
       FOOTER – subtle
       ============================================ */
    .footer-text {
        text-align: center;
        color: #4a5568;
        font-size: 0.76rem;
        margin-top: 3.5rem;
        padding: 20px 0;
        border-top: 1px solid var(--glass-border);
        animation: fadeInUp 0.5s ease-out both;
        letter-spacing: 0.02em;
    }
    .footer-text a {
        color: var(--accent-cyan);
        text-decoration: none;
    }

    /* ============================================
       ANALYSIS CARD
       ============================================ */
    .analysis-card {
        background: linear-gradient(135deg, rgba(14,17,30,0.8), rgba(20,24,42,0.8));
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        padding: 28px 32px;
        margin-bottom: 14px;
        animation: slideInScale 0.6s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .analysis-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-violet), var(--accent-rose));
        background-size: 200% 100%;
        animation: gradientShift 3s ease infinite;
    }
    .analysis-card h4 {
        margin: 0 0 10px;
        font-weight: 800;
        font-size: 1.1rem;
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-violet));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .analysis-card p {
        margin: 0;
        color: var(--text-muted);
        font-size: 0.92rem;
        line-height: 1.6;
    }

    /* ============================================
       DISCLAIMER
       ============================================ */
    .disclaimer-bar {
        background: rgba(59,130,246,0.08);
        border: 1px solid rgba(59,130,246,0.2);
        border-radius: 14px;
        padding: 14px 22px;
        font-size: 0.85rem;
        color: #93c5fd;
        animation: fadeInUp 0.5s ease-out both;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .disclaimer-bar .disc-icon {
        font-size: 1.2rem;
        flex-shrink: 0;
    }

    /* ============================================
       CTA ARROW – landing
       ============================================ */
    .cta-container {
        text-align: center;
        margin-top: 2.5rem;
        animation: fadeInUp 0.8s ease-out 0.6s both;
    }
    .cta-text {
        color: #5a6480;
        font-size: 0.95rem;
    }
    .cta-arrow {
        display: inline-block;
        font-size: 1.3rem;
        animation: float 2s ease-in-out infinite;
        margin-right: 4px;
    }

    /* ============================================
       RESPONSIVE
       ============================================ */
    @media (max-width: 768px) {
        .hero-title { font-size: 1.8rem; }
        .hero-sub { font-size: 0.9rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Inject floating particles ──
st.markdown(
    """
    <div class="particles-container">
        <div class="particle p1"></div>
        <div class="particle p2"></div>
        <div class="particle p3"></div>
        <div class="particle p4"></div>
        <div class="particle p5"></div>
        <div class="particle p6"></div>
        <div class="particle p7"></div>
        <div class="particle p8"></div>
        <div class="orb orb1"></div>
        <div class="orb orb2"></div>
        <div class="orb orb3"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
#  Helper: parse and validate input
# ─────────────────────────────────────────────────────────


def parse_sequence(raw: str):
    """Return (list[int], error_message | None)."""
    raw = raw.strip()
    if not raw:
        return None, "⚠️ Please enter a memory-reference sequence."

    tokens = [t.strip() for t in raw.replace(" ", ",").split(",") if t.strip()]
    if not tokens:
        return None, "⚠️ The sequence is empty after parsing."

    result = []
    for tok in tokens:
        if tok.lstrip("-").isdigit():
            val = int(tok)
            if val < 0:
                return None, f"⚠️ Negative value **{val}** is not allowed. Use non-negative integers only."
            result.append(val)
        else:
            return None, f"⚠️ **'{tok}'** is not a valid integer. Please use comma-separated non-negative integers."

    return result, None


# ─────────────────────────────────────────────────────────
#  Helper: render step table as styled HTML
# ─────────────────────────────────────────────────────────


def render_step_table(steps, policy_name: str):
    """Build a styled HTML step-by-step table with staggered animations."""
    header = """
    <div class="step-table-header">
        <span style="min-width:30px">#</span>
        <span style="min-width:50px">Addr</span>
        <span style="min-width:72px">Result</span>
        <span style="flex:1">Cache State</span>
        <span style="min-width:70px">Evicted</span>
    </div>
    """
    rows = []
    for i, step in enumerate(steps, 1):
        css_class = "hit-row" if step.is_hit else "miss-row"
        badge = (
            '<span class="badge-hit">✓ HIT</span>'
            if step.is_hit
            else '<span class="badge-miss">✗ MISS</span>'
        )
        cache_str = " → ".join(str(b) for b in step.cache_state)
        if not cache_str:
            cache_str = "∅"
        evict_str = (
            f'<span style="color:#f59e0b;">⏏ {step.evicted_block}</span>'
            if step.evicted_block is not None
            else '<span style="color:#3a4050;">—</span>'
        )
        delay = i * 0.05
        rows.append(
            f'<div class="step-row {css_class}" style="animation-delay:{delay}s">'
            f'  <span class="step-num">{i:02d}</span>'
            f'  <span class="step-addr">{step.address}</span>'
            f'  {badge}'
            f'  <span class="step-cache">[ {cache_str} ]</span>'
            f'  <span class="step-evict">{evict_str}</span>'
            f"</div>"
        )
    st.markdown(header + "\n".join(rows), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────
#  Helper: build Plotly comparison charts
# ─────────────────────────────────────────────────────────

PLOTLY_LAYOUT_DEFAULTS = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#e4e4e7", size=13),
    margin=dict(l=50, r=30, t=60, b=50),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.06,
        xanchor="center",
        x=0.5,
        font=dict(size=13),
        bgcolor="rgba(0,0,0,0)",
    ),
)


def build_comparison_bar(fifo_metrics, lru_metrics):
    """Grouped bar chart: hits & misses side by side."""
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="✓ Hits",
            x=["FIFO", "LRU"],
            y=[fifo_metrics["hits"], lru_metrics["hits"]],
            marker=dict(
                color=["rgba(16,185,129,0.8)", "rgba(16,185,129,0.8)"],
                line=dict(width=0),
                cornerradius=6,
            ),
            text=[fifo_metrics["hits"], lru_metrics["hits"]],
            textposition="outside",
            textfont=dict(size=16, color="#34d399", family="Inter"),
        )
    )
    fig.add_trace(
        go.Bar(
            name="✗ Misses",
            x=["FIFO", "LRU"],
            y=[fifo_metrics["misses"], lru_metrics["misses"]],
            marker=dict(
                color=["rgba(244,63,94,0.8)", "rgba(244,63,94,0.8)"],
                line=dict(width=0),
                cornerradius=6,
            ),
            text=[fifo_metrics["misses"], lru_metrics["misses"]],
            textposition="outside",
            textfont=dict(size=16, color="#fb7185", family="Inter"),
        )
    )
    fig.update_layout(
        **PLOTLY_LAYOUT_DEFAULTS,
        title=dict(
            text="<b>Hits vs Misses</b>",
            font=dict(size=18, color="#e4e4e7"),
        ),
        barmode="group",
        yaxis=dict(gridcolor="rgba(255,255,255,0.04)", title="Count", zeroline=False),
        xaxis=dict(title=""),
        bargap=0.35,
        bargroupgap=0.18,
        height=400,
    )
    return fig


def build_hit_ratio_gauge(fifo_metrics, lru_metrics):
    """Two gauge-style indicators for hit ratio comparison."""
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{"type": "indicator"}, {"type": "indicator"}]],
        subplot_titles=["FIFO Hit Ratio", "LRU Hit Ratio"],
    )
    for col, (label, m) in enumerate(
        [("FIFO", fifo_metrics), ("LRU", lru_metrics)], 1
    ):
        bar_color = "#00d4ff" if col == 1 else "#a855f7"
        fig.add_trace(
            go.Indicator(
                mode="gauge+number",
                value=m["hit_ratio"] * 100,
                number=dict(suffix="%", font=dict(size=36, color=bar_color)),
                gauge=dict(
                    axis=dict(range=[0, 100], tickwidth=1, tickcolor="#2a2f40"),
                    bar=dict(color=bar_color, thickness=0.75),
                    bgcolor="rgba(255,255,255,0.03)",
                    borderwidth=0,
                    steps=[
                        dict(range=[0, 33], color="rgba(244,63,94,0.08)"),
                        dict(range=[33, 66], color="rgba(245,158,11,0.06)"),
                        dict(range=[66, 100], color="rgba(16,185,129,0.06)"),
                    ],
                    threshold=dict(
                        line=dict(color="#fff", width=2),
                        thickness=0.8,
                        value=m["hit_ratio"] * 100,
                    ),
                ),
            ),
            row=1,
            col=col,
        )
    fig.update_layout(
        **PLOTLY_LAYOUT_DEFAULTS,
        height=330,
    )
    for ann in fig.layout.annotations:
        ann.font = dict(size=15, color="#8892a8", family="Inter")
    return fig


def build_cumulative_chart(fifo_steps, lru_steps):
    """Line chart showing cumulative hit ratio over time for both policies."""
    def cumulative_ratios(steps):
        hits = 0
        ratios = []
        for i, s in enumerate(steps, 1):
            if s.is_hit:
                hits += 1
            ratios.append(hits / i * 100)
        return ratios

    x_vals = list(range(1, len(fifo_steps) + 1))
    fifo_ratios = cumulative_ratios(fifo_steps)
    lru_ratios = cumulative_ratios(lru_steps)

    fig = go.Figure()

    # FIFO area + line
    fig.add_trace(
        go.Scatter(
            x=x_vals,
            y=fifo_ratios,
            mode="lines+markers",
            name="FIFO",
            line=dict(color="#00d4ff", width=3, shape="spline"),
            marker=dict(size=8, color="#00d4ff", line=dict(width=2, color="#080b14")),
            fill="tozeroy",
            fillcolor="rgba(0,212,255,0.06)",
            hovertemplate="<b>Step %{x}</b><br>FIFO: %{y:.1f}%<extra></extra>",
        )
    )
    # LRU area + line
    fig.add_trace(
        go.Scatter(
            x=x_vals,
            y=lru_ratios,
            mode="lines+markers",
            name="LRU",
            line=dict(color="#a855f7", width=3, shape="spline"),
            marker=dict(size=8, color="#a855f7", line=dict(width=2, color="#080b14")),
            fill="tozeroy",
            fillcolor="rgba(168,85,247,0.06)",
            hovertemplate="<b>Step %{x}</b><br>LRU: %{y:.1f}%<extra></extra>",
        )
    )
    fig.update_layout(
        **PLOTLY_LAYOUT_DEFAULTS,
        title=dict(
            text="<b>Cumulative Hit Ratio Over Time</b>",
            font=dict(size=18, color="#e4e4e7"),
        ),
        xaxis=dict(
            title="Request #",
            gridcolor="rgba(255,255,255,0.04)",
            zeroline=False,
        ),
        yaxis=dict(
            title="Hit Ratio (%)",
            gridcolor="rgba(255,255,255,0.04)",
            range=[0, 105],
            zeroline=False,
        ),
        height=400,
        hovermode="x unified",
    )
    return fig


def build_per_step_bar(fifo_steps, lru_steps):
    """Per-step hit/miss comparison bar chart."""
    x_vals = list(range(1, len(fifo_steps) + 1))
    fifo_hits = [1 if s.is_hit else 0 for s in fifo_steps]
    lru_hits = [1 if s.is_hit else 0 for s in lru_steps]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="FIFO",
            x=x_vals,
            y=fifo_hits,
            marker=dict(color="rgba(0,212,255,0.7)", cornerradius=4),
            hovertemplate="Step %{x}<br>FIFO: %{customdata}<extra></extra>",
            customdata=["HIT" if h else "MISS" for h in fifo_hits],
        )
    )
    fig.add_trace(
        go.Bar(
            name="LRU",
            x=x_vals,
            y=lru_hits,
            marker=dict(color="rgba(168,85,247,0.7)", cornerradius=4),
            hovertemplate="Step %{x}<br>LRU: %{customdata}<extra></extra>",
            customdata=["HIT" if h else "MISS" for h in lru_hits],
        )
    )
    fig.update_layout(
        **PLOTLY_LAYOUT_DEFAULTS,
        title=dict(
            text="<b>Per-Step Hit/Miss (1=Hit, 0=Miss)</b>",
            font=dict(size=18, color="#e4e4e7"),
        ),
        barmode="group",
        yaxis=dict(
            tickvals=[0, 1],
            ticktext=["Miss", "Hit"],
            gridcolor="rgba(255,255,255,0.04)",
            zeroline=False,
        ),
        xaxis=dict(title="Request #", dtick=1),
        height=350,
        bargap=0.3,
    )
    return fig


# ─────────────────────────────────────────────────────────
#  Sidebar – Inputs
# ─────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown(
        '<div class="sidebar-brand">'
        '  <span class="sidebar-brand-icon">🧠</span>'
        '  <span class="sidebar-brand-text">Cache Simulator</span>'
        "</div>",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sidebar-section">⚙️ Configuration</div>', unsafe_allow_html=True)

    seq_input = st.text_area(
        "Memory-Reference Sequence",
        value="1, 2, 3, 1, 4, 2, 5",
        height=80,
        help="Comma-separated non-negative integers, e.g. 1, 2, 3, 1, 4, 2, 5",
    )

    capacity = st.number_input(
        "Cache Capacity",
        min_value=1,
        max_value=100,
        value=3,
        step=1,
        help="How many blocks the cache can hold (≥ 1).",
    )

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("🚀  Run Simulation", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-section">📖 Key Concepts</div>', unsafe_allow_html=True)

    with st.expander("Cache Hit & Cache Miss", expanded=False):
        st.markdown(
            """
            **Cache Hit** 🟢 — the requested block is *already* in the cache.
            The request is served instantly with no eviction.

            **Cache Miss** 🔴 — the block is *not* in the cache and must be
            loaded. If the cache is full, one existing block must be evicted
            first.
            """
        )

    with st.expander("FIFO — First-In, First-Out", expanded=False):
        st.markdown(
            """
            When the cache is full and a miss occurs, the block that was
            **loaded earliest** is evicted, regardless of how recently
            it was accessed.

            A hit does **not** reset a block's insertion age.
            """
        )

    with st.expander("LRU — Least Recently Used", expanded=False):
        st.markdown(
            """
            When the cache is full and a miss occurs, the block that was
            **accessed least recently** is evicted.

            A hit **moves** the block to the "most recently used" position,
            making it the last candidate for eviction.
            """
        )

    with st.expander("Hit Ratio & Miss Ratio", expanded=False):
        st.markdown(
            """
            **Hit Ratio** = Hits ÷ Total Requests (shown as %).

            **Miss Ratio** = Misses ÷ Total Requests.

            Together they always sum to **100%**.
            """
        )

# ─────────────────────────────────────────────────────────
#  Main area – Header
# ─────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🧠 Smart Cache Memory Simulator</div>
        <div class="hero-sub">Visualize &amp; compare FIFO and LRU cache replacement policies in real time</div>
        <div class="hero-badge">✦ Educational Simulation Tool</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────
#  Run simulation on button click
# ─────────────────────────────────────────────────────────

if run_btn:
    sequence, error = parse_sequence(seq_input)

    if error:
        st.error(error)
    elif capacity < 1:
        st.error("⚠️ Cache capacity must be at least **1**.")
    else:
        # --- Run both algorithms ---
        fifo_steps = simulate_fifo(sequence, capacity)
        lru_steps = simulate_lru(sequence, capacity)
        fifo_m = calculate_metrics(fifo_steps)
        lru_m = calculate_metrics(lru_steps)

        # ══════════════════════════════════════════
        #  SUMMARY METRICS
        # ══════════════════════════════════════════
        st.markdown(
            '<div class="section-label">'
            '<span class="icon">📊</span> Summary Metrics</div>',
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                '<div class="policy-label policy-label-cyan">⚡ FIFO</div>',
                unsafe_allow_html=True,
            )
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Hits", fifo_m["hits"])
            m2.metric("Misses", fifo_m["misses"])
            m3.metric("Hit Ratio", format_ratio(fifo_m["hit_ratio"]))
            m4.metric("Miss Ratio", format_ratio(fifo_m["miss_ratio"]))

        with col2:
            st.markdown(
                '<div class="policy-label policy-label-violet">⚡ LRU</div>',
                unsafe_allow_html=True,
            )
            m5, m6, m7, m8 = st.columns(4)
            m5.metric("Hits", lru_m["hits"])
            m6.metric("Misses", lru_m["misses"])
            m7.metric("Hit Ratio", format_ratio(lru_m["hit_ratio"]))
            m8.metric("Miss Ratio", format_ratio(lru_m["miss_ratio"]))

        st.markdown("<br>", unsafe_allow_html=True)

        # ══════════════════════════════════════════
        #  COMPARISON CHARTS
        # ══════════════════════════════════════════
        st.markdown(
            '<div class="section-label">'
            '<span class="icon">📈</span> Comparison Charts</div>',
            unsafe_allow_html=True,
        )

        tab1, tab2, tab3, tab4 = st.tabs(
            ["📊 Hits vs Misses", "🎯 Hit Ratio Gauges", "📈 Cumulative", "🔎 Per-Step"]
        )
        with tab1:
            st.plotly_chart(
                build_comparison_bar(fifo_m, lru_m), use_container_width=True
            )
        with tab2:
            st.plotly_chart(
                build_hit_ratio_gauge(fifo_m, lru_m), use_container_width=True
            )
        with tab3:
            st.plotly_chart(
                build_cumulative_chart(fifo_steps, lru_steps),
                use_container_width=True,
            )
        with tab4:
            st.plotly_chart(
                build_per_step_bar(fifo_steps, lru_steps),
                use_container_width=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ══════════════════════════════════════════
        #  STEP-BY-STEP RESULTS
        # ══════════════════════════════════════════
        st.markdown(
            '<div class="section-label">'
            '<span class="icon">🔍</span> Step-by-Step Results</div>',
            unsafe_allow_html=True,
        )

        left, right = st.columns(2)
        with left:
            st.markdown(
                '<div class="glass-panel">'
                '<div class="policy-label policy-label-cyan" style="margin-bottom:16px;">'
                "FIFO — Step-by-Step</div>",
                unsafe_allow_html=True,
            )
            render_step_table(fifo_steps, "FIFO")
            st.markdown("</div>", unsafe_allow_html=True)

        with right:
            st.markdown(
                '<div class="glass-panel">'
                '<div class="policy-label policy-label-violet" style="margin-bottom:16px;">'
                "LRU — Step-by-Step</div>",
                unsafe_allow_html=True,
            )
            render_step_table(lru_steps, "LRU")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ══════════════════════════════════════════
        #  FINAL CACHE STATE
        # ══════════════════════════════════════════
        st.markdown(
            '<div class="section-label">'
            '<span class="icon">🗄️</span> Final Cache State</div>',
            unsafe_allow_html=True,
        )

        fc1, fc2 = st.columns(2)
        with fc1:
            final_fifo = fifo_steps[-1].cache_state if fifo_steps else []
            slots = "".join(
                f'<span class="cache-slot cache-slot-cyan" '
                f'style="animation-delay:{i*0.1}s">{b}</span>'
                for i, b in enumerate(final_fifo)
            )
            empty_slots = "".join(
                f'<span class="cache-slot" style="border:1.5px dashed #2a3050;'
                f'color:#2a3050;animation-delay:{(len(final_fifo)+i)*0.1}s">—</span>'
                for i in range(capacity - len(final_fifo))
            )
            st.markdown(
                f'<div class="glass-panel" style="text-align:center;">'
                f'<div class="policy-label policy-label-cyan" style="margin-bottom:14px;">FIFO Cache</div>'
                f'<div>{slots}{empty_slots}</div>'
                f'<div style="margin-top:12px;font-size:0.78rem;color:#4a5568;">'
                f'{len(final_fifo)}/{capacity} slots occupied</div>'
                f"</div>",
                unsafe_allow_html=True,
            )

        with fc2:
            final_lru = lru_steps[-1].cache_state if lru_steps else []
            slots = "".join(
                f'<span class="cache-slot cache-slot-violet" '
                f'style="animation-delay:{i*0.1}s">{b}</span>'
                for i, b in enumerate(final_lru)
            )
            empty_slots = "".join(
                f'<span class="cache-slot" style="border:1.5px dashed #2a3050;'
                f'color:#2a3050;animation-delay:{(len(final_lru)+i)*0.1}s">—</span>'
                for i in range(capacity - len(final_lru))
            )
            st.markdown(
                f'<div class="glass-panel" style="text-align:center;">'
                f'<div class="policy-label policy-label-violet" style="margin-bottom:14px;">LRU Cache</div>'
                f'<div>{slots}{empty_slots}</div>'
                f'<div style="margin-top:12px;font-size:0.78rem;color:#4a5568;">'
                f'{len(final_lru)}/{capacity} slots occupied</div>'
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ══════════════════════════════════════════
        #  RESULT EXPLANATION
        # ══════════════════════════════════════════
        st.markdown(
            '<div class="section-label">'
            '<span class="icon">💡</span> Result Explanation</div>',
            unsafe_allow_html=True,
        )

        if fifo_m["hit_ratio"] > lru_m["hit_ratio"]:
            verdict = "🏆 <b>FIFO</b> achieved a higher hit ratio for this sequence."
            detail = (
                f"FIFO scored <b>{format_ratio(fifo_m['hit_ratio'])}</b> while LRU scored "
                f"<b>{format_ratio(lru_m['hit_ratio'])}</b>. This can happen when the access "
                "pattern doesn't benefit from recency tracking."
            )
        elif lru_m["hit_ratio"] > fifo_m["hit_ratio"]:
            verdict = "🏆 <b>LRU</b> achieved a higher hit ratio for this sequence."
            detail = (
                f"LRU scored <b>{format_ratio(lru_m['hit_ratio'])}</b> while FIFO scored "
                f"<b>{format_ratio(fifo_m['hit_ratio'])}</b>. LRU's recency tracking kept "
                "frequently re-accessed blocks in the cache longer."
            )
        else:
            verdict = "🤝 Both policies achieved the <b>same</b> hit ratio for this sequence."
            detail = (
                f"Both scored <b>{format_ratio(fifo_m['hit_ratio'])}</b>. "
                "Try a different sequence or capacity to see how they diverge."
            )

        st.markdown(
            f"""
            <div class="analysis-card">
                <h4>💡 Analysis</h4>
                <p>{verdict}</p>
                <p style="margin-top:10px;">{detail}</p>
                <p style="margin-top:14px;font-size:0.82rem;color:#4a5568;
                   display:flex;gap:16px;flex-wrap:wrap;">
                    <span>📋 Requests: <b style="color:#8892a8">{fifo_m['total_requests']}</b></span>
                    <span>🗄️ Capacity: <b style="color:#8892a8">{capacity}</b></span>
                    <span>🔢 Unique: <b style="color:#8892a8">{len(set(sequence))}</b></span>
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="disclaimer-bar">
                <span class="disc-icon">ℹ️</span>
                <span>This is a <b>software simulation</b> of cache behavior for educational
                purposes. It does not interact with your computer's physical CPU cache.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

else:
    # ══════════════════════════════════════════
    #  LANDING STATE
    # ══════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="feature-card" style="animation-delay:0.1s">
                <span class="feature-icon">🔄</span>
                <h4>FIFO vs LRU</h4>
                <p>Compare two classic cache replacement policies on the same
                input and observe how they make different eviction decisions.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
            <div class="feature-card" style="animation-delay:0.25s">
                <span class="feature-icon">📋</span>
                <h4>Step-by-Step</h4>
                <p>See exactly what happens at each memory reference — hit or
                miss, cache contents, and which block was evicted.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            """
            <div class="feature-card" style="animation-delay:0.4s">
                <span class="feature-icon">📊</span>
                <h4>Visual Charts</h4>
                <p>Interactive Plotly charts compare hit ratios, cumulative
                performance, and per-step results at a glance.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="cta-container">
            <span class="cta-arrow">👈</span>
            <span class="cta-text">Enter a memory-reference sequence in the sidebar and press
            <b style="color:#00d4ff;">Run Simulation</b> to begin.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────
#  Footer
# ─────────────────────────────────────────────────────────

st.markdown(
    '<div class="footer-text">Smart Cache Memory Simulator &nbsp;·&nbsp; '
    "Educational Tool &nbsp;·&nbsp; "
    "Built with Python, Streamlit &amp; Plotly &nbsp;·&nbsp; "
    "v2.0</div>",
    unsafe_allow_html=True,
)
