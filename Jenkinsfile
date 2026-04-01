pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.10'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Info') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python --version'
                    } else {
                        bat 'python --version'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python -m pip install --upgrade pip
                            if [ ! -f requirements.txt ]; then echo "requirements.txt not found"; exit 1; fi
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m pip install --upgrade pip
                            if not exist requirements.txt (echo requirements.txt not found && exit /b 1)
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Lint with Ruff') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    script {
                        if (isUnix()) {
                            sh 'ruff --output-format=github --target-version=py310 .'
                        } else {
                            bat 'ruff --output-format=github --target-version=py310 .'
                        }
                    }
                }
            }
        }

        stage('Test with Pytest + Coverage') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'coverage run -m pytest -v -s'
                    } else {
                        bat 'coverage run -m pytest -v -s'
                    }
                }
            }
        }

        stage('Coverage Report') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'coverage report -m'
                    } else {
                        bat 'coverage report -m'
                    }
                }
            }
        }
    }
}
