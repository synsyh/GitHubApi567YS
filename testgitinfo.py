"""
GitHubApi567YS-testgitinfo by Yuning Sun
23:11 2020/2/18
Module documentation: 
"""
import unittest
from unittest import mock

from requests.cookies import MockResponse

from getgitinfo import get_git_info


class TestTriangles(unittest.TestCase):

    @mock.patch('requests.get')
    def test_normal_case(self, mocked_req):
        mocked_req.return_value.text = '[{"id":28765791,"node_id":"MDEwOlJlcG9zaXRvcnkyODc2NTc5MQ==","name":"hellogitworld","full_name":"richkempinski/hellogitworld","private":false,"owner":{"login":"richkempinski","id":1920366,"node_id":"MDQ6VXNlcjE5MjAzNjY=","avatar_url":"https://avatars3.githubusercontent.com/u/1920366?v=4","gravatar_id":"","url":"https://api.github.com/users/richkempinski","html_url":"https://github.com/richkempinski","followers_url":"https://api.github.com/users/richkempinski/followers","following_url":"https://api.github.com/users/richkempinski/following{/other_user}","gists_url":"https://api.github.com/users/richkempinski/gists{/gist_id}","starred_url":"https://api.github.com/users/richkempinski/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/richkempinski/subscriptions","organizations_url":"https://api.github.com/users/richkempinski/orgs","repos_url":"https://api.github.com/users/richkempinski/repos","events_url":"https://api.github.com/users/richkempinski/events{/privacy}","received_events_url":"https://api.github.com/users/richkempinski/received_events","type":"User","site_admin":false},"html_url":"https://github.com/richkempinski/hellogitworld","description":"Sample hellogitworld repo for GitHub Training classes","fork":true,"url":"https://api.github.com/repos/richkempinski/hellogitworld","forks_url":"https://api.github.com/repos/richkempinski/hellogitworld/forks","keys_url":"https://api.github.com/repos/richkempinski/hellogitworld/keys{/key_id}","collaborators_url":"https://api.github.com/repos/richkempinski/hellogitworld/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/richkempinski/hellogitworld/teams","hooks_url":"https://api.github.com/repos/richkempinski/hellogitworld/hooks","issue_events_url":"https://api.github.com/repos/richkempinski/hellogitworld/issues/events{/number}","events_url":"https://api.github.com/repos/richkempinski/hellogitworld/events","assignees_url":"https://api.github.com/repos/richkempinski/hellogitworld/assignees{/user}","branches_url":"https://api.github.com/repos/richkempinski/hellogitworld/branches{/branch}","tags_url":"https://api.github.com/repos/richkempinski/hellogitworld/tags","blobs_url":"https://api.github.com/repos/richkempinski/hellogitworld/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/richkempinski/hellogitworld/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/richkempinski/hellogitworld/git/refs{/sha}","trees_url":"https://api.github.com/repos/richkempinski/hellogitworld/git/trees{/sha}","statuses_url":"https://api.github.com/repos/richkempinski/hellogitworld/statuses/{sha}","languages_url":"https://api.github.com/repos/richkempinski/hellogitworld/languages","stargazers_url":"https://api.github.com/repos/richkempinski/hellogitworld/stargazers","contributors_url":"https://api.github.com/repos/richkempinski/hellogitworld/contributors","subscribers_url":"https://api.github.com/repos/richkempinski/hellogitworld/subscribers","subscription_url":"https://api.github.com/repos/richkempinski/hellogitworld/subscription","commits_url":"https://api.github.com/repos/richkempinski/hellogitworld/commits{/sha}","git_commits_url":"https://api.github.com/repos/richkempinski/hellogitworld/git/commits{/sha}","comments_url":"https://api.github.com/repos/richkempinski/hellogitworld/comments{/number}","issue_comment_url":"https://api.github.com/repos/richkempinski/hellogitworld/issues/comments{/number}","contents_url":"https://api.github.com/repos/richkempinski/hellogitworld/contents/{+path}","compare_url":"https://api.github.com/repos/richkempinski/hellogitworld/compare/{base}...{head}","merges_url":"https://api.github.com/repos/richkempinski/hellogitworld/merges","archive_url":"https://api.github.com/repos/richkempinski/hellogitworld/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/richkempinski/hellogitworld/downloads","issues_url":"https://api.github.com/repos/richkempinski/hellogitworld/issues{/number}","pulls_url":"https://api.github.com/repos/richkempinski/hellogitworld/pulls{/number}","milestones_url":"https://api.github.com/repos/richkempinski/hellogitworld/milestones{/number}","notifications_url":"https://api.github.com/repos/richkempinski/hellogitworld/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/richkempinski/hellogitworld/labels{/name}","releases_url":"https://api.github.com/repos/richkempinski/hellogitworld/releases{/id}","deployments_url":"https://api.github.com/repos/richkempinski/hellogitworld/deployments","created_at":"2015-01-04T06:01:19Z","updated_at":"2015-01-04T06:01:20Z","pushed_at":"2015-01-04T12:34:50Z","git_url":"git://github.com/richkempinski/hellogitworld.git","ssh_url":"git@github.com:richkempinski/hellogitworld.git","clone_url":"https://github.com/richkempinski/hellogitworld.git","svn_url":"https://github.com/richkempinski/hellogitworld","homepage":"https://training.github.com","size":194,"stargazers_count":0,"watchers_count":0,"language":"Java","has_issues":false,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"},{"id":144656027,"node_id":"MDEwOlJlcG9zaXRvcnkxNDQ2NTYwMjc=","name":"helloworld","full_name":"richkempinski/helloworld","private":false,"owner":{"login":"richkempinski","id":1920366,"node_id":"MDQ6VXNlcjE5MjAzNjY=","avatar_url":"https://avatars3.githubusercontent.com/u/1920366?v=4","gravatar_id":"","url":"https://api.github.com/users/richkempinski","html_url":"https://github.com/richkempinski","followers_url":"https://api.github.com/users/richkempinski/followers","following_url":"https://api.github.com/users/richkempinski/following{/other_user}","gists_url":"https://api.github.com/users/richkempinski/gists{/gist_id}","starred_url":"https://api.github.com/users/richkempinski/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/richkempinski/subscriptions","organizations_url":"https://api.github.com/users/richkempinski/orgs","repos_url":"https://api.github.com/users/richkempinski/repos","events_url":"https://api.github.com/users/richkempinski/events{/privacy}","received_events_url":"https://api.github.com/users/richkempinski/received_events","type":"User","site_admin":false},"html_url":"https://github.com/richkempinski/helloworld","description":"My Hello world repository","fork":false,"url":"https://api.github.com/repos/richkempinski/helloworld","forks_url":"https://api.github.com/repos/richkempinski/helloworld/forks","keys_url":"https://api.github.com/repos/richkempinski/helloworld/keys{/key_id}","collaborators_url":"https://api.github.com/repos/richkempinski/helloworld/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/richkempinski/helloworld/teams","hooks_url":"https://api.github.com/repos/richkempinski/helloworld/hooks","issue_events_url":"https://api.github.com/repos/richkempinski/helloworld/issues/events{/number}","events_url":"https://api.github.com/repos/richkempinski/helloworld/events","assignees_url":"https://api.github.com/repos/richkempinski/helloworld/assignees{/user}","branches_url":"https://api.github.com/repos/richkempinski/helloworld/branches{/branch}","tags_url":"https://api.github.com/repos/richkempinski/helloworld/tags","blobs_url":"https://api.github.com/repos/richkempinski/helloworld/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/richkempinski/helloworld/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/richkempinski/helloworld/git/refs{/sha}","trees_url":"https://api.github.com/repos/richkempinski/helloworld/git/trees{/sha}","statuses_url":"https://api.github.com/repos/richkempinski/helloworld/statuses/{sha}","languages_url":"https://api.github.com/repos/richkempinski/helloworld/languages","stargazers_url":"https://api.github.com/repos/richkempinski/helloworld/stargazers","contributors_url":"https://api.github.com/repos/richkempinski/helloworld/contributors","subscribers_url":"https://api.github.com/repos/richkempinski/helloworld/subscribers","subscription_url":"https://api.github.com/repos/richkempinski/helloworld/subscription","commits_url":"https://api.github.com/repos/richkempinski/helloworld/commits{/sha}","git_commits_url":"https://api.github.com/repos/richkempinski/helloworld/git/commits{/sha}","comments_url":"https://api.github.com/repos/richkempinski/helloworld/comments{/number}","issue_comment_url":"https://api.github.com/repos/richkempinski/helloworld/issues/comments{/number}","contents_url":"https://api.github.com/repos/richkempinski/helloworld/contents/{+path}","compare_url":"https://api.github.com/repos/richkempinski/helloworld/compare/{base}...{head}","merges_url":"https://api.github.com/repos/richkempinski/helloworld/merges","archive_url":"https://api.github.com/repos/richkempinski/helloworld/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/richkempinski/helloworld/downloads","issues_url":"https://api.github.com/repos/richkempinski/helloworld/issues{/number}","pulls_url":"https://api.github.com/repos/richkempinski/helloworld/pulls{/number}","milestones_url":"https://api.github.com/repos/richkempinski/helloworld/milestones{/number}","notifications_url":"https://api.github.com/repos/richkempinski/helloworld/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/richkempinski/helloworld/labels{/name}","releases_url":"https://api.github.com/repos/richkempinski/helloworld/releases{/id}","deployments_url":"https://api.github.com/repos/richkempinski/helloworld/deployments","created_at":"2018-08-14T02:06:43Z","updated_at":"2018-10-04T17:46:51Z","pushed_at":"2018-10-04T17:46:50Z","git_url":"git://github.com/richkempinski/helloworld.git","ssh_url":"git@github.com:richkempinski/helloworld.git","clone_url":"https://github.com/richkempinski/helloworld.git","svn_url":"https://github.com/richkempinski/helloworld","homepage":null,"size":4,"stargazers_count":0,"watchers_count":0,"language":"Python","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"},{"id":151335858,"node_id":"MDEwOlJlcG9zaXRvcnkxNTEzMzU4NTg=","name":"Mocks","full_name":"richkempinski/Mocks","private":false,"owner":{"login":"richkempinski","id":1920366,"node_id":"MDQ6VXNlcjE5MjAzNjY=","avatar_url":"https://avatars3.githubusercontent.com/u/1920366?v=4","gravatar_id":"","url":"https://api.github.com/users/richkempinski","html_url":"https://github.com/richkempinski","followers_url":"https://api.github.com/users/richkempinski/followers","following_url":"https://api.github.com/users/richkempinski/following{/other_user}","gists_url":"https://api.github.com/users/richkempinski/gists{/gist_id}","starred_url":"https://api.github.com/users/richkempinski/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/richkempinski/subscriptions","organizations_url":"https://api.github.com/users/richkempinski/orgs","repos_url":"https://api.github.com/users/richkempinski/repos","events_url":"https://api.github.com/users/richkempinski/events{/privacy}","received_events_url":"https://api.github.com/users/richkempinski/received_events","type":"User","site_admin":false},"html_url":"https://github.com/richkempinski/Mocks","description":null,"fork":false,"url":"https://api.github.com/repos/richkempinski/Mocks","forks_url":"https://api.github.com/repos/richkempinski/Mocks/forks","keys_url":"https://api.github.com/repos/richkempinski/Mocks/keys{/key_id}","collaborators_url":"https://api.github.com/repos/richkempinski/Mocks/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/richkempinski/Mocks/teams","hooks_url":"https://api.github.com/repos/richkempinski/Mocks/hooks","issue_events_url":"https://api.github.com/repos/richkempinski/Mocks/issues/events{/number}","events_url":"https://api.github.com/repos/richkempinski/Mocks/events","assignees_url":"https://api.github.com/repos/richkempinski/Mocks/assignees{/user}","branches_url":"https://api.github.com/repos/richkempinski/Mocks/branches{/branch}","tags_url":"https://api.github.com/repos/richkempinski/Mocks/tags","blobs_url":"https://api.github.com/repos/richkempinski/Mocks/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/richkempinski/Mocks/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/richkempinski/Mocks/git/refs{/sha}","trees_url":"https://api.github.com/repos/richkempinski/Mocks/git/trees{/sha}","statuses_url":"https://api.github.com/repos/richkempinski/Mocks/statuses/{sha}","languages_url":"https://api.github.com/repos/richkempinski/Mocks/languages","stargazers_url":"https://api.github.com/repos/richkempinski/Mocks/stargazers","contributors_url":"https://api.github.com/repos/richkempinski/Mocks/contributors","subscribers_url":"https://api.github.com/repos/richkempinski/Mocks/subscribers","subscription_url":"https://api.github.com/repos/richkempinski/Mocks/subscription","commits_url":"https://api.github.com/repos/richkempinski/Mocks/commits{/sha}","git_commits_url":"https://api.github.com/repos/richkempinski/Mocks/git/commits{/sha}","comments_url":"https://api.github.com/repos/richkempinski/Mocks/comments{/number}","issue_comment_url":"https://api.github.com/repos/richkempinski/Mocks/issues/comments{/number}","contents_url":"https://api.github.com/repos/richkempinski/Mocks/contents/{+path}","compare_url":"https://api.github.com/repos/richkempinski/Mocks/compare/{base}...{head}","merges_url":"https://api.github.com/repos/richkempinski/Mocks/merges","archive_url":"https://api.github.com/repos/richkempinski/Mocks/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/richkempinski/Mocks/downloads","issues_url":"https://api.github.com/repos/richkempinski/Mocks/issues{/number}","pulls_url":"https://api.github.com/repos/richkempinski/Mocks/pulls{/number}","milestones_url":"https://api.github.com/repos/richkempinski/Mocks/milestones{/number}","notifications_url":"https://api.github.com/repos/richkempinski/Mocks/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/richkempinski/Mocks/labels{/name}","releases_url":"https://api.github.com/repos/richkempinski/Mocks/releases{/id}","deployments_url":"https://api.github.com/repos/richkempinski/Mocks/deployments","created_at":"2018-10-02T23:15:00Z","updated_at":"2019-03-11T17:03:57Z","pushed_at":"2019-03-11T17:03:55Z","git_url":"git://github.com/richkempinski/Mocks.git","ssh_url":"git@github.com:richkempinski/Mocks.git","clone_url":"https://github.com/richkempinski/Mocks.git","svn_url":"https://github.com/richkempinski/Mocks","homepage":null,"size":13,"stargazers_count":0,"watchers_count":0,"language":"Jupyter Notebook","has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"},{"id":28765763,"node_id":"MDEwOlJlcG9zaXRvcnkyODc2NTc2Mw==","name":"Project1","full_name":"richkempinski/Project1","private":false,"owner":{"login":"richkempinski","id":1920366,"node_id":"MDQ6VXNlcjE5MjAzNjY=","avatar_url":"https://avatars3.githubusercontent.com/u/1920366?v=4","gravatar_id":"","url":"https://api.github.com/users/richkempinski","html_url":"https://github.com/richkempinski","followers_url":"https://api.github.com/users/richkempinski/followers","following_url":"https://api.github.com/users/richkempinski/following{/other_user}","gists_url":"https://api.github.com/users/richkempinski/gists{/gist_id}","starred_url":"https://api.github.com/users/richkempinski/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/richkempinski/subscriptions","organizations_url":"https://api.github.com/users/richkempinski/orgs","repos_url":"https://api.github.com/users/richkempinski/repos","events_url":"https://api.github.com/users/richkempinski/events{/privacy}","received_events_url":"https://api.github.com/users/richkempinski/received_events","type":"User","site_admin":false},"html_url":"https://github.com/richkempinski/Project1","description":null,"fork":false,"url":"https://api.github.com/repos/richkempinski/Project1","forks_url":"https://api.github.com/repos/richkempinski/Project1/forks","keys_url":"https://api.github.com/repos/richkempinski/Project1/keys{/key_id}","collaborators_url":"https://api.github.com/repos/richkempinski/Project1/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/richkempinski/Project1/teams","hooks_url":"https://api.github.com/repos/richkempinski/Project1/hooks","issue_events_url":"https://api.github.com/repos/richkempinski/Project1/issues/events{/number}","events_url":"https://api.github.com/repos/richkempinski/Project1/events","assignees_url":"https://api.github.com/repos/richkempinski/Project1/assignees{/user}","branches_url":"https://api.github.com/repos/richkempinski/Project1/branches{/branch}","tags_url":"https://api.github.com/repos/richkempinski/Project1/tags","blobs_url":"https://api.github.com/repos/richkempinski/Project1/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/richkempinski/Project1/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/richkempinski/Project1/git/refs{/sha}","trees_url":"https://api.github.com/repos/richkempinski/Project1/git/trees{/sha}","statuses_url":"https://api.github.com/repos/richkempinski/Project1/statuses/{sha}","languages_url":"https://api.github.com/repos/richkempinski/Project1/languages","stargazers_url":"https://api.github.com/repos/richkempinski/Project1/stargazers","contributors_url":"https://api.github.com/repos/richkempinski/Project1/contributors","subscribers_url":"https://api.github.com/repos/richkempinski/Project1/subscribers","subscription_url":"https://api.github.com/repos/richkempinski/Project1/subscription","commits_url":"https://api.github.com/repos/richkempinski/Project1/commits{/sha}","git_commits_url":"https://api.github.com/repos/richkempinski/Project1/git/commits{/sha}","comments_url":"https://api.github.com/repos/richkempinski/Project1/comments{/number}","issue_comment_url":"https://api.github.com/repos/richkempinski/Project1/issues/comments{/number}","contents_url":"https://api.github.com/repos/richkempinski/Project1/contents/{+path}","compare_url":"https://api.github.com/repos/richkempinski/Project1/compare/{base}...{head}","merges_url":"https://api.github.com/repos/richkempinski/Project1/merges","archive_url":"https://api.github.com/repos/richkempinski/Project1/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/richkempinski/Project1/downloads","issues_url":"https://api.github.com/repos/richkempinski/Project1/issues{/number}","pulls_url":"https://api.github.com/repos/richkempinski/Project1/pulls{/number}","milestones_url":"https://api.github.com/repos/richkempinski/Project1/milestones{/number}","notifications_url":"https://api.github.com/repos/richkempinski/Project1/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/richkempinski/Project1/labels{/name}","releases_url":"https://api.github.com/repos/richkempinski/Project1/releases{/id}","deployments_url":"https://api.github.com/repos/richkempinski/Project1/deployments","created_at":"2015-01-04T06:00:07Z","updated_at":"2015-01-04T06:00:07Z","pushed_at":"2015-01-04T12:12:11Z","git_url":"git://github.com/richkempinski/Project1.git","ssh_url":"git@github.com:richkempinski/Project1.git","clone_url":"https://github.com/richkempinski/Project1.git","svn_url":"https://github.com/richkempinski/Project1","homepage":null,"size":128,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"},{"id":7468415,"node_id":"MDEwOlJlcG9zaXRvcnk3NDY4NDE1","name":"threads-of-life","full_name":"richkempinski/threads-of-life","private":false,"owner":{"login":"richkempinski","id":1920366,"node_id":"MDQ6VXNlcjE5MjAzNjY=","avatar_url":"https://avatars3.githubusercontent.com/u/1920366?v=4","gravatar_id":"","url":"https://api.github.com/users/richkempinski","html_url":"https://github.com/richkempinski","followers_url":"https://api.github.com/users/richkempinski/followers","following_url":"https://api.github.com/users/richkempinski/following{/other_user}","gists_url":"https://api.github.com/users/richkempinski/gists{/gist_id}","starred_url":"https://api.github.com/users/richkempinski/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/richkempinski/subscriptions","organizations_url":"https://api.github.com/users/richkempinski/orgs","repos_url":"https://api.github.com/users/richkempinski/repos","events_url":"https://api.github.com/users/richkempinski/events{/privacy}","received_events_url":"https://api.github.com/users/richkempinski/received_events","type":"User","site_admin":false},"html_url":"https://github.com/richkempinski/threads-of-life","description":null,"fork":false,"url":"https://api.github.com/repos/richkempinski/threads-of-life","forks_url":"https://api.github.com/repos/richkempinski/threads-of-life/forks","keys_url":"https://api.github.com/repos/richkempinski/threads-of-life/keys{/key_id}","collaborators_url":"https://api.github.com/repos/richkempinski/threads-of-life/collaborators{/collaborator}","teams_url":"https://api.github.com/repos/richkempinski/threads-of-life/teams","hooks_url":"https://api.github.com/repos/richkempinski/threads-of-life/hooks","issue_events_url":"https://api.github.com/repos/richkempinski/threads-of-life/issues/events{/number}","events_url":"https://api.github.com/repos/richkempinski/threads-of-life/events","assignees_url":"https://api.github.com/repos/richkempinski/threads-of-life/assignees{/user}","branches_url":"https://api.github.com/repos/richkempinski/threads-of-life/branches{/branch}","tags_url":"https://api.github.com/repos/richkempinski/threads-of-life/tags","blobs_url":"https://api.github.com/repos/richkempinski/threads-of-life/git/blobs{/sha}","git_tags_url":"https://api.github.com/repos/richkempinski/threads-of-life/git/tags{/sha}","git_refs_url":"https://api.github.com/repos/richkempinski/threads-of-life/git/refs{/sha}","trees_url":"https://api.github.com/repos/richkempinski/threads-of-life/git/trees{/sha}","statuses_url":"https://api.github.com/repos/richkempinski/threads-of-life/statuses/{sha}","languages_url":"https://api.github.com/repos/richkempinski/threads-of-life/languages","stargazers_url":"https://api.github.com/repos/richkempinski/threads-of-life/stargazers","contributors_url":"https://api.github.com/repos/richkempinski/threads-of-life/contributors","subscribers_url":"https://api.github.com/repos/richkempinski/threads-of-life/subscribers","subscription_url":"https://api.github.com/repos/richkempinski/threads-of-life/subscription","commits_url":"https://api.github.com/repos/richkempinski/threads-of-life/commits{/sha}","git_commits_url":"https://api.github.com/repos/richkempinski/threads-of-life/git/commits{/sha}","comments_url":"https://api.github.com/repos/richkempinski/threads-of-life/comments{/number}","issue_comment_url":"https://api.github.com/repos/richkempinski/threads-of-life/issues/comments{/number}","contents_url":"https://api.github.com/repos/richkempinski/threads-of-life/contents/{+path}","compare_url":"https://api.github.com/repos/richkempinski/threads-of-life/compare/{base}...{head}","merges_url":"https://api.github.com/repos/richkempinski/threads-of-life/merges","archive_url":"https://api.github.com/repos/richkempinski/threads-of-life/{archive_format}{/ref}","downloads_url":"https://api.github.com/repos/richkempinski/threads-of-life/downloads","issues_url":"https://api.github.com/repos/richkempinski/threads-of-life/issues{/number}","pulls_url":"https://api.github.com/repos/richkempinski/threads-of-life/pulls{/number}","milestones_url":"https://api.github.com/repos/richkempinski/threads-of-life/milestones{/number}","notifications_url":"https://api.github.com/repos/richkempinski/threads-of-life/notifications{?since,all,participating}","labels_url":"https://api.github.com/repos/richkempinski/threads-of-life/labels{/name}","releases_url":"https://api.github.com/repos/richkempinski/threads-of-life/releases{/id}","deployments_url":"https://api.github.com/repos/richkempinski/threads-of-life/deployments","created_at":"2013-01-06T14:19:28Z","updated_at":"2013-01-13T23:34:33Z","pushed_at":"2013-01-06T14:19:29Z","git_url":"git://github.com/richkempinski/threads-of-life.git","ssh_url":"git@github.com:richkempinski/threads-of-life.git","clone_url":"https://github.com/richkempinski/threads-of-life.git","svn_url":"https://github.com/richkempinski/threads-of-life","homepage":null,"size":108,"stargazers_count":0,"watchers_count":0,"language":null,"has_issues":true,"has_projects":true,"has_downloads":true,"has_wiki":true,"has_pages":false,"forks_count":0,"mirror_url":null,"archived":false,"disabled":false,"open_issues_count":0,"license":null,"forks":0,"open_issues":0,"watchers":0,"default_branch":"master"}]'
        self.assertEqual(get_git_info('richkempinski'), ('Repo: hellogitworld Number of commits: 5'
                                                         'Repo: helloworld Number of commits: 5'
                                                         'Repo: Mocks Number of commits: 5'
                                                         'Repo: Project1 Number of commits: 5'
                                                         'Repo: threads-of-life Number of commits: 5'))


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
