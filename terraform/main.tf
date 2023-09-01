terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
  # access_key = "$access_key"
  # secret_key = "$secret_key"
}

resource "aws_instance" "prometheus-server" {
  ami           = "ami-08d4ac5b634553e16" #ubuntu 20.04 LTS // us-east-1
  instance_type = "t2.micro"
  key_name      = "ados-us-east1"

  #vpc_security_group_ids = [
   # aws_security_group.prometheus-iac-sg.id
  #]
  #   root_block_device {
  #     delete_on_termination = true
  #     iops = 150
  #     volume_size = 10
  #     volume_type = "gp2"
  #  }
  tags = {
    Name    = "PrometheusServer"
    OS      = "ubuntu"
    Managed = "IaC"
  }

 # depends_on = [aws_security_group.prometheus-iac-sg]
}


