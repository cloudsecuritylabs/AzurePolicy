# Examples
# Useful when developing custom policies
az provider show --namespace Microsoft.Storage --expand "resourceTypes/aliases" --query "resourceTypes[].aliases[].name"
az provider show --namespace Microsoft.ContainerInstance --expand "resourceTypes/aliases" --query "resourceTypes[].aliases[].name"
