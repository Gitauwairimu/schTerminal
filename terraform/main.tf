terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }

  required_version = ">= 1.0.0"

  backend "s3" {
      # Replace this with your bucket name!
      bucket = "terminal-terraform-state-bucket"
      key = "terraform.tfstate"
      region= "us-east-1"
      # region= "af-south-1"
      encrypt        = true
     }
}

provider "aws" {
  # region = "us-east-1"
  region= "af-south-1"
  # access_key = "$access_key"
  # secret_key = "$secret_key"
}



resource "aws_instance" "prometheus-server" {
#  ami           = "ami-08d4ac5b634553e16" #ubuntu 20.04 LTS // us-east-1
#  ami           = "ami-053b0d53c279acc90" #22.04 LTS, amd64 // us-east-1
  ami           = "ami-02a9d4cace1c5a38a" #22.04 LTS, amd64 // af-south-1
  
  instance_type = "t3.micro"
  # key_name      = "terminal-app-github"
  key_name      = "af-git-key"

  vpc_security_group_ids = [
    aws_security_group.terminal-iac-sg.id
  ]
  #   root_block_device {
  #     delete_on_termination = true
  #     iops = 150
  #     volume_size = 10
  #     volume_type = "gp2"
  #  }
  tags = {
    Name    = "TerminalServer"
    OS      = "ubuntu"
    Managed = "IaC"
  }

  depends_on = [aws_security_group.terminal-iac-sg]
}


resource "aws_security_group" "terminal-iac-sg" {
  name = "terminal-iac-sg"
  description = "Security group for terminal server"
 # vpc_id = vpc-08aa5435941a55127

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  } 

  egress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
