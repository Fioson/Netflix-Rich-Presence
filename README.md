# Netflix Rich Presence
### Show what movie/show you're watching and let others see it through Discord Rich Presence
### ⚠️Notice that this is still very buggy, and will have issues.⚠️
![example](https://github.com/RustyBalboadev/Netflix-Rich-Presence/blob/master/example.png)
1. Go to `chrome://extensions`.
2. Turn on Developer Mode.
3. Load Unpacked and select the NetflixRP Folder.
4. Go [here](https://discord.com/developers/applications) and create a new application named "Netflix". **Make sure it isn't a bot!**
5. Click "Rich Presence", then click the add images button and select the `netflix.jpg` photo.
6. Copy the Client ID from the General Information tab, and paste it into `app.py`, where it says "YOUR DISCORD CLIENT ID HERE".
4. CD into FlaskApp
5. Run ```pip install -r requirements.txt```.
6. Then, ```python run.py```.
7. Simply watch Netflix on your computer, and in about a minute, your rich presence should appear! If it doesn't, make sure that you have "Display current activity as a status message" enabled.
