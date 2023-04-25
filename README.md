# BestGroupProject

* Jesse
* Rob
* Jeremy
* Zach

This project is for a CI/CD pipeline

Overview - Describe how project is



SETUP-
RUNNING LOCALLY- 
Steps:


RUNNING WITH DOCKER- 
Steps:
1. cd into your preferred directory.
2. clone the repository into the directory. (git clone <repository>)
3. cd into the repository. (cd <repository name>)
4. create a python virtual enviorment. (python3 -m venv .venv)
5. Activate the virtual enviorment. (source .venv/bin/activate)
6. Run the up script to start the web server (./up)
7. go to localhost:8000 to see the live web server
8. Run the down script to shut down the web server (./down)

RUNNING WITH AWS-
Steps:
1. Specify a name for the machine
2. Select vockey for the Key Pair
3. Select "Allow HTTP traffic from the internet" under "Network settings"
4. Under "Advanced details" in the "User data" section add contents of aws_user_data file
5. Launch the instance!
Due to the fact that we are running on temporary instances, another step is necessary
6. Copy Public IPv4 DNS or address and update AWS_IP github repo variable to have deploy functionality
7. Go to previously copied IPv4 DNS or address to see the live server!
8. Run the down script to shut down the web server through ssh, or alternatively stop the instance.




TECHNOLOGIES USED- 
1. GitHub- https://github.com/
2. GitHub Actions- https://github.com/features/actions
3. Docker- https://www.docker.com/
4. AWS- https://aws.amazon.com/free/?trk=578b2801-ffbb-4021-a1db-01a0bafb3a4a&sc_channel=ps&ef_id=CjwKCAjw0ZiiBhBKEiwA4PT9z3Co_hPjev-0Lhz9weyBQcxIxKIhR-    JiYqfFF6otaQwEf0n42PelTxoCp-UQAvD_BwE:G:s&s_kwcid=AL!4422!3!592542020605!p!!g!!aws!12563449882!121199905124&all-free-tier.sort-          by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all
5. Python Virtual Enviorment- https://docs.python.org/3/library/venv.html
6. Mac OS Command Terminal

BACKGROUND- 
1. GitHub Actions- https://github.com/features/actions
2. SSH to an EC2 instance (AWS)- https://labs.vocareum.com/web/2275840/1605208.0/ASNLIB/public/docs/lang/en-us/README.html#ssh
3. SSH on mac (AWS)- https://labs.vocareum.com/web/2275840/1605208.0/ASNLIB/public/docs/lang/en-us/README.html#sshmac
4. GitHub Variables- https://docs.github.com/en/actions/learn-github-actions/variables
5. GitHub Secrets- https://docs.github.com/en/actions/security-guides/encrypted-secrets
6. Triggering workflows on merge- https://github.com/orgs/community/discussions/26724

