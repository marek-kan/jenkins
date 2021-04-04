pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'echo "Hello World"'
            }
        }
        stage('Installing Flask') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user flask'
                    sh 'python3 test.py'
                }
            }
        }
        stage('Deploy') {
            steps {
                sshPublisher(
                  continueOnError: false, 
                  failOnError: true,
                  publishers: [
                    sshPublisherDesc(
                      configName: "AppServer",
                      transfers: [sshTransfer(sourceFiles: 'app.py', remoteDirectory: 'test_deploy'),
                                  sshTransfer(sourceFiles: 'wsgi.py', remoteDirectory: 'test_deploy'),
                                  sshTransfer(sourceFiles: 'Dockerfile', remoteDirectory: 'test_deploy'),
                                  sshTransfer(sourceFiles: 'test_dir/**/*', remoteDirectory: 'test_deploy'),
                                  sshTransfer(execCommand: 'docker built -t flask_app_image ./'),
                                  sshTransfer(execCommand: 'docker run -d -t -p 8080:8080 --name flask_app flask_app_image'),
                                  shTransfer(execCommand: 'docker exec -it flask_app'),
                                  shTransfer(execCommand: 'gunicorn -b 0.0.0.0:8080 usr.test_deploy.wsgi:application')],
                      verbose: true
                    )
                  ]
                )
            }
        }
    }
}