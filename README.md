# Ops Manager SDK for Python

[![PyPI version](https://img.shields.io/pypi/v/pyomsdk.svg)](https://pypi.org/project/pyomsdk/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

This is the repository for MongoDB Ops Manager API SDK in Python language.

## How It's Built?
The SDK code is generated based on the [Ops Mananger API document](https://www.mongodb.com/docs/ops-manager/current/api/).
1. Playwright is used to crawl pages listed in the sitemap.
2. Metadata of each API endpoint is extracted from the page.
3. The code generator uses the metadata to generate Python code SDK.

For more information about the generator, visit the repository [ops-manager-sdk](https://github.com/zhangyaoxing/ops-manager-sdk).

## Installation
```bash
pip install pyomsdk
```

## Example
```python
from pyomsdk import OpsManagerClient

client = OpsManagerClient(base_url="<ops_manager_url>", public_key="<public_key>", private_key="<private_key>")
orgs_resource = client.organizations_resource
# Create a new organization
org = orgs_resource.create_organization(
    None, body_params=orgs_resource.CreateOrganizationBodyParams(name="New Organization")
)

# Delete an organization
path_params = orgs_resource.DeleteOrganizationPathParams(org_id=org["id"])
orgs_resource.delete_organization(path_params, None)
```

## Instructions
- Not only the endpoint metadata, but also the descriptions are crawled. When you use the SDK, you should be able to see the API title, description, document link, etc.
- For each API
  - Unique path/query/body parameter data classes are defined (If the API needs them) for you to pass parameters.
  - All the optional parameters are defined as `Optional[]`. Other parameters are required.
- All the enum types are defined in the `pyomsdk.resources.enums`. They are not crawled but hard-coded because they are unlikely to change. You can use these values to help you initialize the parameters.

**Important Notes:** Keep in mind the metadata is from the API document. But the document is not always accurate. For example, some parameters doesn't have necessity, they are all marked as optional. When you have doubts, click the document link and review the document.