from metadata.sdk import configure
from metadata.sdk.entities import Containers
from metadata.sdk.entities import APICollections
from metadata.sdk.entities import Teams
from metadata.generated.schema.api.data.createContainer import CreateContainerRequest
import os
import json
from metadata.generated.schema.api.teams.createTeam import CreateTeamRequest
from metadata.sdk import configure
from metadata.sdk.entities import Users
from metadata.generated.schema.api.teams.createUser import CreateUserRequest
from metadata.generated.schema.api.data.createContainer import CreateContainerRequest
from metadata.generated.schema.type.entityReference import EntityReference
from metadata.sdk.entities import Containers

from dotenv import load_dotenv

load_dotenv()


configure(host="http://localhost:8585/api", jwt_token=os.getenv("METADATA_ADMIN_TOKEN"))


for container in Containers.list_all():
    print(container.name)


team_request = CreateTeamRequest(
    name="Data_engineer",
    teamType="Group",
    displayName="Data_engineer",
    description="Data_engineer"
)

team = Teams.create(team_request)
print(f"Created: {team.fullyQualifiedName}")
print(f"Created: {team.id.root}")

user_request = CreateUserRequest(
    name="aaron_johnson0",
    displayName="Aaron Johnson",
    email="aaron_johnson0@gmail.com",
    description="Data analyst in the Sales team"
)

user = Users.create(user_request)
print(f"Created: {user.fullyQualifiedName}")



buckets = ["raw", "staging", "curated", "archive"]

for bucket in buckets:
    with open(f"metadata/{bucket}/{bucket}_lines.json") as f:
        lines = json.load(f)


    bucket_container = Containers.retrieve_by_name(f"minio.{bucket}")
    print(f"here is bucket container: {bucket_container}")

    parent_ref = EntityReference(
        id=bucket_container.id,
        type="container"
    )

    for line in lines:
        print(line.get("name"))

        request = CreateContainerRequest(
            name= line.get("name"),
            displayName= line.get("displayName"),
            description= line.get("description"),
            prefix= line.get("prefix"),
            fileFormats= line.get("fileFormats"),
            dataModel= line.get("dataModel"),
            owners= [
                {
                "id":f"{team.id.root}",
                "type": "team",
                "name": "Data_engineer"
                }
            ],
            # tags= [
            #     {
            #     "tagFQN": "datalake",
            #     "labelType": "Manual",
            #     "source": "Classification",
            #     "state": "Confirmed"
            #     },
            #     {
            #     "tagFQN": "raw",
            #     "labelType": "Manual",
            #     "source": "Classification",
            #     "state": "Confirmed"
            #     }
            # ]
            service= line.get("service"),
            parent = parent_ref
        )

        container = Containers.create(request)
        print(f"Created: {container.fullyQualifiedName}")


for container in Containers.list_all():
    print(container.name)

