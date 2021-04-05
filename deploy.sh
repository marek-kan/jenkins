docker stop flask_app || echo flask_app not running
docker rm flask_app || echo no flask_app container
docker rmi flask_app_image || echo no flask_app_image
docker build -t flask_app_image ./test_deploy/
docker run -d -t -p 8080:8080 --name flask_app flask_app_image