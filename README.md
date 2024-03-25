# Dynamic Language

[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=383938&style=for-the-badge&logo=cheshire_cat_ai)](https://)  
[![Awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=Awesome+plugin&color=000000&style=for-the-badge&logo=cheshire_cat_ai)](https://)  
[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=F4F4F5&style=for-the-badge&logo=cheshire_cat_black)](https://)

Plugin to Dynamically change language of the cat via WebSocket

## Usage

1. Install the plugin (Via the plugin tab of the admin or by uploading the zip file)
2. Activate the plugin
3. Send a ws message like so: 
   ```json
   {
    "text": <message>,
    "lang": "Japanese"
   }
   ```

> **Important**
> 
> Tested only on GPT-4.
> The language must be written in english becuase this plugin depends to the default cat prompt
