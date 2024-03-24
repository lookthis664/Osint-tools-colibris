# COLIBRIS
<p align="center">
  <img src="https://img.shields.io/badge/last%20update-24%2F03%2F24-red">
  <br>
  I have decided to revert back to version 1.0 of the software, keeping only the '-u/--username' functionality to focus solely on this feature. I have added a loading bar that is more intuitive to understand, fixed major issues at the launch of the software, and utilized the GitHub API to collect a person's email address from their GitHub profile. And you can use the new GitHub feature to test, I am waiting for your feedback.

<h1 align="center">
  <br>
  <a href="">
    <img src="photo/logo.png" width=300 style="border-radius:50%">
  </a> 
  </div>
  <br>
  COLIBRIS OSINT
  <br>
</h1>

<h4 align="center">OSINT tools work with web scraping.</h4>

<p align="center">
  <a href="">
    <img src="https://img.shields.io/badge/version-v1.1-blue">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/platform-windows%2Fmacos%2Flinux-lightgrey">
  </a>
  <a href="">
      <img src="https://img.shields.io/badge/format-Python 3.11-l">
  </a>
</p>

<p align="center">
  <img src="photo/1.png" width=700>
</p>


## **Features**
- [x] Get links & category from a username
- [X] Get email & name from a GitHub account
- [X] Reactive to command

## **_Requirements_**
```
pip install -r requirements.txt
```
This installs all requirements needed

⚠️ You need to have a good Wi-Fi connection in order to fully utilize the power of the software.


## **_Startup_**
**First you need to set up a discord webhook with the following command:**
Use this to start it with Python:
```
py src/colibris.py -w {enter your webhook}
// OR
python3 src/colibris.py -w {enter your webhook}
```


### All command here:
| **👀 Username command** | **🧪 GitHub command** | **❓ Help command** | **📋 Webhook command** |
| ------------- | ------------- | ------------- |------------- | 
| py src/colibris.py -u {username} | py src/colibris.py -g {username} | py src/colibris.py -h | py src/colibris.py -w {webhook}| 

# Author

> Github: lookthis664

> Discord: plesir_soumision_caca

Colibris osint

