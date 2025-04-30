# Databricks Asset Bundles

Databricks Asset Bundles are essentially end-to-end definitions of a project, including information such as:
- How the project should be structured, tested, and deployed
- Descriptions of Databricks jobs and pipelines as source files
- Integration of source control, code review, CI/CD, and other software engineering best practices

This takes the form of a collection of source files and metadata deployed as a single bundle to your target environment. The bundle includes the following parts:
- Required cloud infrastructure and workspace configs
- Source files like notebooks, Python files, and business logic
- Definitions and settings for Databricks resources including jobs, DLT pipelines, Model Serving endpoints, MLflow Experiments, MLflow registered models, etc.
- Unit and integration tests

Here's a diagram providing a high-level view of a development and CI/CD pipeline with asset bundles:
![A diagram providing a high-level view of a development and CI/CD pipeline with asset bundles.](https://learn.microsoft.com/en-us/azure/databricks/_static/images/bundles/bundles-cicd.png)

Bundles are defined and managed through YAML templates and other files that exist alongside source code, making asset bundles a good IaC option.

## How Asset Bundles Work

Asset bundle metadata is defined using YAML files that specify artifacts, resources, and the configuration of a Databricks project. The Databricks CLI can then be used to validate, deploy, and run bundles using the YAML files. Running the bundle projects can be done from IDEs, terminals, or within Databricks.

Bundles can be created manualy or based on a template, like the one provided by the Databricks CLI which is intended for simple use cases.

## Requirements

Databricks Asset Bundles are a feature of the Databricks CLI. Bundles are built locally and then the Databricks CLI is used to deploy the bundle to a target Databricks workspace.

Building, deploying, and running bundles in an Azure Databricks workspace requires:
- Workspace files enabled
- Databricks CLI
- The CLI must be configured to access your Databricks workspaces

## Quick Start

Create your first bundle project using the Databricks CLI:

`databricks bundle init`

This command presents a choice of Databricks-provided default bundle templates.