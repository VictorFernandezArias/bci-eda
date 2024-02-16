# Define el JSON como un diccionario en Python
event = {
    "problemId": "130040776500213880_1708022040000V2",
    "displayId": "P-24021750",
    "title": "Test EDA",
    "impactLevel": "ENVIRONMENT",
    "severityLevel": "AVAILABILITY",
    "status": "OPEN",
    "affectedEntities": [
        {
            "entityId": {
                "id": "ENVIRONMENT-0000000000000001",
                "type": "ENVIRONMENT"
            },
            "name": "0_BCI_Certificacion"
        }
    ],
    "impactedEntities": [
        {
            "entityId": {
                "id": "ENVIRONMENT-0000000000000001",
                "type": "ENVIRONMENT"
            },
            "name": "0_BCI_Certificacion"
        }
    ],
    "rootCauseEntity": "None",
    "managementZones": [],
    "entityTags": [],
    "problemFilters": [
        {
            "id": "c21f969b-5f03-333d-83e0-4f8f136e7682",
            "name": "Default"
        },
        {
            "id": "eb72a4b4-750a-341c-a99c-1d068b901a79",
            "name": "SinSinteticos"
        },
        {
            "id": "a4911f2f-3469-3014-8691-2786ef0b1c5c",
            "name": "All"
        }
    ],
    "startTime": 1708022220000,
    "endTime": -1,
    "recentComments": {
        "totalCount": 1,
        "comments": [
            {
                "id": "5157188417883994691_1708022040000",
                "createdAtTimestamp": 1708022664824,
                "content": "test eda",
                "authorName": "fquirog@bci.cl"
            }
        ]
    },
    "meta": {
        "source": {
            "name": "dynatrace Saas",
            "type": "dynatrace.event_driven_ansible.dt_esa_api"
        },
        "received_at": "2024-02-15T18:45:17.977298Z",
        "uuid": "ce55212b-b7b9-476a-accf-4bcef28675bf"
    }
}

# Extrae el valor de "content" del diccionario y guárdalo en una variable
comentario = event["recentComments"]["comments"][0]["content"]

# Imprime el comentario
print(comentario)
