# Graduation_Thesis
## Step 1: Install Visual Studio and MSVC++
Download Visual Studio 2017 or latter, link: https://visualstudio.microsoft.com/ and install with MSVC++
## Step 2: Install Python
Install python >= 3.6.0, don't forget add PATH python
Install requirement.txt in folder **eHealth_Version1.0_01_13_2022_12_47_pm_Release** via command pip **install -r requirement.txt**
## Step 3: Install SQL Server
Install SQL Server 2012 R2 or latter
## Step 4: Download weight file
Download weights file: https://drive.google.com/file/d/1mZxcTWkcwSe9WzrK50GUkXWNDyeZ7T-x/view?usp=sharing
Unzip rar file, copy **brain_seg_unet.hdf5** to folder **ModelAI/Brain_Tumor_Segmentation/weights**, copy **best_xray.pt** to folder **ModelAI/Chest_XRay_YOLOv5/weights**
## Step 5: Restore DataBase
If you are using SQL Server 2012 R2 please restore with file **eHealth_test.bak** in folder **BackupDB**
If you are using higher version please restore with file **script.sql** in folder **BackupDB**
## Step 6: Run
Run program via command python main.py
