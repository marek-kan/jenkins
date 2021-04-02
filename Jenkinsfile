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
                      transfers: [sshTransfer(sourceFiles: 'app.py'),
                                  sshTransfer(sourceFiles: 'Jenkinsfile'),
                                  sshTransfer(sourceFiles: './test_dir/.gitkeep'),
                                  sshTransfer(sourceFiles: './test_dir/subdir/.gitkeep')],
                      verbose: true
                    )
                  ]
                )
            }
        }
    }
}