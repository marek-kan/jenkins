pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'echo "Hello World"'
            }
        }
        stage('Testing Flask') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip3 install --user flask'
                    sh 'python3 test.py'
                }
            }
        }
        if (env.GIT_BRANCH == 'master') {
            stage ('Deploy INFO'){
                sh 'echo "using master server"'
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
                                      sshTransfer(sourceFiles: '__init__.py', remoteDirectory: 'test_deploy'),
                                      sshTransfer(sourceFiles: 'Dockerfile', remoteDirectory: 'test_deploy'),
                                      sshTransfer(sourceFiles: 'test_dir/**/*', remoteDirectory: 'test_deploy'),
                                      sshTransfer(sourceFiles: 'start_app.sh', remoteDirectory: 'test_deploy'),
                                      sshTransfer(execCommand: 'docker stop flask_app || echo flask_app not running'),
                                      sshTransfer(execCommand: 'docker rm flask_app || echo no flask_app container'),
                                      sshTransfer(execCommand: 'docker rmi flask_app_image || echo no flask_app_image'),
                                      sshTransfer(execCommand: 'docker build -t flask_app_image ./test_deploy/'),
                                      sshTransfer(execCommand: 'docker run -d -t -p 8080:8080 --name flask_app flask_app_image')],
                          verbose: true
                        )
                      ]
                    )
                }
            }
            stage('Start App') {
                steps {
                    sshPublisher(
                      continueOnError: false, 
                      failOnError: true,
                      publishers: [
                        sshPublisherDesc(
                          configName: "AppServer",
                          transfers: [sshTransfer(execCommand: 'pwd'),
                                      sshTransfer(execCommand: 'sh -x ./test_deploy/start_app.sh')],
                          verbose: true
                        )
                      ]
                    )
                }
            }  
        }
        if (env.GIT_BRANCH == 'dev') {
            stage ('Deploy INFO'){
                sh 'echo "using dev server"'
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
                                      sshTransfer(sourceFiles: '__init__.py', remoteDirectory: 'test_deploy'),
                                      sshTransfer(sourceFiles: 'Dockerfile', remoteDirectory: 'test_deploy'),
                                      sshTransfer(sourceFiles: 'test_dir/**/*', remoteDirectory: 'test_deploy'),
                                      sshTransfer(sourceFiles: 'start_app.sh', remoteDirectory: 'test_deploy'),
                                      sshTransfer(execCommand: 'docker stop flask_app || echo flask_app not running'),
                                      sshTransfer(execCommand: 'docker rm flask_app || echo no flask_app container'),
                                      sshTransfer(execCommand: 'docker rmi flask_app_image || echo no flask_app_image'),
                                      sshTransfer(execCommand: 'docker build -t flask_app_image ./test_deploy/'),
                                      sshTransfer(execCommand: 'docker run -d -t -p 8080:8080 --name flask_app flask_app_image')],
                          verbose: true
                        )
                      ]
                    )
                }
            }
            stage('Start App') {
                steps {
                    sshPublisher(
                      continueOnError: false, 
                      failOnError: true,
                      publishers: [
                        sshPublisherDesc(
                          configName: "AppServer",
                          transfers: [sshTransfer(execCommand: 'pwd'),
                                      sshTransfer(execCommand: 'sh -x ./test_deploy/start_app.sh')],
                          verbose: true
                        )
                      ]
                    )
                }
            }  
        }
        else{
            stage('Deploy ERROR'){
                sh 'unknown branch ${env.GIT_BRANCH}'
                sh 'exit 125'
            }
        }
    }
}
