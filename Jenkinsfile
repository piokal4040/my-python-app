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
                    venv\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                bat '''
                    venv\\Scripts\\pip.exe install flake8
                    venv\\Scripts\\flake8.exe src/ --max-line-length=120 --jobs=1
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
                    venv\\Scripts\\python.exe -c "from deployed_app.src.app import app; client = app.test_client(); response = client.get('/'); assert response.status_code == 200; print('Smoke test passed from deployed_app')"
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
