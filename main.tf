module "lambda" {
  source = "./module"
  lambda_bucket = "gjygju"
  lambda_file_handler = "lambda_function.lambda_handler"
  lambda_function_name = "test-lambda"
  lambda_memory_size = 512
  lambda_runtime = "python3.8"
  env_vars = {
      name = "first"
      second = "22"
    }
  }

