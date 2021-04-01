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
                    sh 'PID=$!'
                    sh 'pip3 install --user flask'
                    sh 'python3 app.py'
                    sh 'kill $PID'
                }
            }
        }
    }
}