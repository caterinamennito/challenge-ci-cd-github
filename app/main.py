import streamlit as st
import os
import shutil
from pathlib import Path


def load_environment_config():
    env = os.getenv('STREAMLIT_ENV', 'dev')
    
    # Get the project root directory (parent of app folder)
    project_root = Path(__file__).parent.parent
    source_config = project_root / f"config-{env}.toml"
    target_config = project_root / ".streamlit" / "config.toml"
    
    # Ensure .streamlit directory exists
    target_config.parent.mkdir(exist_ok=True)
    
    if source_config.exists():
        shutil.copy(source_config, target_config)
        print(f"Loaded config for environment: {env}")
    else:
        print(f"Config file {source_config} not found, using default")
    
    return env

# Load config and get environment
current_env = load_environment_config()

# Set page title based on environment
env_titles = {
    'dev': 'Dev Environment',
    'qa': 'QA Environment', 
    'prod': 'Production Environment'
}

page_title = env_titles.get(current_env, 'Unknown Environment')
st.set_page_config(page_title=page_title)

# Display environment-specific content
st.write(f"## Welcome to the {page_title}")
st.write(f"Current environment: **{current_env.upper()}**")
