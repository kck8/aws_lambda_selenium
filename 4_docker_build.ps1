param([switch] $nocache)

if ($nocache) {
    echo "cache disabled"
    docker build --platform linux/amd64 -t lambda-selenium . --no-cache --progress=plain
}
else {
    echo "cache enabled"
    docker build --platform linux/amd64 -t lambda-selenium . --progress=plain
}