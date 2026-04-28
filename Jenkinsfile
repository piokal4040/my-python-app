pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                '''
            }
        }

        stage('Lint') {
            steps {
                bat '''
                    venv\\Scripts\\pip.exe install flake8
                    venv\\Scripts\\flake8.exe src/ --max-line-length=120
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    venv\\Scripts\\pip.exe install pytest
                    venv\\Scripts\\pytest.exe tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Something went wrong. Check the logs.'
        }
    }
}