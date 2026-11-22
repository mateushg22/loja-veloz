provider "aws" {
  region = "us-east-1"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version         = "~> 20.0"
  cluster_name    = "loja-veloz-cluster"
  cluster_version = "1.30"

  vpc_id     = "vpc-12345678"
  subnet_ids = ["subnet-abc", "subnet-xyz"]

  eks_managed_node_groups = {
    nodes = {
      min_size       = 2
      max_size       = 8
      desired_size   = 2
      instance_types = ["t3.medium"]
    }
  }
}
