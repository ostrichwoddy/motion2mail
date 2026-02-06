# 📹 MOTION2MAIL

## 🚀 DESCRIPTION
This is a Python application that monitors a webcam feed to detect motion. When motion is detected, it captures photograph of the moving object and sends a notification via email, along with the picture as attachment.

## 🌍 POSSIBLE APPLICATIONS
### **🏠 Home Security Monitoring**  
This system can be used as a lightweight home security solution to monitor entrances, rooms, or outdoor areas and notify users when unexpected motion is detected.

### **🏢 Office and Workspace Surveillance**  
Small offices and shared workspaces can use this project to track after-hours activity and receive alerts when movement occurs outside normal operating times.

### **🏬 Retail Store Monitoring**  
Retail environments can adapt this system to monitor restricted areas, storage rooms, or storefront activity during closed hours without deploying expensive surveillance systems.

### **🦌 Wildlife or Outdoor Observation**  
With minor adjustments, the application can be used to capture images of wildlife movement for research or observation purposes in outdoor or rural environments.

## ⚙️ MECHANISM
Motion2mail uses the OpenCV library to initialize webcam and stores the first frame for reference. Then it converts each frame to grayscale and applies Gaussian blur. It then checks for absolute differences betwewen the current and reference frame. Thresholding and dilation are applied to highlight motion. It ignores small movement but detects contours and draws a bounding rectangle around larger motions. It stores the image of the object per frame, naming them in order, in a folder called images. Then when the object is out of the frame, it selects a photo around the middle among all images from the images directory, sends it as an attachment via email and then cleans up the images folder.  

## ⚠️ DISCLAIMER
Ensure that the SMTP credentials are configured as environment variables on the system. The code will not work unless you configure your SMTP credentials in [emailing.py](emailing.py)

## Demo

### Live Motion Detection
![Live motion detection with bounding boxes](screenshots/object.png)

### Email Alert
![Email alert with attached image](screenshots/demomail.png)
