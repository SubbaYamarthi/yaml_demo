# import yaml

# # Open and read the YAML file
# with open('demo.yaml', 'r') as file:
#     config = yaml.safe_load(file)
# # Access the values
# string_value = config.get('name')
# integer_value = config.get('age')

# # Print the values
# print(f"name: {string_value}")
# print(f"age: {integer_value}")


import yaml
# Load multiple documents
with open('demo.yaml', 'r') as file:
    data = yaml.safe_load_all(file)#By using yaml.safe_load_all, you can handle multiple documents in a single YAML stream, preventing the ComposerError.
    for doc in data:
        print(doc)
