variable "aws_region" {
  default = "us-east-1"
}

variable "key_pair_name" {
  description = "EC2 key pair name"
  type        = string
}

variable "db_username" {
  default = "postgres"
}

variable "db_password" {
  description = "RDS password"
  sensitive   = true
}
