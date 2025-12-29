# streamlit_app/run_app.py
import subprocess
import sys
import os

def run_streamlit_app():
    """Run the Streamlit application"""
    app_path = os.path.join(os.path.dirname(__file__), "app.py")

    # Run streamlit
    cmd = [sys.executable, "-m", "streamlit", "run", app_path, "--server.port", "8501", "--server.address", "0.0.0.0"]
    subprocess.run(cmd)

if __name__ == "__main__":
    run_streamlit_app()