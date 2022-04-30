provider "azurerm" {
  features {}
#  subscription_id = "xxxxxxxx-xxxxxxx-xxxxxxxx"
}

terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = ">= 2.96.0"
    }
  }
}

resource "azurerm_management_group_policy_assignment" "example" {
  name                 = "someAssignmentName"
  display_name = "Name of the assignment"
  description = "Description of the assignment"
  policy_definition_id = "/providers/Microsoft.Management/managementgroups/mg/providers/Microsoft.Authorization/policySetDefinitions/xxxxxxxxxxxxx"
  management_group_id  = "/providers/Microsoft.Management/managementGroups/mg"
  location = "uksouth"
  identity {
    type = "SystemAssigned"
  }

  parameters           =  <<PARAM
      {
        "parameter1": {
          "value": "pppppppppppppp"
        },
        "parameter2": {
          "value": "somevalue"
        }
      }
    PARAM
}

