import json
from six import StringIO
import requests


def post(url, repo_token, service_job_id, service_name, git, source_files, parallel):
    json_file = build_file(repo_token, service_job_id, service_name, git, source_files, parallel)
    return requests.post(url, files={'json_file': json_file}, verify=False)


def build_file(repo_token, service_job_id, service_name, git, source_files, parallel):
    content = {
        'service_job_id': service_job_id,
        'service_name': service_name,
        'git': git,
        'source_files': source_files,
    }
    if repo_token:
        content['repo_token'] = repo_token
    if parallel:
        content['parallel'] = True
    return StringIO(json.dumps(content))
