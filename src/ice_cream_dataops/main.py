from dotenv import load_dotenv
import os
from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials

load_dotenv()

def main():
    creds = OAuthClientCredentials(
        token_url=f"https://login.microsoftonline.com/{os.environ['IDP_TENANT_ID']}/oauth2/v2.0/token",
        client_id=os.environ["IDP_CLIENT_ID"],
        client_secret=os.environ["IDP_CLIENT_SECRET"],
        scopes=[f"https://{os.environ['CDF_CLUSTER']}.cognitedata.com/.default"],
    )

    config = ClientConfig(
        client_name="ice-cream-dataops",
        project=os.environ["CDF_PROJECT_POC"],
        base_url=f"https://{os.environ['CDF_CLUSTER']}.cognitedata.com",
        credentials=creds,
    )

    client = CogniteClient(config)

    print(client.assets.list(limit=1))

if __name__ == "__main__":
    main()