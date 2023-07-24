
### Concepts
* [Terraform_overview](../1_terraform_overview.md)
* [Audio](https://drive.google.com/file/d/1IqMRDwJV-m0v9_le_i2HA_UbM_sIWgWx/view?usp=sharing)

### Execution

```shell
export GOOGLE_APPLICATION_CREADENTIALS={path_to_credential_file}

```

```shell
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan 
```

```shell
# Create new infra
terraform apply 
```

```shell
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```

<!-- format config file file -->
`terrafom fmt`

<!-- validate -->
```shell
terraform validate

```


<!-- view data output -->
```shell
terraform output
```