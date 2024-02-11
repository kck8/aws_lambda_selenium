param([Parameter(Mandatory)][string]$ecr) 
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ecr
docker build -t lambda-selenium .
docker tag lambda-selenium:latest $ecr/lambda-selenium:latest
docker push $ecr/lambda-selenium:latest
