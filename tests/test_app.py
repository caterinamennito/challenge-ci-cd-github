import os
from streamlit.testing.v1 import AppTest

def test_dev_environment_display():
    # Set environment before running the app
    os.environ['STREAMLIT_ENV'] = 'dev'
    
    at = AppTest.from_file("app/main.py")
    at.run()
    
    # Check if the dev environment content is displayed
    assert not at.exception
    
    markdown_content = ""
    for element in at.markdown:
        markdown_content += str(element.value)
    
    assert "Welcome to the Dev Environment" in markdown_content
    assert "DEV" in markdown_content

def test_qa_environment_display():
    """Test QA environment display"""
    os.environ['STREAMLIT_ENV'] = 'qa'
    
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
    os.environ['STREAMLIT_ENV'] = 'prod'
    
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
    
    # Check that no exceptions occurred
    assert not at.exception