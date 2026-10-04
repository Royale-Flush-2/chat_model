variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-2"
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "centinela-chat-model"
}

variable "database_url" {
  description = "Database URL for the application"
  type        = string
  sensitive   = true
  default     = ""
}

variable "openai_api_key" {
  description = "API Key for OpenAI LLM"
  type        = string
  sensitive   = true
  default     = ""
}
