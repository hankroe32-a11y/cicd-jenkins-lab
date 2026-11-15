pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }
    }

    post {
        always {
            withCredentials([
                string(credentialsId: 'WEBEX_TOKEN', variable: 'WEBEX_TOKEN'),
                string(credentialsId: 'WEBEX_ROOM_ID', variable: 'WEBEX_ROOM_ID')
            ]) {
                sh '''python3 -c '
import os, json, urllib.request
req = urllib.request.Request(
    "https://webexapis.com/v1/messages",
    data=json.dumps({
        "roomId": os.environ["WEBEX_ROOM_ID"],
        "markdown": f"Jenkins Build **{os.environ.get(\"BUILD_STATUS\", \"SUCCESS\")}**: {os.environ[\"JOB_NAME\"]} #{os.environ[\"BUILD_NUMBER\"]}"
    }).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {os.environ[\"WEBEX_TOKEN\"]}",
        "Content-Type": "application/json"
    }
)
urllib.request.urlopen(req)
' '''
            }
        }
    }
}
