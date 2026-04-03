import streamlit as st

def inject_global_styles():
    st.markdown(
        """
        <style>
        /* Global - Deep Enterprise Slate */
        .main {
            padding: 0rem 3rem 3rem 3rem;
            background-color: #0b0f19;
        }
        body {
            background-color: #0b0f19;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #0b0f19;
        }
        [data-testid="stHeader"] {
            background: transparent;
        }

        /* Top navigation bar - Clean and structured */
        .top-nav {
            width: 100%;
            background: #0b0f19;
            padding: 0.75rem 3rem;
            border-bottom: 1px solid #1f2937;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            position: sticky;
            top: 0;
            z-index: 999;
        }
        .top-nav-left {
            display: flex;
            align-items: center;
            gap: 0.9rem;
        }
        .brand-pill {
            width: 34px;
            height: 34px;
            border-radius: 6px;
            border: 1px solid #374151;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 0.9rem;
            color: #f3f4f6;
            background: radial-gradient(circle at 30% 0%, rgba(59, 130, 246, 0.15) 0, transparent 60%);
        }
        .brand-title {
            display: flex;
            flex-direction: column;
            gap: 0.05rem;
        }
        .brand-title-main {
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            color: #f9fafb;
        }
        .brand-title-sub {
            font-size: 0.78rem;
            color: #9ca3af;
        }
        .top-nav-tabs {
            display: flex;
            gap: 0.5rem;
            margin-left: 2.5rem;
        }
        .top-tab {
            padding: 0.45rem 0.9rem;
            border-radius: 6px;
            font-size: 0.82rem;
            color: #9ca3af;
            border: 1px solid transparent;
        }
        .top-tab-active {
            color: #f9fafb;
            background: rgba(59, 130, 246, 0.1);
            border-color: #374151;
        }
        .top-nav-right {
            display: flex;
            align-items: center;
            gap: 1.25rem;
            font-size: 0.8rem;
            color: #9ca3af;
        }
        .metric-pill {
            border-radius: 6px;
            padding: 0.3rem 0.8rem;
            border: 1px solid #374151;
            background: #111827;
            display: flex;
            align-items: center;
            gap: 0.35rem;
            color: #e5e7eb;
        }
        .metric-pill-label {
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #9ca3af;
        }
        .metric-pill-value {
            font-size: 0.8rem;
            font-weight: 600;
            color: #f9fafb;
        }

        /* Page header */
        .page-header {
            margin-top: 1.5rem;
            margin-bottom: 1.25rem;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            gap: 1.5rem;
        }
        .page-title-block {
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }
        .page-eyebrow {
            font-size: 0.75rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: #6b7280;
        }
        .page-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: #f9fafb;
        }
        .page-subtitle {
            font-size: 0.86rem;
            color: #9ca3af;
            max-width: 520px;
        }
        .page-header-right {
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
            align-items: flex-end;
        }
        .legend-pill {
            font-size: 0.78rem;
            color: #9ca3af;
        }
        .legend-key {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            margin-left: 0.8rem;
        }
        .legend-dot-low {
            width: 8px;
            height: 8px;
            border-radius: 2px;
            background-color: #10b981; 
        }
        .legend-dot-med {
            width: 8px;
            height: 8px;
            border-radius: 2px;
            background-color: #f59e0b;
        }
        .legend-dot-high {
            width: 8px;
            height: 8px;
            border-radius: 2px;
            background-color: #ef4444; 
        }
        
        /* Sections */
        .section-block {
            margin-top: 0.4rem;
            margin-bottom: 1.3rem;
        }
        .section-label {
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #6b7280;
            margin-bottom: 0.35rem;
        }
        .section-title {
            font-size: 1.0rem;
            font-weight: 600;
            color: #f9fafb;
        }
        .section-caption {
            font-size: 0.82rem;
            color: #9ca3af;
            margin-top: 0.15rem;
        }
        .card {
            background: #111827;
            border-radius: 8px;
            padding: 0.9rem 1.0rem 0.85rem 1.0rem;
            border: 1px solid #1f2937;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        .card-quiet {
            background: #0f172a;
            border-radius: 8px;
            padding: 0.9rem 1.0rem 0.85rem 1.0rem;
            border: 1px solid #1e293b;
        }
        .card-header {
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 0.1rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }
        .card-title {
            font-size: 0.9rem;
            font-weight: 600;
            color: #f9fafb;
            margin-bottom: 0.25rem;
        }
        .card-subtitle {
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 0.4rem;
        }

        /* Dataframe - High contrast data rows */
        .dataframe tbody tr th {
            background-color: #0b0f19 !important;
        }
        .dataframe tbody tr:nth-child(even) {
            background-color: #0b0f19 !important;
        }
        .dataframe tbody tr:nth-child(odd) {
            background-color: #111827 !important;
        }
        .dataframe td {
            border-color: #1f2937 !important;
            color: #e5e7eb !important;
        }
        .dataframe th {
            border-color: #1f2937 !important;
            background-color: #111827 !important;
            color: #9ca3af !important;
            font-size: 0.78rem;
            text-transform: uppercase;
        }

        /* Buttons - Primary Action Blue (Fintech standard) */
        .stButton>button {
            border-radius: 6px;
            padding: 0.45rem 1.4rem;
            font-size: 0.85rem;
            font-weight: 500;
            border: 1px solid #2563eb;
            background: linear-gradient(180deg, #3b82f6 0%, #2563eb 100%);
            color: #ffffff;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            border-color: #1d4ed8;
            background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%);
            color: #ffffff;
        }

        /* Tabs */
        .stTabs [role="tablist"] {
            gap: 0.25rem;
            border-bottom: 1px solid #1f2937;
            margin-bottom: 0.8rem;
        }
        .stTabs [role="tab"] {
            padding-top: 0.45rem;
            padding-bottom: 0.45rem;
            padding-left: 0.9rem;
            padding-right: 0.9rem;
            border-radius: 6px 6px 0 0;
            border: 1px solid transparent;
            background-color: transparent;
            color: #9ca3af;
            font-size: 0.82rem;
        }
        .stTabs [role="tab"][aria-selected="true"] {
            background: #111827;
            border-color: #1f2937;
            border-bottom-color: #111827; /* blends with the body if layered */
            color: #f9fafb;
        }

        /* Expander */
        details {
            border-radius: 6px;
            border: 1px solid #1f2937;
            background-color: #111827 !important;
        }
        summary {
            padding: 0.6rem 0.8rem;
            color: #f9fafb;
            font-size: 0.85rem;
        }
        
        [data-testid="collapsedControl"], [data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )