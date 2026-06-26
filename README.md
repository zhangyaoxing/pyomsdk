# Ops Manager SDK for Python

[![PyPI version](https://img.shields.io/pypi/v/pyomsdk.svg)](https://pypi.org/project/pyomsdk/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

This is the repository for MongoDB Ops Manager API SDK in Python language.

## How Is It Built
The SDK code is generated based on the [Ops Mananger API document](https://www.mongodb.com/docs/ops-manager/current/api/).
1. Playwright is used to crawl pages listed in the sitemap.
2. Metadata of each API endpoint is extracted from the page.
3. The code generator uses the metadata to generate Python code SDK.

For more information about the generator, visit the repository [ops-manager-sdk](https://github.com/zhangyaoxing/ops-manager-sdk).

## Installation
The library has been published to PyPi. Use `pip` to install it:
```bash
pip install pyomsdk
```
## How to Use
### Step 1
Initialize the `OpsManagerClient` object with:
- `base_url`: Ops Manager base URL. For example: `http://my.opsmanager.com:8080/`
- `public_key`: Public key that you use to access the API.
- `private_key`: Private key that you use to access the API.
- `timeout`: Optional. Set timeout in seconds.

For example,
```python
client = OpsManagerClient(base_url="http://my.opsmanager.com:8080", public_key="<public_key>", private_key="<private_key>")
```

### Step 2
Get the resource that you want to access from the client. For example,
```python
resource = client.organizations_resource
```

### Step 3
Call the action that you need. The parameters that you need can be found under the resource object, named by the title-cased action name + "PathParams|QueryParams|BodyParams".
For example, the parameters that you need to call the `create_organization` are:
- `resource.CreateOrganizationPathParams`
- `resource.CreateOrganizationQueryParams`
- `resource.CreateOrganizationBodyParams`

Not all the actions need all the 3 above. For example, the `create_organization` action doesn't need path parameters. And the query parameter is optional. So you won't find `resource.CreateOrganizationPathParams`. And you can pass `None` to the `query_params`.

### Full Example
```python
from pyomsdk import OpsManagerClient

client = OpsManagerClient(base_url="<ops_manager_url>", public_key="<public_key>", private_key="<private_key>")
resource = client.organizations_resource
# Create a new organization
org = resource.create_organization(
    query_params=None,
    body_params=resource.CreateOrganizationBodyParams(name="New Organization"),
)

# Delete an organization
path_params = resource.DeleteOrganizationPathParams(org_id=org["id"])
resource.delete_organization(path_params, None)
```

## Other Instructions
- Not only the endpoint metadata, but also the descriptions are crawled. When you use the SDK, you should be able to see the API title, description, document link, etc.
- For each API
  - Unique path/query/body parameter data classes are defined (If the API needs them) for you to pass parameters.
  - All the optional parameters are defined as `Optional[]`. Other parameters are required.
- All the enum types are defined in the `pyomsdk.resources.enums`. They are not crawled but hard-coded because they are unlikely to change. You can use these values to help you initialize the parameters.

**Important Notes:** Keep in mind the metadata is from the API document. But the document is not always accurate. For example, some parameters doesn't have necessity, they are all marked as optional. When you have doubts, click the document link and review the document.

## Use the Makefile
If you are contributing to this project, use the `Makefile` to help you. You may need the following targets:
- `venv`: initialize the virtual environment.
- `install`: install the dependencies.
- `install-dev`: install the dev dependencies.
- `docs`: generate html doc from the docstring into `/docs`.

There are other targets, use `make help` to find out.
