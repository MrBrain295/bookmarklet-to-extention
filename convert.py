import json

# Function to get user input for bookmarklet code, extension name, and description
def get_user_input():
    bookmarklet_code = input("Enter your bookmarklet code: ")
    extension_name = input("Enter the extension name: ")
    extension_description = input("Enter the extension description: ")
    return bookmarklet_code, extension_name, extension_description

# Create the manifest.json file with user input
def create_manifest(bookmarklet_code, extension_name, extension_description):
    manifest = {
        "manifest_version": 3,
        "name": extension_name,
        "description": extension_description,
        "version": "1.0",
        "permissions": [],
        "background": {
            "service_worker": "background.js"
        },
        "icons": {
            "16": "icon.png",
            "48": "icon.png",
            "128": "icon.png"
        },
        "action": {
            "default_popup": ""
        }
    }
    with open("manifest.json", "w") as manifest_file:
        json.dump(manifest, manifest_file, indent=4)

# Create the background.js file with the provided bookmarklet code
def create_background_js(bookmarklet_code):
    background_js = f"""chrome.action.onClicked.addListener(function(tab) {{
    chrome.scripting.executeScript({{ target: {{ tabId: tab.id }}, function: function() {{
        var bookmarkletCode = "{bookmarklet_code}";
        eval(bookmarkletCode);
    }} }});
}});
    """
    with open("background.js", "w") as background_file:
        background_file.write(background_js)

# Main program
if __name__ == "__main__":
    bookmarklet_code, extension_name, extension_description = get_user_input()
    create_manifest(bookmarklet_code, extension_name, extension_description)
    create_background_js(bookmarklet_code)
    print("Chrome Extension files created: manifest.json and background.js")

