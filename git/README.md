# 📘 Git Basic Commands – Quick Reference Guide

This folder will cover git topics like
staging
commit
branches
merge conflicts

## Git Setup
Install git from its website and open the git terminal to run git commands

## Github set up
Create an account in github and we're good to start. Create a repo in github.

The repo has two main ways to communicate with it.
1. HTTPS
2. SSH

### HTTPS
It's just basically a hash code(token) that replaces password
To generate a Token go to Profile > settings > Developer Settings > Personal Access Token

Every time we communicate with github (pull or push) we can enter the Token when it asks for password
Note: Ater Token was generated we have to copy it and save the key anywhere safely. (we cannot retrieve it afterwards)

### SSH
It was more secure way of Authentication. Here we basically create two keys
private key
Public key

Private Key should be saved our local (/users/.ssh)

public key will be added to the github under 
Profile > settings > SH and GPG Keys > New SSH Key

IF I was communicating with multiple github accounts We have to setup ssh config and add profiles

# 🔐 Git SSH Setup with Multiple GitHub Profiles (Personal & Work)

This guide helps configure SSH for two GitHub accounts:

github-personal
github-work

1️⃣ Check Existing SSH Keys
ls ~/.ssh
If you see id_ed25519, id_rsa, or similar → SSH already exists.

2️⃣ Generate SSH Keys

🔹 Personal GitHub
ssh-keygen -t ed25519 -C "personal@email.com"
When prompted:
Enter file in which to save the key: /c/Users/YourName/.ssh/id_ed25519_personal

🔹 Work GitHub
ssh-keygen -t ed25519 -C "work@email.com"
Save as:
/c/Users/YourName/.ssh/id_ed25519_work


✅ Check created keys:
ls ~/.ssh

3️⃣ Start SSH Agent
eval "$(ssh-agent -s)"

✅ You should see:
Agent pid 12345

4️⃣ Add Keys to SSH Agent
ssh-add ~/.ssh/id_ed25519_personal
ssh-add ~/.ssh/id_ed25519_work

✅ Verify added keys:
ssh-add -l

5️⃣ Add Keys to GitHub

Copy public keys:
cat ~/.ssh/id_ed25519_personal.pub
cat ~/.ssh/id_ed25519_work.pub

Paste each into:
GitHub → Settings → SSH and GPG Keys → New SSH Key

6️⃣ Configure SSH for Multiple Accounts

Edit config file:
nano ~/.ssh/config

Paste:
/# Personal GitHub
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_personal

/# Work GitHub
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work

Save & exit.


7️⃣ Clone Repos Using Correct Profile
Personal Repo
git clone git@github-personal:username/repo.git

Work Repo
git clone git@github-work:orgname/repo.git

## Configure Git Profiles
Global default (personal)
git config --global user.name "Your Name"
git config --global user.email "personal@email.com"

Work profile (local repo only)

Inside work repo:
git config user.name "Your Work Name"
git config user.email "work@email.com"


# ✅ Verify:

git config user.name
git config user.email

Verify Git Configs
Check global config
git config --global --list

Check local repo config
git config --list

key used
ssh -vT github-personal

Check remote URL
git remote -v

Set remote to use correct profile
git remote set-url origin git@github-work:org/repo.git