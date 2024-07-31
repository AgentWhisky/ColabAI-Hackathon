import os
import xmltodict
import json
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex, ComplexField, SimpleField, edm
from azure.core.credentials import AzureKeyCredential

# Set up Azure Cognitive Search
service_endpoint = "<YOUR_COGNITIVE_SEARCH_ENDPOINT>"
api_key = "<YOUR_COGNITIVE_SEARCH_API_KEY>"

index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))
search_client = SearchClient(service_endpoint, "awards-index", AzureKeyCredential(api_key))

# Define the index schema
index_name = "awards-index"
fields = [
    SimpleField(name="AwardID", type=edm.String, key=True),
    SimpleField(name="AwardTitle", type=edm.String),
    SimpleField(name="AbstractNarration", type=edm.String),
    SimpleField(name="AwardEffectiveDate", type=edm.DateTimeOffset),
    SimpleField(name="AwardExpirationDate", type=edm.DateTimeOffset),
    SimpleField(name="AwardAmount", type=edm.Int32),
    ComplexField(name="Organization", fields=[
        SimpleField(name="Code", type=edm.Int32),
        SimpleField(name="Directorate", type=edm.String),
        SimpleField(name="Division", type=edm.String)
    ]),
    ComplexField(name="ProgramOfficer", fields=[
        SimpleField(name="SignBlockName", type=edm.String)
    ]),
    ComplexField(name="Investigators", collection=True, fields=[
        SimpleField(name="FirstName", type=edm.String),
        SimpleField(name="LastName", type=edm.String),
        SimpleField(name="EmailAddress", type=edm.String),
        SimpleField(name="StartDate", type=edm.DateTimeOffset),
        SimpleField(name="EndDate", type=edm.DateTimeOffset),
        SimpleField(name="RoleCode", type=edm.Int32)
    ]),
    ComplexField(name="Institutions", collection=True, fields=[
        SimpleField(name="Name", type=edm.String),
        SimpleField(name="CityName", type=edm.String),
        SimpleField(name="ZipCode", type=edm.Int32),
        SimpleField(name="PhoneNumber", type=edm.Double),
        SimpleField(name="StreetAddress", type=edm.String),
        SimpleField(name="CountryName", type=edm.String),
        SimpleField(name="StateName", type=edm.String),
        SimpleField(name="StateCode", type=edm.String)
    ]),
    ComplexField(name="FoaInformation", collection=True, fields=[
        SimpleField(name="Code", type=edm.Int32),
        SimpleField(name="Name", type=edm.String)
    ]),
    ComplexField(name="ProgramElements", collection=True, fields=[
        SimpleField(name="Code", type=edm.Int32),
        SimpleField(name="Text", type=edm.String)
    ]),
    ComplexField(name="ProgramReferences", collection=True, fields=[
        SimpleField(name="Code", type=edm.Int32),
        SimpleField(name="Text", type=edm.String)
    ])
]

index = SearchIndex(name=index_name, fields=fields)
index_client.create_index(index)

# Convert XML files to JSON
def convert_xml_to_json(xml_folder):
    awards_data = []
    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            filepath = os.path.join(xml_folder, filename)
            with open(filepath, 'r') as file:
                xml_content = file.read()
                parsed_data = xmltodict.parse(xml_content)
                award_data = parsed_data['rootTag']['Award']
                awards_data.append(award_data)
    return awards_data

xml_folder = 'assets/xml'
awards_data = convert_xml_to_json(xml_folder)

# Upload documents to Cognitive Search
search_client.upload_documents(documents=awards_data)
print("XML files have been successfully converted to JSON and uploaded to Azure Cognitive Search.")
