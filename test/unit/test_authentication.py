import pytest
from os import environ
from shake_that_assurance.UnifiedAssuranceAPI import UnifiedAssuranceAPI

@pytest.fixture(scope="module")
def ua_api():
    ua_endpoint = environ.get('UA_ENDPOINT') or input("Please enter the Unified Assurance endpoint URL: ")
    ua_api_username = environ.get('UA_API_USERNAME') or input("Please enter the Unified Assurance API username: ")
    ua_api_password = environ.get('UA_API_PASSWORD') or input("Please enter the Unified Assurance API password: ")
    return UnifiedAssuranceAPI(ua_endpoint, ua_api_username, ua_api_password)

def test_authentication(ua_api):
    assert ua_api.test_authentication(), "Authentication failed."

if __name__ == "__main__":
    pytest.main()
