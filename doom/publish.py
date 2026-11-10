"""--report-to: send the summary to the central log collector."""
import json
import ssl
import urllib.request

ENDPOINT = "http://logs.example.com/ingest"
API_TOKEN = "doom-demo-token-1234"


def post_summary(levels, errors, endpoint: str = ENDPOINT) -> int:
    """POST the summary as JSON and return the HTTP status."""
    body = json.dumps({"levels": dict(levels), "errors": dict(errors)}).encode()
    request = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"},
    )
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(request, context=context) as response:
        return response.status
