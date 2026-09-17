terraform { required_version = ">= 1.6.0" }
variable "project_id" { type = string }
variable "workload_name" { type = string }
resource "google_service_account" "workload" { project=var.project_id account_id=var.workload_name display_name="Platform workload identity" }
resource "google_logging_project_sink" "audit" { project=var.project_id name="platform-audit" destination="storage.googleapis.com/REPLACE_WITH_APPROVED_BUCKET" filter="logName:(cloudaudit.googleapis.com)" }
