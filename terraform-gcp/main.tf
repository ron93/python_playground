# terraform settings
terraform {
#   required_version = ">= 1.0"

  backend "local" {}  # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online

  required_providers {

    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

# specific provider config
provider "google" {
  credentials = file(var.credentials_file)

  project = var.project
  region  = var.region
#   zone    = var.zone

}


# Data Lake bucket
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket

resource "google_storage_bucket" "data-lake-bucket" {
    name = "${local.data_lake_bucket}_${var.project}" #concatinating Data Lake bucket and proj_name for unique naming
    location = var.region

    # optional but recommended settings 
    storage_class = var.storage_class
    uniform_bucket_level_access = true

    versioning {
       enabled = true

    }

    lifecycle_rule {
       action {
          
            type = "Delete"
          }
          condition {
             
                age = 30 #days
             }
          }
          force_destroy =  true
       }
 
# Data Warehouse
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset

resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.BQ_DATASET
    project = var.project
    location = var.region
  
}


# define infrastructure components

# 'google_compute_network' -> resource type
# 'vpc_network' = resource name
# resource "google_compute_network" "vpc_network" {
#   name = "terraform-network"

# }

# # compute resource 
# resource "google_compute_instance" "vm_instance" {
#   name         = "terraform-instance"
#   machine_type = "f1-micro"
#   tags         = ["web", "dev"]

#   boot_disk {
#     initialize_params {
#       image = "debian-cloud/debian-11"
#     }
#   }

#   network_interface {
#     network = google_compute_network.vpc_network.name
#     access_config {
#     }
#   }
# }
