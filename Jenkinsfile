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
                bat '''
                    if exist deployed_app rmdir /S /Q deployed_app
                    mkdir deployed_app
                    xcopy src deployed_app\\src\\ /E /I /Y
                    venv\\Scripts\\python.exe -c "from deployed_app.src.app import add; assert add(2, 3) == 5; print('Smoke test passed from deployed_app')"
                '''
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
