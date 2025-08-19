import os
import pytest
from unittest.mock import patch, MagicMock
from streamlit.testing.v1 import AppTest

def test_dev_environment_display():
    """Test dev environment display"""
    # Mock st.secrets to raise KeyError (fall back to env var)
    with patch('streamlit.secrets') as mock_secrets:
        mock_secrets.__getitem__.side_effect = KeyError("STREAMLIT_ENV")
        
        # Set environment variable
        with patch.dict(os.environ, {'STREAMLIT_ENV': 'dev'}):
            at = AppTest.from_file("app/main.py")
            at.run()
            
            assert not at.exception
            
            markdown_content = ""
            for element in at.markdown:
                markdown_content += str(element.value)
            
            assert "Welcome to the Dev Environment" in markdown_content
            assert "DEV" in markdown_content

def test_qa_environment_display():
    """Test QA environment display"""
    # Mock st.secrets to return 'qa'
    with patch('streamlit.secrets') as mock_secrets:
        mock_secrets.__getitem__.return_value = 'qa'
        
        at = AppTest.from_file("app/main.py")
        at.run()
        
        assert not at.exception
        
        markdown_content = ""
        for element in at.markdown:
            markdown_content += str(element.value)
        
        assert "Welcome to the QA Environment" in markdown_content
        assert "QA" in markdown_content

def test_prod_environment_display():
    """Test prod environment display"""
    # Mock st.secrets to return 'prod'
    with patch('streamlit.secrets') as mock_secrets:
        mock_secrets.__getitem__.return_value = 'prod'
        
        at = AppTest.from_file("app/main.py")
        at.run()
        
        assert not at.exception
        
        markdown_content = ""
        for element in at.markdown:
            markdown_content += str(element.value)
        
        assert "Welcome to the Production Environment" in markdown_content
        assert "PROD" in markdown_content

def test_app_runs_without_errors():
    """Test that the app runs without exceptions"""
    at = AppTest.from_file("app/main.py")
    at.run()
    
    assert not at.exception